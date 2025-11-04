from __future__ import annotations
import datetime
from airflow.models.dag import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime.datetime(2025, 1, 1),
    'retries': 0,
    'execution_timeout': datetime.timedelta(minutes=10),
}

with DAG(
    dag_id='hop_sample_pipeline',
    default_args=default_args,
    description='Executa um pipeline de exemplo do Apache Hop no Kubernetes',
    schedule=None,
    catchup=False,
    tags=['hop', 'kubernetes', 'sample'],
) as dag:

    executar_hop_sample = KubernetesPodOperator(
        task_id='executar_hop_sample',
        namespace='default',
        name='hop-sample-pod',
        image='apache/hop:2.9.0',  # imagem oficial do Apache Hop
        image_pull_policy='IfNotPresent',

        # Comando de execução do Hop
        cmds=['/bin/bash', '-c'],
        arguments=[
            'cd /opt/hop && '
            './hop-run.sh '
            '-f samples/pipelines/json-input-to-log.hpl '
            '-r local '
            '-l /tmp/hop-sample.log && '
            'echo "=== PIPELINE EXECUTADO COM SUCESSO ===" && '
            'cat /tmp/hop-sample.log'
        ],

        # Conexão do Kubernetes configurada no Airflow
        kubernetes_conn_id='kind',

        # Logs diretos no Airflow
        get_logs=True,
        do_xcom_push=False,
        is_delete_operator_pod=True,
        startup_timeout_seconds=300,
        resources={"request_cpu": "250m", "request_memory": "256Mi"},
    )


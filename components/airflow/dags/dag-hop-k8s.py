from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime.datetime(2025, 1, 1),
    'retries': 0,
    'execution_timeout': datetime.timedelta(minutes=10),
}

with DAG(
    dag_id='hop_sample_pipeline',
    default_args=default_args,
    description='Executa um pipeline de exemplo do Apache Hop no Kubernetes.',
    schedule=None,
    catchup=False,
    tags=['hop', 'kubernetes', 'sample'],
) as dag:
    
    executar_hop_sample = KubernetesPodOperator(
        task_id='executar_hop_sample',
        namespace='default',
        name='hop-sample-pod',
        image='apache/hop:2.9.0',  # ou a versão que você usa

        env_vars={
            'HOP_LOG_LEVEL': 'Basic',
            'HOP_FILE_PATH': '${PROJECT_HOME}/pipelines/samples/pipeline-hello-world.hpl',
            'HOP_PROJECT_FOLDER': '/files',
            'HOP_PROJECT_NAME': 'samples',
            'HOP_RUN_CONFIG': 'local'
        },

        # monta o volume com os samples do Hop (você pode alterar o path local)
        volumes=[k8s.V1Volume(
            name='hop-samples-volume',
            host_path=k8s.V1HostPathVolumeSource(path='/opt/hop/samples')
        )],
        volume_mounts=[k8s.V1VolumeMount(
            mount_path='/files',
            name='hop-samples-volume'
        )],

        cmds=['/bin/sh', '-c'],
        arguments=['/usr/local/bin/hop-run.sh'],

        get_logs=True,
        is_delete_operator_pod=True,
        kubernetes_conn_id='kind',
        startup_timeout_seconds=300
    )

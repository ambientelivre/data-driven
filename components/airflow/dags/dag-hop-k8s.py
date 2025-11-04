# form Airflow 3.x
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
import timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 0
}

with DAG(
    dag_id="hop_sample_pipeline",
    default_args=default_args,
    description="Executa um sample do Apache Hop usando KubernetesPodOperator",
    schedule=None,
    start_date=datetime.datetime(2025, 1, 1),
    catchup=False,
    tags=["hop", "kubernetes", "samples"],
) as dag:

    executar_hop_sample = KubernetesPodOperator(
        task_id="executar_hop_sample",
        name="hop-sample-pod",
        namespace="default",
        image="apache/hop:2.15.0",
        env_vars={
            "HOP_LOG_LEVEL": "Basic",
            "HOP_FILE_PATH": "/opt/hop/samples/pipelines/01-basic/01-basic.hpl",
            "HOP_PROJECT_FOLDER": "/opt/hop/samples",
            "HOP_PROJECT_NAME": "samples",
            "HOP_RUN_CONFIG": "local",
        },
        kubernetes_conn_id="kind",
        is_delete_operator_pod=True,
        in_cluster=False,
        do_xcom_push=False,
    )

    executar_hop_sample

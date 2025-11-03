from __future__ import annotations

import datetime

from airflow.models.dag import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from kubernetes.client import models as k8s

# Argumentos Padrão para a DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime.datetime(2025, 1, 1), # Data de início no futuro, apenas para referência
    'retries': 0,
    'execution_timeout': datetime.timedelta(minutes=5),
}

# Definição do DAG
with DAG(
    dag_id='kubernetes_hello_world',
    default_args=default_args,
    description='Executa um Pod simples de Hello World no Kubernetes (Kind).',
    schedule=None,  # Configurado para execução manual
    catchup=False,
    tags=['kubernetes', 'demo', 'hello-world'],
) as dag:
    
    # Tarefa que cria e executa o Pod
    hello_k8s_pod = KubernetesPodOperator(
        # ID Único da Tarefa
        task_id='executar_hello_world_pod',
        # O namespace onde o Pod será criado. Deve ser o mesmo onde o Airflow opera (e tem permissão).
        namespace='default', 
        # Nome do Pod (útil para debug com kubectl get pods)
        name='hello-world-pod',
        # Imagem a ser usada no contêiner
        image='ubuntu:latest',

        # Comando a ser executado no Pod
        cmds=['/bin/bash', '-c'],
        arguments=['echo "Hello World from Kubernetes!"; sleep 1; date;'],

        # Se for True, o log do Pod é puxado para os logs da tarefa do Airflow
        do_xcom_push=False,
        # Remove o Pod após a conclusão da tarefa (recomendado para limpeza)
        is_delete_operator_pod=True,
        # Define o modo de reinicialização para nunca, o que é padrão para tarefas únicas.
        startup_timeout_seconds=300
    )

    # A DAG tem apenas uma tarefa:
    # hello_k8s_pod

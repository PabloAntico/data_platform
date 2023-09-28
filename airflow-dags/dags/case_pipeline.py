from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime, timedelta
from airflow.models import Variable
from kubernetes.client import models as k8s

AWS_ACCESS_KEY_ID = Variable.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = Variable.get("AWS_SECRET_ACCESS_KEY")

default_args = {
    'owner': 'Pablo Antico',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 20),
    'retries': 3,
    'retry_delay': timedelta(minutes=2),
    # KubernetesPodOperator Defaults
    'namespace': 'default',
    'in_cluster': True,
    'get_logs': True,
    'is_delete_operator_pod': True
}

dag = DAG('data-platform-case',
          default_args=default_args,
          description='Kubernetes Pod Operator - Downloading and Loading Data',
          schedule_interval='0 6 * * *',
          start_date=datetime(2023, 9, 15),
          catchup=False)

configmaps = [k8s.V1EnvFromSource(config_map_ref=k8s.V1ConfigMapEnvSource(name='my-configs'))]

download_data = KubernetesPodOperator(
            image="localhost:5001/airflow_task:1.0.0",
            cmds=["/bin/bash", "-c"],
            arguments=[f"python3 download_data.py {AWS_ACCESS_KEY_ID} {AWS_SECRET_ACCESS_KEY}"],
            env_from=configmaps,
            name=f"download_data",
            task_id=f"download_data",
            retries=3,
            retry_delay=timedelta(minutes=2),
            dag=dag,
        )

load_data = KubernetesPodOperator(
            image="localhost:5001/airflow_task:1.0.0",
            cmds=["/bin/bash", "-c"],
            arguments=[f"python3 load_data.py {AWS_ACCESS_KEY_ID} {AWS_SECRET_ACCESS_KEY}"],
            env_from=configmaps,
            name=f"load_data",
            task_id=f"load_data",
            retries=3,
            retry_delay=timedelta(minutes=2),
            dag=dag,
        )

download_data >> load_data
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'start_date': days_ago(1),
    'catchup': False,
}

dag = DAG(
    'spark_example',
    default_args=default_args,
    schedule_interval='@daily',
    description='Run a Spark job from Airflow'
)

run_spark = BashOperator(
    task_id='run_spark_job',
    bash_command="""
    jupyter nbconvert --to script /mnt/shared/notebooks/spark_job.ipynb --output /mnt/shared/notebooks/spark_job &&
    docker exec spark-master-1 spark-submit --master spark://spark-master:7077 /mnt/shared/notebooks/spark_job.py
    """,
    dag=dag
)
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def extract_and_load():
    print("Executing pipeline step...")

default_args = {
    'owner': 'data_team',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

# Schedule using cron syntax (Runs daily at midnight)
with DAG(
    dag_id='data_pipeline_v1',
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule_interval='0 0 * * *', 
    catchup=False
) as dag:

    execute_pipeline = PythonOperator(
        task_id='run_pipeline_task',
        python_callable=extract_and_load
    )
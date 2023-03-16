from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "prithoo",
    "retries": 5,
    "retry_delay": timedelta(minutes=2)
}

with DAG(
    dag_id = "our_first_dag",
    default_args = default_args,
    description = "This is the first Directed Acyclic Graph that we wrote in Apache Airflow.",
    start_date = datetime(2023, 3, 17, 0, 27, 0, 0),
    schedule_interval = "@daily"
) as dag:
    task_1 = BashOperator(
        task_id = "first_task",
        bash_command = "echo 'Hello World! This is the first task.'"
    )

    task_1

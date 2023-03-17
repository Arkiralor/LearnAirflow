"""
We will use this to create a python operation using the PythonOperator in Airflow.
"""
from datetime import datetime, timedelta
from pytz import timezone

from airflow import DAG
from airflow.operators.python import PythonOperator


def greet() -> None:
    print(f"[{datetime.now(tz=timezone('Asia/Kolkata'))}]\tHello, from the python DAG!")


default_args = {
    "owner": "prithoo",
    "retries": 5,
    "retry_delay": timedelta(seconds=5)
}

datetime_obj = datetime(
    year=2023,
    month=3,
    day=16,
    hour=7,
    minute=40,
    second=0,
    microsecond=0,
    tzinfo=timezone('Asia/Kolkata')
)

with DAG(
    dag_id="python_operation",
    default_args=default_args,
    description="This is a python operation in Apache Airflow using the basic `PythonOperator`.",
    start_date=datetime_obj,
    schedule_interval="@daily"
) as dag:
    task1 = PythonOperator(
        task_id="greet",
        python_callable=greet
    )

    task1

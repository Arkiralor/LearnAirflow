"""
We will use this to create a python operation using the PythonOperator in Airflow.
"""
from datetime import datetime, timedelta
from pytz import timezone

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models.taskinstance import TaskInstance

DAG_ID = "python_operation_v10"
NAME = "Artoria Uthersdottir Pendragon"


def greet(ti:TaskInstance, age:int=None) -> None:
    name = ti.xcom_pull(task_ids="get_name", dag_id=DAG_ID)

    resp = f"[{datetime.now(tz=timezone('Asia/Kolkata'))}]\tHello, from the python DAG!"
    if name and not age:
        resp = f"[{datetime.now(tz=timezone('Asia/Kolkata'))}]\tHello, from the python DAG! My name is {name}."
    elif age and not name:
        resp = f"[{datetime.now(tz=timezone('Asia/Kolkata'))}]\tHello, from the python DAG! I am {age} year old" if age == 1 else f"[{datetime.now(tz=timezone('Asia/Kolkata'))}]\tHello, from the python DAG! I am {age} years old."
    elif name and age:
        resp = f"[{datetime.now(tz=timezone('Asia/Kolkata'))}]\tHello, from the python DAG! My name is {name} and I am {age} year old" if age == 1 else f"[{datetime.now(tz=timezone('Asia/Kolkata'))}]\tHello, from the python DAG! My name is {name} and I am {age} years old."
    else:
        resp = f"Invalid argument(s):\n\tNAME: {name}\n\tAGE: {age}"
    print(resp)

    return True


def get_name():
    return NAME


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
    dag_id=DAG_ID,
    default_args=default_args,
    description="This is a python operation in Apache Airflow using the basic `PythonOperator`.",
    start_date=datetime_obj,
    schedule_interval="@daily"
) as dag:
    task1 = PythonOperator(
        task_id="get_name",
        python_callable=get_name
    )

    task2 = PythonOperator(
        task_id="greet",
        python_callable=greet,
        op_kwargs = {
            "age": 30
        }
    )

    task1 >> task2

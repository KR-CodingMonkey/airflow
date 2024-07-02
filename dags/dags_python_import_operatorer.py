from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from common.common import get_sftp

import datetime
import pendulum
import random

with DAG(
    dag_id="dags_python_operator",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
) as dag:
    task_get_sftp = PythonOperator(
        task_id = "py_t1",
        python_callable=get_sftp # 어떤 함수를 실행할 건지 명시
    )

    task_get_sftp
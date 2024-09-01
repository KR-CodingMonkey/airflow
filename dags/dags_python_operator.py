from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator

import datetime
import pendulum
import random

with DAG(
    dag_id="dags_python_operator",
    schedule="0 9 * * *",
    start_date=pendulum.datetime(2024, 8, 25, tz="UTC"),
    catchup=False,
) as dag:
    def select_pet():
        pet = ['DOG', "CAT", "MONKEY", "BIRD"]
        rand_int = random.randint(0,3)
        print(pet[rand_int])


    py_t1 = PythonOperator(
        task_id = "py_t1",
        python_callable=select_pet # 어떤 함수를 실행할 건지 명시
    )

    py_t1
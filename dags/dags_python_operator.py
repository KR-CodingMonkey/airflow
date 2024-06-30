from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator

import datetime
import pendulum
import random

with DAG(
    dag_id="dags_python_operator",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
) as dag:
    def select_fruit():
        fruit = ['APPLE', "BANANA", "ORANGE", "AVOCADO"]
        rand_int = random.randint(0,3)
        print(fruit[rand_int])
    
        pass
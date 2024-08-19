from airflow import DAG
import pendulum

with DAG(
    dag_id="dags_python_task_decorator",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz='UTC'),
    catchup=False,
    tags=["example"]
) as dag:
    
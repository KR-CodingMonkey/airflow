from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from common.common_func import import_python_func
import datetime
import pendulum

with DAG(
    dag_id="dags_python_import",
    schedule="0 9 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    task_import_func = PythonOperator(
        task_id = "py_t1",
        python_callable=import_python_func # 어떤 함수를 실행할 건지 명시
    )

    task_import_func
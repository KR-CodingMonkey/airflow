from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from common.common_func import register
import pendulum

with DAG(
    dag_id="dags_python_operator_args",
    schedule="0 9 * * *",
    start_date=pendulum.datetime(2024, 8, 25, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    py_t1 = PythonOperator(
        task_id = "py_t1",
        python_callable = register,
        op_args = ['dave', 'male', 'korea', 'seoul', '21']
    )

    py_t1
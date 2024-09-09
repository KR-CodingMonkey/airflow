from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from common.common_func import register_kwargs, register_args_kwargs
import pendulum

with DAG(
    dag_id="dags_python_operator_kwargs",
    schedule="0 9 * * *",
    start_date=pendulum.datetime(2024, 8, 25, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    t1_kwargs = PythonOperator(
        task_id = "t1_kwargs",
        python_callable = register_kwargs,
        op_kwargs = {'name':'dave', 'gender':'male', 'country':'korea', 'city':'seoul', 'age':'21'}
    )
    
    t2_args_kwargs = PythonOperator(
        task_id = "t2_args_kwargs",
        python_callable = register_args_kwargs,
        op_args = ['dave', 'male', 'korea', 'seoul'],
        op_kwargs = {'age':'21', 'email':"airflow@google.com"}
    )
    

    t1_kwargs >> t2_args_kwargs
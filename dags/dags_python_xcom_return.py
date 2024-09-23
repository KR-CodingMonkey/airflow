from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
import datetime
import pendulum

with DAG(
    dag_id="dags_python_xcom_return",
    schedule="0 9 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    def xcom_push_return():
            value3 = "value3"
            return value3
            
    def xcom_pull_return(**kwargs):
            ti = kwargs['ti']
            ti_value3 = ti.xcom_pull(key='return_value', task_ids="xcom_push_by_return")
            print(ti_value3)
            
    xcom_push_by_return = PythonOperator(
        task_id = "xcom_push_by_return",
        python_callable=xcom_push_return
    )
    
    xcom_pull_by_return = PythonOperator(
        task_id = "xcom_pull_by_return",
        python_callable=xcom_pull_return
    )

    xcom_push_by_return >> xcom_pull_by_return
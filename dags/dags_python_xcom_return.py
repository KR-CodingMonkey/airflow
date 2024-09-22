from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
import datetime
import pendulum

with DAG(
    dag_id="dags_python_xcom",
    schedule="0 9 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    def xcom_push(**kwargs):
            ti = kwargs['ti']
            ti.xcom_push(key='key1', value="value1")
            ti.xcom_push(key='key2', value=[1,2,3,4])
            
    def xcom_pull(**kwargs):
            ti = kwargs['ti']
            ti_value1 = ti.xcom_pull(key='key1', task_ids="xcom_ti_push")
            ti_value2 = ti.xcom_pull(key='key2', task_ids="xcom_ti_push")
            print(ti_value1)
            print(ti_value2)
            
    xcom_ti_push = PythonOperator(
        task_id = "xcom_ti_push",
        python_callable=xcom_push
    )
    
    xcom_ti_pull = PythonOperator(
        task_id = "xcom_ti_pull",
        python_callable=xcom_pull
    )

    xcom_ti_push >> xcom_ti_pull
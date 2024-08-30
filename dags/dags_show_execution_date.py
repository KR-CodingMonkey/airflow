from airflow.models.dag import DAG
from airflow.decorators import task
from pprint import pprint
import datetime
import pendulum

with DAG(
    dag_id="dags_show_execution_date",
    schedule_interval="@daily",
    start_date=pendulum.datetime(2024, 8, 1, tz="Asia/Seoul"),
    end_date=pendulum.datetime(2024, 8, 30, tz="Asia/Seoul"),
    catchup=True,
) as dag:
    
    @task(task_id='executeion_date')
    def show_execution_date(**kwargs):
        pprint(kwargs)

    show_execution_date()
        
    


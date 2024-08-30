from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
# from airflow.operators.empty import EmptyOperator
import datetime
import pendulum # datetime 자료형을 쉽게 다룰 수 있게 해줌

with DAG(
    dag_id="dags_daily_schedule",
    schedule_interval="@daily",
    start_date=pendulum.datetime(2023, 1, 1, tz="Asia/Seoul"),
    end_date=pendulum.datetime(2023, 2, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    


from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
import datetime
import pendulum

with DAG(
    dag_id="dags_bash_operator_xcom",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["example", "example2"],
    params={"example_key": "example_value"},
) as dag:
    
    BASE_TIME = "{{data_interval_end.in_timezone('Asia/Seoul').strftime('%Y%m%d')}}"
    
    t1_push = BashOperator(
    task_id="t1_push",
    bash_command="echo {{ti.xcom_push(key='bash_xcom_key1', value='bash_xcom_value1')}} &&"
                 f"echo today is {BASE_TIME}",
    do_xcom_push=True
    )

    t2_pull = BashOperator(
    task_id="t2_pull",
    env={'PUSH_VALUE': "{{ti.xcom_pull(key='bash_xcom_key1')}}",
        'RETURN_VALUE': "{{ti.xcom_pull(task_ids='t1_push')}}"},
    bash_command="echo $PUSH_VALUE && echo $RETURN_VALUE",
    do_xcom_push=False
    )

    t1_push >> t2_pull
       
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
import datetime
import pendulum

with DAG(
    dag_id="dags_bash_my_pet",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2023, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    t1_mypet_dog = BashOperator(
    task_id="t1_mypet_dog",
    bash_command="/opt/airflow/plugins/shell/mypet.sh dog",
    )

    t2_mypet_cat = BashOperator(
    task_id="t2_mypet_cat",
    bash_command="/opt/airflow/plugins/shell/mypet.sh cat",
    )

    t3_mypet_pig = BashOperator(
    task_id="t3_mypet_pig",
    bash_command="/opt/airflow/plugins/shell/mypet.sh pig",
    )

    t1_mypet_dog >> t2_mypet_cat >> t3_mypet_pig
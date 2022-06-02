import airflow.utils.dates as dates
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

DIR_PATH="/opt/airflow/igkim/wiki"

dag=DAG(
    dag_id="11_context_args",
    start_date=dates.days_ago(3),
    schedule_interval="@daily",
    # catchup=False,
    tags=['igkim', 'test'],
)

def _print_context(**kwargs):
    print(kwargs)

print_context=PythonOperator(
    task_id="print_context",
    python_callable=_print_context,
    dag=dag,
)


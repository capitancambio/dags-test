
"""
Code that goes along with the Airflow located at:
    http://airflow.readthedocs.org/en/latest/tutorial.html
    """

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2018, 11, 20),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(seconds=1),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}


dag = DAG(
    "celery_remote", default_args=default_args, schedule_interval=None)

one = PythonOperator(task_id="one_task",
                     python_callable=print,
                     op_args=["this is one"],
                     dag=dag)

two = PythonOperator(task_id="another_task",
                     python_callable=print,
                     op_args=["this is two"],
                     dag=dag)


two.set_upstream(one)
# t2.set_upstream(t1)
# t3.set_upstream(t1)

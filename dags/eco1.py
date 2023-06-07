from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.models.variable import Variable

today= '{{ execution_date.add(hours=9).format("%Y%m%d") }}'
year= '{{ execution_date.add(hours=9).format("%Y") }}'
month= '{{ execution_date.add(hours=9).format("%m") }}'
day= '{{ execution_date.add(hours=9).format("%d") }}'

# DAG 생성
dag = DAG('eco-pipeline', description='pipeline', start_date=datetime(2023, 6, 7), schedule_interval=None)

# 더미 오퍼레이터 생성
load_data = DummyOperator(task_id='load_data', dag=dag)
call_api = DummyOperator(task_id='api_data', dag=dag)
trans_data_keyward = DummyOperator(task_id='trans_data_keyward', dag=dag)
trans_data_category = DummyOperator(task_id='trans_data_category', dag=dag)
load_trans_data = DummyOperator(task_id='load_trans_data', dag=dag)
service_start = DummyOperator(task_id='service_start', dag=dag)
user_emotion=DummyOperator(task_id='user_emotion', dag=dag)
user_time=DummyOperator(task_id='user_time', dag=dag)
apply_user=DummyOperator(task_id='apply_user', dag=dag)
visualize=DummyOperator(task_id='visualize', dag=dag)
end_task = DummyOperator(task_id='end_task', dag=dag)

# 작업 간의 의존성 정의
call_api >>load_data >>trans_data_keyward>> load_trans_data
load_data >>trans_data_category>> load_trans_data
load_trans_data >> service_start
service_start >> user_time >> apply_user
service_start >> user_emotion >> apply_user

apply_user >> visualize >> end_task


from airflow import DAG 
from airflow.operators.bash_operator import BashOperator 
from airflow.operators.dummy_operator import DummyOperator 
from airflow.utils.dates import days_ago 
from airflow.operators.python_operator import PythonOperator 

default_args = { 
    'owner': 'alisa', 
    'start_date': days_ago(1) 
    } 

 
# Defining the DAG using Context Manager 
with DAG( 
        'bash_write', 
        default_args=default_args, 
        schedule_interval=None, 
        ) as dag: 


    t1 = BashOperator( 
                    task_id = 'create_task', 
                    bash_command = 'python pi.py'
            ) 

#start = DummyOperator(task_id='start', dag=dag) 
end = DummyOperator(task_id='end', dag=dag) 

#step 5 - Define Dependency 

#start >> end 

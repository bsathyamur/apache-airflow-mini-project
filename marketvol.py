from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from y_finance import stock_yfinance
from queryFiles import queryData
from airflow import DAG

#default_args = {
#    'owner': 'admin',
#    'start_date': datetime(2021,3,5),
#    'retries': 2,
#    'retry_delay': timedelta(minutes=5),
#}

default_args = {
    'owner': 'admin',
    'start_date': datetime(2021,3,5)
}

# Initialize the DAG
dag = DAG('marketvol',
	      default_args=default_args,
	      description='A simple DAG on stock market volume',
	      schedule_interval='0 18 * * 1-5'
	      )

# BashOperator to initialize a temporary directory for data download

templated_command1 = """
  mkdir -p ~/desktop/airflow-prj/tmp/data/{{ ds }}
"""

task0 = BashOperator(task_id='create_folder_task',
                     bash_command=templated_command1,
                     dag=dag)

EXEC_DATE = '{{ ds }}'

# Python operator to download TSLA data
task1 = PythonOperator(dag=dag,
                       task_id='download_yfinance_tsla',
                       python_callable=stock_yfinance,
                       provide_context=True,
                       op_kwargs={'symbol': 'TSLA','execution_dt':EXEC_DATE})

# Python operator to download AAPL data
task2 = PythonOperator(dag=dag,
                       task_id='download_yfinance_aapl',
                       python_callable=stock_yfinance,
                       provide_context=True,                       
                       op_kwargs={'symbol': 'AAPL','execution_dt':EXEC_DATE})

templated_command2 = """
  cp ~/desktop/airflow-prj/tmp/data/{{ ds }}/TSLA*.csv ~/desktop/stocksdata/
"""

# Python operator to download AAPL data
task3 = BashOperator(task_id='copy_tsla_files',
                     bash_command=templated_command2,
                     dag=dag)

templated_command3 = """
  cp ~/desktop/airflow-prj/tmp/data/{{ ds }}/AAPL*.csv ~/desktop/stocksdata/
"""

# Python operator to download AAPL data
task4 = BashOperator(task_id='copy_aapl_files',
                     bash_command=templated_command3,
                     dag=dag)


# Python operator to process the data
task5 = PythonOperator(dag=dag,
                       task_id='process_data',
                       python_callable=queryData)

task0 >> task1 >> task3 
task0 >> task2 >> task4
task3 >> task5
task4 >> task5
# apache-airflow-mini-project

## Objective:
 use Apache Airflow to create a data pipeline to extract online stock market data and deliver analytical results

## Details of the DAG 
Task0: BashOperator to download to create a folder for downloading the data
Task1: PythonOperator to call the yahoo finance API to download the data and move to a temporary location for TESLA
Task2: PythonOperator to call the yahoo finance API to download the data and move to a temporary location for AAPL
Task3: BashOperator to move the downloaded TESLA data files to the final location
Task4: BashOperator to move the downloaded AAPL data files to the final location
Task5: PythonOperator to process the data downloaded to the final location

## DAG dependency details
Task0 >> Task1 >> Task3 >> Task5
Task0 >> Task2 >> Task4 >> Task5

## Output
![img](https://github.com/bsathyamur/apache-airflow-mini-project/blob/main/workflow-pic.png)

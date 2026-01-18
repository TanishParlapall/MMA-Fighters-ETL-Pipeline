from airflow import DAG
import os
import pandas as pd
from datetime import datetime, timedelta
import requests
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from scripts.extract_data import fetch_MMA_data
from scripts.create_table import create_table
from scripts.load_data import load_into_postgres

# default DAG args
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 16),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG definition
dag = DAG(
    'fetch_and_store_MMA_data',
    default_args=default_args,
    description='first DAG',
    schedule='@daily',
)

# tasks
fetch_MMA_data_task = PythonOperator(
    task_id='fetch_MMA_data',
    python_callable=fetch_MMA_data,
    dag=dag,
)

create_table_task = PythonOperator(
    task_id="create_table_task",
    python_callable=create_table,
    dag=dag,
)

insert_fighter_data_task = PythonOperator(
    task_id="insert_fighter_data",
    python_callable=load_into_postgres,
    dag=dag,
)

# dependencies
fetch_MMA_data_task >> create_table_task >> insert_fighter_data_task

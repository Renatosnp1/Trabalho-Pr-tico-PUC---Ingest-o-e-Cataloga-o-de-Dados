from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import ingestao

default_args = {
    'owner': 'faculdade',
    'start_date': datetime(2024, 1, 1),
}

dag = DAG('ingestao_dados_faculdade', default_args=default_args, schedule_interval='@daily')

ingestao_tarefa = PythonOperator(
    task_id='ingestao_raw_para_staging',
    python_callable=ingestao_csv_para_parquet,
    op_kwargs={'input_path': 'datalake-dados-faculdade/raw/alunos/alunos.csv',
               'output_path': 'datalake-dados-faculdade/staging/alunos/alunos.parquet'},
    dag=dag,
)

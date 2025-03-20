from airflow import DAG
from airflow.providers.google.cloud.operators.gcs import GCSHook
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import json

# Configuração padrão da DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 3, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'load_guardian_news',
    default_args=default_args,
    description='Carrega notícias do The Guardian do GCS para BigQuery',
    schedule_interval='0 1 * * *',  # Executa diariamente às 01:00 UTC
    catchup=False,
)

# Informações do Cloud Storage e BigQuery
BUCKET_NAME = 'bucket_scrapy' 
FILE_NAME = 'output.json'
BQ_DATASET = 'guardian_news'
BQ_TABLE = 'articles'


def fetch_from_gcs():
    """Baixa o arquivo JSON do Cloud Storage."""
    hook = GCSHook()
    data = hook.download(bucket_name=BUCKET_NAME, object_name=FILE_NAME)
    return json.loads(data)


def insert_into_bigquery():
    """Carrega os dados no BigQuery."""
    hook = GCSHook()
    data = hook.download(bucket_name=BUCKET_NAME, object_name=FILE_NAME)
    records = json.loads(data)

    query = f"""
    INSERT INTO `{BQ_DATASET}.{BQ_TABLE}` (title, author, published_date, url, content)
    VALUES {", ".join([f"('{r['title']}', '{r['author']}', '{r['published_date']}', '{r['url']}', '{r['content']}')" for r in records])}
    """

    return query


# Task 1: Baixar arquivo do GCS
fetch_task = PythonOperator(
    task_id='fetch_from_gcs',
    python_callable=fetch_from_gcs,
    dag=dag,
)

# Task 2: Inserir no BigQuery
upload_task = BigQueryInsertJobOperator(
    task_id='upload_to_bigquery',
    configuration={"query": {"query": insert_into_bigquery(), "useLegacySql": False}},
    dag=dag,
)

# Define a ordem das tarefas
fetch_task >> upload_task

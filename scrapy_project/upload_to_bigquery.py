import json
from google.cloud import bigquery

def upload_to_bigquery():
    print("Starting BigQuery upload...")

    client = bigquery.Client()
    dataset_id = 'guardian_news'
    table_id = 'articles'

    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    print("Checking if table exists...")
    try:
        table = client.get_table(table_ref)
    except Exception as e:
        print(f"Error fetching table: {e}")
        return

    print("Reading JSON file...")
    try:
        # Caminho do arquivo no Composer
        file_path = '/home/airflow/gcs/scripts/scrapy_project/output.json'
        with open(file_path, 'r') as f:
            records = json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return

    if not records:
        print("No records found in JSON file. Exiting...")
        return

    print(f"Read {len(records)} records. Preparing for upload...")

    rows_to_insert = []
    for record in records:
        row = {
            'title': record.get('title'),
            'link': record.get('link'),
            'section': record.get('section'),
            'publication_date': record.get('publication_date'),
            'api_url': record.get('api_url'),
            'pillar_name': record.get('pillar_name')
        }
        rows_to_insert.append(row)

    print("Inserting records into BigQuery...")
    errors = client.insert_rows_json(table, rows_to_insert)

    if errors:
        print("Errors encountered while inserting rows:")
        for error in errors:
            print(error)
    else:
        print("Data uploaded successfully.")

if __name__ == "__main__":
    upload_to_bigquery()
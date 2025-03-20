import json
from google.cloud import storage
import os

class SaveToGCS:
    def __init__(self):
        self.bucket_name = "bucket_scrapy" 
        self.file_name = "output.json"  
        self.data = []

    def process_item(self, item, spider):
        self.data.append(dict(item))
        return item

    def close_spider(self, spider):
        client = self.get_gcs_client()
        bucket = client.bucket(self.bucket_name)
        blob = bucket.blob(self.file_name)

        # Salva os dados no Cloud Storage
        blob.upload_from_string(json.dumps(self.data, indent=2), content_type="application/json")
        spider.logger.info(f"Arquivo {self.file_name} salvo no GCS: gs://{self.bucket_name}/{self.file_name}")

    @staticmethod
    def get_gcs_client():
        credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        if not credentials_path or not os.path.exists(credentials_path):
            raise ValueError(f"Credenciais não encontradas: {credentials_path}")
        return storage.Client.from_service_account_json(credentials_path)

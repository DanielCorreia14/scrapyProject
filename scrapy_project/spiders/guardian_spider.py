# import os
# import sys
# import scrapy
# import json
# from google.cloud import storage
# from scrapy_project.items import ScrapyProjectItem

# sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# class GuardianSpider(scrapy.Spider):
#     name = "guardian_spider"
#     api_key = "347ab7cd-9e75-46a5-b575-f8666b8b050f"
#     start_urls = [
#         f"https://content.guardianapis.com/search?api-key={api_key}&show-fields=body,headline,trailText,byline&page-size=100&order-by=newest"
#     ]

#     output_file = "scrapy_project/output.json"  # Caminho relativo dentro do container
#     bucket_name = "bucket_scrapy"  # Nome do seu bucket no Cloud Storage

#     def parse(self, response):
#         try:
#             data = json.loads(response.text)
#             articles = data.get('response', {}).get('results', [])
#         except json.JSONDecodeError:
#             self.logger.error("Erro ao decodificar JSON!")
#             return

#         scraped_data = []
#         for article in articles:
#             item = {
#                 "title": article.get("webTitle", "N/A"),
#                 "link": article.get("webUrl", "N/A"),
#                 "section": article.get("sectionName", "N/A"),
#                 "publication_date": article.get("webPublicationDate", "N/A"),
#                 "api_url": article.get("apiUrl", "N/A"),
#                 "pillar_name": article.get("pillarName", "N/A")
#             }
#             scraped_data.append(item)
        
#         # Salvar os dados localmente
#         self.save_to_json(scraped_data)

#         # Fazer o upload para o Cloud Storage
#         self.upload_to_gcs(self.output_file, self.bucket_name)

#     def save_to_json(self, data):
#         os.makedirs(os.path.dirname(self.output_file), exist_ok=True)  # Cria a pasta se não existir
#         with open(self.output_file, "w", encoding="utf-8") as f:
#             json.dump(data, f, indent=4, ensure_ascii=False)
#         self.log(f"Dados salvos localmente em {self.output_file}")

#     def upload_to_gcs(self, source_file_name, bucket_name):
#         """Faz upload do arquivo JSON para o Cloud Storage."""
#         try:
#             if os.path.getsize(source_file_name) > 0:  # Verifica se o arquivo não está vazio
#                 storage_client = storage.Client()
#                 bucket = storage_client.bucket(bucket_name)
#                 blob = bucket.blob(os.path.basename(source_file_name))
#                 blob.upload_from_filename(source_file_name)
#                 self.log(f"Arquivo {source_file_name} enviado para gs://{bucket_name}/output.json")
#             else:
#                 self.log("Arquivo vazio, não enviado para o Cloud Storage")
#         except Exception as e:
#             self.log(f"Erro ao enviar para Cloud Storage: {e}")


# import os
# import sys
# import scrapy
# import json
# from google.cloud import storage
# from scrapy_project.items import ScrapyProjectItem

# sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# class GuardianSpider(scrapy.Spider):
#     name = "guardian_spider"
#     api_key = "347ab7cd-9e75-46a5-b575-f8666b8b050f"
#     start_urls = [
#         f"https://content.guardianapis.com/search?api-key={api_key}&show-fields=body,headline,trailText,byline&page-size=100&order-by=newest"
#     ]

#     output_file = "scrapy_project/output.json"  # Caminho relativo dentro do container
#     bucket_name = "bucket_scrapy"  # Nome do bucket no Cloud Storage

#     def parse(self, response):
#         try:
#             data = json.loads(response.text)
#             articles = data.get('response', {}).get('results', [])
#         except json.JSONDecodeError:
#             self.logger.error("Erro ao decodificar JSON!")
#             return

#         self.log(f"API retornou {len(articles)} artigos")  # Log para debug

#         scraped_data = []
#         for article in articles:
#             item = {
#                 "title": article.get("webTitle", "N/A"),
#                 "link": article.get("webUrl", "N/A"),
#                 "section": article.get("sectionName", "N/A"),
#                 "publication_date": article.get("webPublicationDate", "N/A"),
#                 "api_url": article.get("apiUrl", "N/A"),
#                 "pillar_name": article.get("pillarName", "N/A")
#             }
#             scraped_data.append(item)
        
#         # Salvar os dados localmente
#         self.save_to_json(scraped_data)

#         # Fazer o upload para o Cloud Storage
#         self.upload_to_gcs(self.output_file, self.bucket_name)

#     def save_to_json(self, data):
#         os.makedirs(os.path.dirname(self.output_file), exist_ok=True)  # Cria a pasta se não existir

#         with open(self.output_file, "w", encoding="utf-8") as f:
#             json.dump(data, f, indent=4, ensure_ascii=False)

#         self.log(f"Arquivo salvo localmente em {self.output_file}")

#     def upload_to_gcs(self, source_file_name, bucket_name):
#         """Faz upload do arquivo JSON para o Cloud Storage."""
#         try:
#             if not os.path.exists(source_file_name):
#                 self.log(f"Erro: Arquivo {source_file_name} não encontrado!")
#                 return
            
#             file_size = os.path.getsize(source_file_name)
#             self.log(f"Tamanho do arquivo antes do upload: {file_size} bytes")

#             if file_size > 0:
#                 storage_client = storage.Client()
#                 bucket = storage_client.bucket(bucket_name)
#                 blob = bucket.blob("output.json")
#                 blob.upload_from_filename(source_file_name)
#                 self.log(f"Nome do arquivo local: {source_file_name}")
#                 self.log(f"Nome do arquivo no GCS: {os.path.basename(source_file_name)}")

#                 self.log(f"Arquivo {source_file_name} enviado para gs://{bucket_name}/output.json")
#             else:
#                 self.log("Arquivo vazio, não enviado para o Cloud Storage")
#         except Exception as e:
#             self.log(f"Erro ao enviar para Cloud Storage: {e}")
import os
import sys
import scrapy
import json
from google.cloud import storage
from scrapy_project.items import ScrapyProjectItem

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

class GuardianSpider(scrapy.Spider):
    name = "guardian_spider"
    api_key = "347ab7cd-9e75-46a5-b575-f8666b8b050f"
    start_urls = [
        f"https://content.guardianapis.com/search?api-key={api_key}&show-fields=body,headline,trailText,byline&page-size=100&order-by=newest"
    ]

    output_file_json = "scrapy_project/output.json"  # Caminho para JSON
    output_file_txt = "scrapy_project/output.txt"  # Caminho para TXT
    bucket_name = "bucket_scrapy"  # Nome do bucket no Cloud Storage

    def parse(self, response):
        try:
            data = json.loads(response.text)
            articles = data.get('response', {}).get('results', [])
        except json.JSONDecodeError:
            self.logger.error("Erro ao decodificar JSON!")
            return

        self.log(f"API retornou {len(articles)} artigos")  # Log para debug

        scraped_data = []
        for article in articles:
            item = {
                "title": article.get("webTitle", "N/A"),
                "link": article.get("webUrl", "N/A"),
                "section": article.get("sectionName", "N/A"),
                "publication_date": article.get("webPublicationDate", "N/A"),
                "api_url": article.get("apiUrl", "N/A"),
                "pillar_name": article.get("pillarName", "N/A")
            }
            scraped_data.append(item)
        
        # Salvar os dados em JSON e TXT
        self.save_to_json(scraped_data)
        self.save_to_txt(scraped_data)

        # Fazer o upload para o Cloud Storage
        self.upload_to_gcs(self.output_file_txt, self.bucket_name)

    def save_to_json(self, data):
        os.makedirs(os.path.dirname(self.output_file_json), exist_ok=True)  # Cria a pasta se não existir
        with open(self.output_file_json, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        self.log(f"Arquivo JSON salvo localmente em {self.output_file_json}")

    def save_to_txt(self, data):
        os.makedirs(os.path.dirname(self.output_file_txt), exist_ok=True)
        with open(self.output_file_txt, "w", encoding="utf-8") as f:
            for article in data:
                f.write(f"Título: {article['title']}\n")
                f.write(f"Link: {article['link']}\n")
                f.write(f"Seção: {article['section']}\n")
                f.write(f"Data de publicação: {article['publication_date']}\n")
                f.write(f"Pilar: {article['pillar_name']}\n")
                f.write("=" * 40 + "\n")  # Separador entre os artigos

        self.log(f"Arquivo TXT salvo localmente em {self.output_file_txt}")

    def upload_to_gcs(self, source_file_name, bucket_name):
        """Faz upload do arquivo TXT para o Cloud Storage."""
        try:
            if not os.path.exists(source_file_name):
                self.log(f"Erro: Arquivo {source_file_name} não encontrado!")
                return
            
            file_size = os.path.getsize(source_file_name)
            self.log(f"Tamanho do arquivo antes do upload: {file_size} bytes")

            if file_size > 0:
                storage_client = storage.Client()
                bucket = storage_client.bucket(bucket_name)
                blob = bucket.blob("output.txt")  # Agora sobe como .txt
                blob.upload_from_filename(source_file_name)
                
                self.log(f"Arquivo {source_file_name} enviado para gs://{bucket_name}/output.txt")
            else:
                self.log("Arquivo vazio, não enviado para o Cloud Storage")
        except Exception as e:
            self.log(f"Erro ao enviar para Cloud Storage: {e}")

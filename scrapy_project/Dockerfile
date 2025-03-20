FROM python:3.10-slim

# Ajustando o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . /app/

# Copia o arquivo de credenciais para dentro do container
COPY scrapy-project-452300-bead235bea85.json /app/

# Define a variável de ambiente para as credenciais do GCP
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/scrapy-project-452300-bead235bea85.json"

RUN pip install --no-cache-dir -r requirements.txt

# Move os arquivos Python para dentro do módulo scrapy_project
RUN mkdir -p /app/scrapy_project && \
    mv /app/*.py /app/scrapy_project/ && \
    mv /app/spiders /app/scrapy_project/

# Define a variável de ambiente para o Scrapy encontrar o projeto
ENV PYTHONPATH="/app"

# Comando padrão para rodar o container
CMD ["scrapy", "crawl", "guardian_spider"]

# Scrapy Project - Guardian News Scraper

This project is a web scraper built with **Scrapy** to extract news articles from *The Guardian*. The scraped data is stored in a JSON file and can be uploaded to **Google BigQuery** for further analysis.

## 🚀 Features
- Extracts article **titles, links, sections, publication dates**, and more.
- Saves the output as a **JSON file**.
- Includes a script to upload the data to **Google BigQuery**.
- Dockerized for easy deployment.
- Can be scheduled to run automatically on **Cloud Run**.

## 📌 Project Structure
```
├── scrapy_project
│   ├── Dockerfile
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── items.cpython-312.pyc
│   │   ├── pipelines.cpython-312.pyc
│   │   └── settings.cpython-312.pyc
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── requirements.txt
│   ├── scrapy.cfg
│   ├── settings.py
│   ├── spiders
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   └── guardian_spider.cpython-312.pyc
│   │   └── guardian_spider.py
│   └── upload_to_bigquery.py
```

## 🔧 Installation

1. **Clone the repository**
   ```
   git clone https://github.com/your-username/scrapy_project.git
   cd scrapy_project
## Create a virtual environment (optional)


python -m venv myenv
source myenv/bin/activate   # On Windows: myenv\Scripts\activate

## Install dependencies

```  
pip install -r requirements.txt
```
## 🕷️ Running the Scraper
To start the Scrapy spider, run:
```
scrapy crawl guardian_spider
```

This will generate an output.json file containing the scraped articles.

## ☁️ Uploading Data to BigQuery
After running the scraper, you can upload the JSON file to BigQuery:

```
python upload_to_bigquery.py
```

## 🐳 Running with Docker
To run the scraper inside a Docker container:


```
docker build -t scrapy_project .
docker run scrapy_project
```
## 📌 Environment Variables
For BigQuery integration, create a .env file with:


```
GCP_PROJECT_ID=your-project-id
GCP_DATASET_ID=your-dataset
GCP_TABLE_ID=your-table
GOOGLE_APPLICATION_CREDENTIALS=path-to-your-service-account.json
```
## 📜 License
This project is open-source and available under the MIT License.



---

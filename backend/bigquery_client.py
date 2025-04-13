from google.cloud import bigquery
import os

# Load your credentials and project info from environment variables or .env
PROJECT_ID = os.getenv("GCP_PROJECT_ID")
DATASET = os.getenv("BQ_DATASET")
TABLE = os.getenv("BQ_TABLE")

client = bigquery.Client(project=PROJECT_ID)

def get_total_cost():
    query = f"""
        SELECT
            ROUND(SUM(cost), 2) as total_cost
        FROM `{PROJECT_ID}.{DATASET}.{TABLE}`
        WHERE usage_start_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
    """
    query_job = client.query(query)
    results = query_job.result()
    for row in results:
        return row.total_cost

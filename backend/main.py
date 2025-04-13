from fastapi import FastAPI
from bigquery_client import get_total_cost

app = FastAPI()

@app.get("/total-cost")
def total_cost():
    return {"total_cost": get_total_cost()}

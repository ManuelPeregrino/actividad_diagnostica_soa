from fastapi import FastAPI
from app.catalog.controller import catalog_router
from app.orders.controller import orders_router
from app.config.database import connect_db

app = FastAPI()

app.include_router(catalog_router, prefix="/catalog")
app.include_router(orders_router, prefix="/orders")

@app.on_event("startup")
def startup_db_client():
    connect_db()

@app.get("/")
def read_root():
    return {"message": "Florist API is running"}

# Swagger UI will be automatically available at /docs

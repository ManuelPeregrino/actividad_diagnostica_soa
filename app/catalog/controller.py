from fastapi import APIRouter, HTTPException
from app.catalog.service import fetch_catalog_items, create_catalog_item

catalog_router = APIRouter()

@catalog_router.get("/")
def get_catalog():
    return fetch_catalog_items()

@catalog_router.post("/")
def add_item_to_catalog(item: dict):
    result = create_catalog_item(item)
    if result:
        return {"message": "Item added successfully"}
    raise HTTPException(status_code=500, detail="Failed to add item")

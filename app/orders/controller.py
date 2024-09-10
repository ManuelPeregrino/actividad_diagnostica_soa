from fastapi import APIRouter, HTTPException
from app.orders.service import fetch_orders, add_order

orders_router = APIRouter()

@orders_router.get("/")
def get_orders():
    return fetch_orders()

@orders_router.post("/")
def create_order(order: dict):
    result = add_order(order)
    if result:
        return {"message": "Order created successfully"}
    raise HTTPException(status_code=500, detail="Failed to create order")

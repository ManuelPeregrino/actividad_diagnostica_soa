from app.orders.repository import get_orders, create_order

def fetch_orders():
    return get_orders()

def add_order(order):
    return create_order(order)

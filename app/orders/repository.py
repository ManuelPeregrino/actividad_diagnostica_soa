from app.config.database import db

def get_orders():
    return list(db['orders'].find())

def create_order(order):
    return db['orders'].insert_one(order)

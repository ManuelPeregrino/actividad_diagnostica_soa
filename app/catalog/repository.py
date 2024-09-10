from app.config.database import db

def get_catalog_items():
    return list(db['catalog'].find())

def add_catalog_item(item):
    return db['catalog'].insert_one(item)

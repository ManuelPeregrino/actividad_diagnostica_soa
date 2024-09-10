from app.catalog.repository import get_catalog_items, add_catalog_item

def fetch_catalog_items():
    return get_catalog_items()

def create_catalog_item(item):
    return add_catalog_item(item)

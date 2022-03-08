from . import CredoBase
from typing import Union


class Products(CredoBase):
    def __init__(self, public_key: str, secret_key: str):
        super().__init__(public_key=public_key, secret_key=secret_key)

    def add_physical(self, category_id: int, collection_id: int, name: str, description: str,
                     image_url1: str, image_url2: str, cost_per_item: int, regular_price: int,
                     selling_price: int, sku: str, tags: str, shipping_fee: int, tax: int, weight: int,
                     pickup: bool, continue_selling_when_out_of_stock: bool, max_no_of_purchase: int,
                     available_quantity: int, variants: list):
        pass

    def add_digital(self):
        pass

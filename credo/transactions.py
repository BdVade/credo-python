from . import CredoBase
from typing import Union


class Transactions(CredoBase):
    def __init__(self, public_key: str, secret_key: str):
        super().__init__(public_key=public_key, secret_key=secret_key)

    def all(self):
        url = f"{self.BASE_URL}/third-party/transactions"
        return self.get(url=url)

    def get_one(self, transaction_id: int):
        url = f"{self.BASE_URL}/third-party/transactions/{transaction_id}"
        return self.get(url=url)

    def refund(self, transaction_id: int, amount: int):
        url = f"{self.BASE_URL}/third-party/transactions/{transaction_id}/refund"
        body = {
            "amount": amount
        }
        return self.patch(url=url, data=body)

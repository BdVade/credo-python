from . import CredoBase
from typing import Union


class BanksCurrencies(CredoBase):
    def __init__(self, public_key: str, secret_key: str):
        super().__init__(public_key=public_key, secret_key=secret_key)

    def get_banks(self):
        url = f'{self.BASE_URL}/third-party/banks'
        return self.get(url=url)

    def get_currencies(self):
        url = f'{self.BASE_URL}/third-party/currencies'
        return self.get(url=url)

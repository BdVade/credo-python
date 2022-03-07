from . import CredoBase
from typing import Union


class SubAccount(CredoBase):

    def __init__(self, public_key: str, secret_key: str):
        super().__init__(public_key=public_key, secret_key=secret_key)

    def subaccounts(self):
        url = f"{self.BASE_URL}/third-party/subaccounts"
        return self.get(url=url)

    def create_subaccount(self, bank_id: int, currency_id: int, account_name: str, account_number: str,
                          personal_account_name: str, verified: bool, split_percentage: int):
        url = f"{self.BASE_URL}/third_party/subaccounts"
        body = {
            "bankId": bank_id,
            "currencyId": currency_id,
            "accountName": account_name,
            "accountNo": account_number,
            "personalAccountName": personal_account_name,
            "verified": verified,
            "splitPercentage": split_percentage
        }

        return self.post(url=url, data=body)

    def get_subaccount(self, subaccount_id: int):
        url = f"{self.BASE_URL}/third-party/subaccounts/{subaccount_id}"
        return self.get(url=url)

    def update_subaccount(self, subaccount_id: int, bank_id: int, currency_id: int, account_name: str,
                          account_number: str, personal_account_name: str, verified: bool, split_percentage: int):
        url = f"{self.BASE_URL}/third-party/subaccounts/{subaccount_id}"

        body = {
            "bankId": bank_id,
            "currencyId": currency_id,
            "accountName": account_name,
            "accountNo": account_number,
            "personalAccountName": personal_account_name,
            "verified": verified,
            "splitPercentage": split_percentage
        }

        self.patch(url=url, data=body)


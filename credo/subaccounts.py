from . import CredoBase
from typing import Union


class SubAccount(CredoBase):
    """
            A class used to interact with the Subaccounts module of the Credo API

            ...

            Attributes
            ----------
            public_key : str
                The users Credo Public Key
            secret_key : str
                The user's Credo secret key

            Methods
            -------
            subaccounts()
            create_subaccount()
            get_subaccount()
            update_subaccount()

    """

    def __init__(self, public_key: str, secret_key: str):
        super().__init__(public_key=public_key, secret_key=secret_key)

    def subaccounts(self):
        """

        :return:
             A Json Response from Credo
        """
        url = f"{self.BASE_URL}/third-party/subaccounts"
        return self.get(url=url)

    def create_subaccount(self, bank_id: int, currency_id: int, account_name: str, account_number: str,
                          personal_account_name: str, verified: bool, split_percentage: int):
        """

        :param bank_id:
        :param currency_id:
        :param account_name:
        :param account_number:
        :param personal_account_name:
        :param verified:
        :param split_percentage:

        :return:
            A Json Response from Credo
        """
        url = f"{self.BASE_URL}/third-party/subaccounts"
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
        """

        :param subaccount_id:

        :return:
            A Json Response from Credo
        """
        url = f"{self.BASE_URL}/third-party/subaccounts/{subaccount_id}"
        return self.get(url=url)

    def update_subaccount(self, subaccount_id: int, bank_id: int, currency_id: int, account_name: str,
                          account_number: str, personal_account_name: str, verified: bool, split_percentage: int):
        """

        :param subaccount_id:
        :param bank_id:
        :param currency_id:
        :param account_name:
        :param account_number:
        :param personal_account_name:
        :param verified:
        :param split_percentage:

        :return:
            A Json Response from Credo
        """
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

        return self.patch(url=url, data=body)


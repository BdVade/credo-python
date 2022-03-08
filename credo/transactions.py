from . import CredoBase
from typing import Union


class Transactions(CredoBase):
    """
            A class used to interact with the banks and currency module of the Credo API

            ...

            Attributes
            ----------
            public_key : str
                The users Credo Public Key
            secret_key : str
                The user's Credo secret key

            Methods
            -------
            all()
            get_one()
            refund()
    """

    def __init__(self, public_key: str, secret_key: str):
        """

        :param public_key:
        :param secret_key:
        """
        super().__init__(public_key=public_key, secret_key=secret_key)

    def all(self):
        """

        :return:
            A Json Response from Credo
        """
        url = f"{self.BASE_URL}/third-party/transactions"
        return self.get(url=url)

    def get_one(self, transaction_id: int):
        """

        :param transaction_id:

        :return:
            A Json Response from Credo
        """
        url = f"{self.BASE_URL}/third-party/transactions/{transaction_id}"
        return self.get(url=url)

    def refund(self, transaction_id: int, amount: int):
        """

        :param transaction_id:
        :param amount:

        :return:
            A Json Response from Credo
        """
        url = f"{self.BASE_URL}/third-party/transactions/{transaction_id}/refund"
        body = {
            "amount": amount
        }
        return self.patch(url=url, data=body)

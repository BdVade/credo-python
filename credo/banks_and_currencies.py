from . import CredoBase
from typing import Union


class BanksCurrencies(CredoBase):
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
        get_banks()
        get_currencies()
    """

    def __init__(self, public_key: str, secret_key: str):
        """

        :param public_key:
        :param secret_key:
        """
        super().__init__(public_key=public_key, secret_key=secret_key)

    def get_banks(self,):
        """

        :return:
         a JSON object from the credo API
        """
        url = f'{self.BASE_URL}/third-party/banks'
        return self.get(url=url)

    def get_currencies(self):
        """

        :return:
            A JSON objects from the Credo API containing a list of Currencies supported by credo
        """
        url = f'{self.BASE_URL}/third-party/currencies'
        return self.get(url=url)

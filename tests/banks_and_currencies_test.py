from credo.banks_and_currencies import BanksCurrencies
from . import PUBLIC_KEY, SECRET_KEY


class TestBankCurrencies:
    instance = BanksCurrencies(public_key=PUBLIC_KEY, secret_key=SECRET_KEY)

    # testing for the data types because these endpoints don't return a status in the json response on success
    def test_currencies(self):
        status, currencies = self.instance.get_currencies()
        assert status == 200

    def test_banks(self):
        status, banks = self.instance.get_banks()
        assert status == 200


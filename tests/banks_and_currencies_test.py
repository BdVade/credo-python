from credo.banks_and_currencies import BanksCurrencies
from . import PUBLIC_KEY, SECRET_KEY


class TestBankCurrencies:
    instance = BanksCurrencies(public_key=PUBLIC_KEY, secret_key=SECRET_KEY)

    # testing for the data types because these endpoints don't return a status in the json response on success
    def test_currencies(self):
        currencies = self.instance.get_currencies()
        print(currencies)
        assert type(currencies) == list

    def test_banks(self):
        banks = self.instance.get_banks()
        assert type(banks) == list

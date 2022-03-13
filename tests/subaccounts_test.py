from credo.subaccounts import SubAccount
from . import PUBLIC_KEY, SECRET_KEY

class TestSubAccount:
    instance = SubAccount(public_key=PUBLIC_KEY, secret_key=SECRET_KEY)

    def test_subaccount(self):
        status, subaccount = self.instance.subaccounts()
        print(subaccount)
        assert status == 200

    def test_get_subaccount(self):
        status, subaccount = self.instance.get_subaccount(55)
        print(subaccount)
        assert status == 200

    def test_create_subaccount(self):
        status, subaccount = self.instance.create_subaccount(account_name='Funds', account_number='0129322920',
                                                             personal_account_name='Funds Money', verified=True,
                                                             split_percentage=20, bank_id=6, currency_id=2)
        print(subaccount)
        assert status == 201


    def test_update_subaccount(self):
        status, subaccount = self.instance.update_subaccount(account_name='Fund', account_number='0129322920',
                                                             personal_account_name='Funds Money', verified=True,
                                                             split_percentage=20, bank_id=6, currency_id=2,
                                                             subaccount_id=59)
        assert status == 200


from credo.customers import Customers
from . import SECRET_KEY, PUBLIC_KEY


class TestCustomers:
    instance = Customers(public_key=PUBLIC_KEY, secret_key=SECRET_KEY)

    def test_add_customer(self):
        status, customer = self.instance.add(full_name='Random Name', email='rando.nam@gmail.co',
                                             phone_number='080123456789',
                                             billing_address1='random ', billing_address2='random', district='random',
                                             state='random', facebook_username=None,
                                             instagram_username=None,
                                             twitter_username=None)
        print(customer)
        assert status == 201

    # def test_update_customer(self):
    #     status, customer = self.instance.update(customer_id=143, full_name='Random Name', email='random.name@gmail.com',
    #                                             phone_number='080123456780',
    #                                             billing_address1='random ', billing_address2='rando',
    #                                             district='random',
    #                                             state='random',
    #                                             facebook_username=None,
    #                                             instagram_username=None,
    #                                             twitter_username=None)
    #     print(customer)
    #     assert status == 200

    def test_fetch_all(self):
        status, customers = self.instance.fetch_all()
        assert status == 200

    def test_fetch(self):
        status, customer = self.instance.fetch(141)
        print(customer)
        assert status == 200

    def test_fetch_transactions(self):
        status, customer = self.instance.fetch_transactions(141)
        assert status

    def test_blacklist(self):
        status, customer = self.instance.blacklist(141)
        assert status == 200

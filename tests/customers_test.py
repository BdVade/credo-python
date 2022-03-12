from credo.customers import Customers
from . import SECRET_KEY, PUBLIC_KEY


class TestCustomers:
    instance = Customers(public_key=PUBLIC_KEY, secret_key=SECRET_KEY)

    def test_add_customer(self):
        self.instance.add(full_name='Random Name', email='random.name@gmail.com', phone_number='080123456789',
                          billing_address1='random ', billing_address2='random', district='random', state='random')

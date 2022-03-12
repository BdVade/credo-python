from credo.payment import Payment
from . import SECRET_KEY, PUBLIC_KEY


class TestPayment:
    instance = Payment(public_key=PUBLIC_KEY, secret_key=SECRET_KEY)

    def test_initiate_payment(self):
        status, payment = self.instance.initiate_payment(amount=3000, currency='NGN', customer_name='Random',
                                                         customer_email='random@gmail.com',
                                                         customer_phone='23480123456789',
                                                         trans_ref='iy67f64hvc62', payment_options='CARD,BANK',
                                                         redirect_url='https://github.com/BdVade/credo-python')
        assert status == 200

    def test_verify_payment(self):
        status, payment = self.instance.verify_payment(transaction_reference='iy67f64hvc62')
        assert status == 200

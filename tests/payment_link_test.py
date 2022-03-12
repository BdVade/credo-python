from credo.payment_link import PaymentLink
from . import SECRET_KEY, PUBLIC_KEY


class TestPaymentLink:
    instance = PaymentLink(public_key=PUBLIC_KEY, secret_key=SECRET_KEY)

    def test_create_payment_link(self):
        status, payment_link = self.instance.create_link(name="Random", description="Random stuff", type_id=1,
                                                         redirect_url='https://github.com/BdVade/credo-python',
                                                         amount=3000, success_message="Thank you",
                                                         phone_number='23480123456789', currencies="NGN",
                                                         custom_fields=['Favourite food', 'Age'])
        print(payment_link)
        assert status == 201

    def test_get_link_by_slug(self):
        status, link = self.instance.get_by_slug(link_slug='credo-random-2')
        assert status == 200

    def test_get_link_by_id(self):
        status, link = self.instance.get_by_id(link_id=63)
        assert status == 200

    def test_get_link_transaction_by_id(self):
        # TODO:  Document this when it's fixed
        status, transactions = self.instance.get_link_transaction_by_id(63)
        assert status == 200

    def test_get_link_transactions(self):
        status, transactions = self.instance.get_link_transactions()
        assert status == 200

    def test_update_link(self):
        # TODO: Document After Fix
        status, link = self.instance.update_link(link_id=63, name="New Random", description="Random stuff", type_id=1,
                                                 redirect_url='https://github.com/BdVade/credo-python',
                                                 amount=3000, success_message="Thank you",
                                                 phone_number='23480123456789', currencies="NGN",
                                                 custom_fields=['Favourite food', 'Age'])
        print(link)
        assert status == 200

    def test_post_link_transaction(self):
        status, transaction = self.instance.post_link_transaction(link_slug='credo-random-1', address='Random Adress',
                                                                  amount=2000, currency='NGN', email='e@mal.com',
                                                                  first_name='Ran', last_name='Dom',
                                                                  phone_number='23480123456788', reason="The reason")
        print(transaction)
        # TODO: Come back to do this when it's resolved
        assert status == 200

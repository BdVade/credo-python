from credo.direct_charge import DirectCharge
from . import SECRET_KEY, PUBLIC_KEY


class TestDirectCharge:
    instance = DirectCharge(secret_key=SECRET_KEY, public_key=PUBLIC_KEY)

    def test_verify_card(self):
        status, verify_card = self.instance.verify_card(card_number='5204730000001003', currency='NGN',
                                                        payment_slug="vhvhvvvhvjvgjvjgv")
        print(verify_card)
        assert status == 200

    def test_three_ds_charge(self):
        # TODO: finish this up when they're done
        pass

    def test_charge_card(self):
        status, charge_card = self.instance.charge_card(amount=2000, currency='NGN', card_number='5204730000001003',
                                                        expiry_month="12", expiry_year="25", security_code="123",
                                                        trans_ref="iy67f64hvc61", customer_email='random@mil.com',
                                                        customer_phone="23480123456789", customer_name='Random',
                                                        payment_slug="0H0UOEsawNjkIxgsporr")
        assert status == 200

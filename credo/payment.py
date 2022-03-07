from . import CredoBase
from typing import Union


class Payment(CredoBase):

    def __init__(self, public_key: str, secret_key: str):
        super().__init__(public_key=public_key, secret_key=secret_key)

    def initiate_payment(self, amount: int, currency: str, redirect_url: str, trans_ref: str,
                         payment_options: str, customer_email: str, customer_name: str,
                         customer_phone: str, custom_fields: Union[dict, None] = None):
        url = f'{self.BASE_URL}/payments/initiate'

        body = {
            "amount": amount,
            "currency": currency,
            "redirectUrl": redirect_url,
            "transRef": trans_ref,
            "paymentOptions": payment_options,
            "customerEmail": customer_email,
            "customerName": customer_name,
            "customerPhoneNo": customer_phone
        }

        if custom_fields:
            custom_fields_string = ",".join(f"{k}|{v}" for k, v in custom_fields.items())
            body["customFields"] = custom_fields_string
        return self.post(url=url, data=body)

    def verify_payment(self, transaction_reference: str):
        url = f"{self.BASE_URL}/transactions/{transaction_reference}/verify"
        headers = self.secret_key_headers
        return self.get(url=url, headers=headers)

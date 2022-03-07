from . import CredoBase
from typing import Union


class PaymentLink(CredoBase):
    def __init__(self, public_key: str, secret_key: str):
        super().__init__(public_key=public_key, secret_key=secret_key)

    def create_payment_link(self, name: str, description: str, type_id: int, amount: int, redirect_url: str,
                            success_message: str, phone_number: str, currencies: str,
                            custom_fields: Union[dict, None] = None):
        url = f"{self.BASE_URL}//third-party/payment-links/links"

        body = {
            "name": name,
            "description": description,
            "typeId": type_id,
            "amount": amount,
            "redirectUrl": redirect_url,
            "successMessage": success_message,
            "phoneNo": phone_number,
            "currencies": currencies,
        }
        if custom_fields:
            custom_fields_string = ",".join(f"{k}|{v}" for k, v in custom_fields.items())
            body["customFields"] = custom_fields_string

        return self.post(url=url, data=body)

    def get_payment_link_by_id(self, link_id: int):
        url = f"{self.BASE_URL}/third-party/payment-links/links/{link_id}"
        return self.get(url)

    def update_payment_link(self, link_id: int, name: str, description: str, type_id: int, amount: int,
                            redirect_url: str,
                            success_message: str, phone_number: str, currencies: str,
                            custom_fields: Union[dict, None] = None):
        url = f"{self.BASE_URL}//third-party/payment-links/links/{link_id}"
        body = {
            "name": name,
            "description": description,
            "typeId": type_id,
            "amount": amount,
            "redirectUrl": redirect_url,
            "successMessage": success_message,
            "phoneNo": phone_number,
            "currencies": currencies,
        }
        if custom_fields:
            custom_fields_string = ",".join(f"{k}|{v}" for k, v in custom_fields.items())
            body["customFields"] = custom_fields_string

        return self.patch(url=url, data=body)

    def get_payment_link_by_slug(self, link_slug: str):
        url = f"{self.BASE_URL}/third-party/payment-links/fetch-details-by-slug/{link_slug}"
        return self.get(url)

    def post_payment_link_transaction(self, link_slug: str, currency: str, first_name: str, last_name: str,
                                      amount: int, email: str,
                                      reason: str, address: str, phone_number: str,
                                      custom_fields: Union[dict, None] = None):
        url = f"{self.BASE_URL}//third-party/payment-links/{link_slug}/transactions"
        body = {
            "currency": currency,
            "firstName": first_name,
            "lastName": last_name,
            "amount": amount,
            "email": email,
            "reason": reason,
            "address": address,
            "phoneNo": phone_number,
        }

        if custom_fields:
            custom_fields_string = "|".join(f"{k}:{v}" for k, v in custom_fields.items())
            body["customFields"] = custom_fields_string

        self.post(url=url, data=body)

    def get_payment_link_transactions(self):
        url = f"{self.BASE_URL}/third-party/payment-links/transactions"
        return self.get(url=url)

    def get_payment_link_transaction_by_id(self, transaction_id: int):
        url = f"{self.BASE_URL}/third-party/payment-links/transactions/{transaction_id}"
        return self.get(url=url)

    def get_customers(self):
        url = f"{self.BASE_URL}/third-party/customers"
        return self.get(url=url)

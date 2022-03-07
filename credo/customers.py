from . import CredoBase
from typing import Union


class Customers(CredoBase):
    def __init__(self, public_key: str, secret_key: str):
        super().__init__(public_key=public_key, secret_key=secret_key)

    def add(self, full_name: str, email: str, phone_number: str, billing_address1: str,
            billing_address2: str, district: str, state: str, twitter_username: Union[str, None] = None,
            facebook_username: Union[str, None] = None, instagram_username: Union[str, None] = None):
        url = f"{self.BASE_URL}/third-party/customers"
        body = {
            "fullName": full_name,
            "email": email,
            "phoneNo": phone_number,
            "billingAddress1": billing_address1,
            "billingsAddress2": billing_address2,
            "district": district,
            "state": state,
            "facebookUsername": facebook_username,
            "twitterUsername": twitter_username,
            "instagramUsername": instagram_username
        }

        return self.post(url=url, data=body)

    def update(self, customer_id: int, full_name: str, email: str, phone_number: str,
               billing_address1: str,
               billing_address2: str, district: str, state: str,
               twitter_username: Union[str, None] = None,
               facebook_username: Union[str, None] = None,
               instagram_username: Union[str, None] = None):
        url = f"{self.BASE_URL}/third-party/customers/{customer_id}"
        body = {
            "fullName": full_name,
            "email": email,
            "phoneNo": phone_number,
            "billingAddress1": billing_address1,
            "billingsAddress2": billing_address2,
            "district": district,
            "state": state,
            "facebookUsername": facebook_username,
            "twitterUsername": twitter_username,
            "instagramUsername": instagram_username
        }

        return self.patch(url=url, data=body)

    def fetch(self, customer_id: int):
        url = f"{self.BASE_URL}//third-party/customers/{customer_id}"
        return self.get(url=url)

    def blacklist(self, customer_id):
        url = f"{self.BASE_URL}/third-party/customers/{customer_id}/blacklist"
        return self.patch(url=url)

    def fetch_transactions(self, customer_id):
        url = f"{self.BASE_URL}/third-party/customers/{customer_id}/transactions"
        return self.get(url=url)

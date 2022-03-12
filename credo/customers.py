from . import CredoBase
from typing import Union


class Customers(CredoBase):
    """
            A class used to interact with the customers module of the Credo API

            ...

            Attributes
            ----------
            public_key : str
                The users Public Key
            secret_key : str
                The user's Credo secret key

            Methods
            -------

            fetch_all()

            add()

            update()

            fetch()

            blacklist()

            fetch_transactions()



            """

    def __init__(self, public_key: str, secret_key: str):
        super().__init__(public_key=public_key, secret_key=secret_key)

    def fetch_all(self):
        url = f"{self.BASE_URL}/third-party/customers"
        return self.get(url=url)

    def add(self, full_name: str, email: str, phone_number: str, billing_address1: str,
            billing_address2: str, district: str, state: str, twitter_username: Union[str, None] = None,
            facebook_username: Union[str, None] = None, instagram_username: Union[str, None] = None) -> dict:
        """

        :param full_name:
        :param email:
        :param phone_number:
        :param billing_address1:
        :param billing_address2:
        :param district:
        :param state:
        :param twitter_username: optional
        :param facebook_username: optional
        :param instagram_username:optional
        :return:
        """
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

    # def update(self, customer_id: int, full_name: str, email: str, phone_number: str,
    #            billing_address1: str,
    #            billing_address2: str, district: str, state: str,
    #            twitter_username: Union[str, None] = None,
    #            facebook_username: Union[str, None] = None,
    #            instagram_username: Union[str, None] = None):
    #     """
    #
    #     :param customer_id:
    #     :param full_name:
    #     :param email:
    #     :param phone_number:
    #     :param billing_address1:
    #     :param billing_address2:
    #     :param district:
    #     :param state:
    #     :param twitter_username: optional
    #     :param facebook_username: optional
    #     :param instagram_username:optional
    #     :return:
    #         A Json response from Credo
    #     """
    #     url = f"{self.BASE_URL}/third-party/customers/{customer_id}"
    #     body = {
    #         "fullName": full_name,
    #         "email": email,
    #         "phoneNo": phone_number,
    #         "billingAddress1": billing_address1,
    #         "billingsAddress2": billing_address2,
    #         "district": district,
    #         "state": state
    #     }
    #
    #     if facebook_username:
    #         body['facebookUsername'] = facebook_username
    #     if twitter_username:
    #         body['twitterUsername'] = twitter_username
    #     if instagram_username:
    #         body['instagramUsername'] = instagram_username
    #
    #     return self.patch(url=url, data=body)

    def fetch(self, customer_id: int):
        """

        :param customer_id:
        :return:
            A Json response from Credo
        """
        url = f"{self.BASE_URL}/third-party/customers/{customer_id}"
        return self.get(url=url)

    def blacklist(self, customer_id):
        """

        :param customer_id:
        :return:
            A Json response from Credo
        """
        url = f"{self.BASE_URL}/third-party/customers/{customer_id}/blacklist"
        return self.patch(url=url)

    def fetch_transactions(self, customer_id):
        """

        :param customer_id:
        :return:
            A Json response from Credo
        """
        url = f"{self.BASE_URL}/third-party/customers/{customer_id}/transactions"
        return self.get(url=url)


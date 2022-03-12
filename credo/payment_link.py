from . import CredoBase
from typing import Union


class PaymentLink(CredoBase):
    """
            A class used to interact with the Payment Links module of the Credo API

            ...

            Attributes
            ----------
            public_key : str
                The users Credo Public Key
            secret_key : str
                The user's Credo secret key

            Methods
            -------
            create_link()
            get_by_id()
            update_link()
            get_by_slug()
            post_link_transaction()
            get_link_transactions()
            get_link_transaction_by_id()


            """

    def __init__(self, public_key: str, secret_key: str):
        """

        :param public_key:
        :param secret_key:
        """
        super().__init__(public_key=public_key, secret_key=secret_key)

    def create_link(self, name: str, description: str, type_id: int, amount: int, redirect_url: str,
                    success_message: str, phone_number: str, currencies: str,
                    custom_fields: Union[list, None] = None):
        """

        :param name:
        :param description:
        :param type_id:
        :param amount:
        :param redirect_url:
        :param success_message:
        :param phone_number:
        :param currencies:
        :param custom_fields:

        :return:
            A Json Response from Credo
        """
        url = f"{self.BASE_URL}/third-party/payment-links/links"

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
            custom_fields_string = "|".join(i for i in custom_fields)
            body["customFields"] = custom_fields_string

        return self.post(url=url, data=body)

    def get_by_id(self, link_id: int):
        """

        :param link_id:

        :return:
            A Json Response from Credo
        """
        url = f"{self.BASE_URL}/third-party/payment-links/links/{link_id}"
        return self.get(url)

    def update_link(self, link_id: int, name: str, description: str, type_id: int, amount: int,
                    redirect_url: str,
                    success_message: str, phone_number: str, currencies: str,
                    custom_fields: Union[list, None] = None):
        """

        :param link_id:
        :param name:
        :param description:
        :param type_id:
        :param amount:
        :param redirect_url:
        :param success_message:
        :param phone_number:
        :param currencies:
        :param custom_fields: optional

        :return: A json Response from Credo

        """
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
            custom_fields_string = "|".join(i for i in custom_fields)
            # custom_fields_string = ",".join(f"{k}|{v}" for k, v in custom_fields.items())
            body["customFields"] = custom_fields_string

        return self.patch(url=url, data=body)

    def get_by_slug(self, link_slug: str):
        """

        :param link_slug:
        :return:
            A Json Response from Credo
        """
        url = f"{self.BASE_URL}/third-party/payment-links/fetch-details-by-slug/{link_slug}"
        return self.get(url)

    def post_link_transaction(self, link_slug: str, currency: str, first_name: str, last_name: str,
                              amount: int, email: str,
                              reason: str, address: str, phone_number: str,
                              custom_fields: Union[dict, None] = None):
        """

        :param link_slug:
        :param currency:
        :param first_name:
        :param last_name:
        :param amount:
        :param email:
        :param reason:
        :param address:
        :param phone_number:
        :param custom_fields:optional

        :return:
            A Json Response from Credo
        """
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
            print('here')
            custom_fields_string = "|".join(f"{k}:{v}" for k, v in custom_fields.items())
            body["customFields"] = custom_fields_string

        return self.post(url=url, data=body)

    def get_link_transactions(self):
        """

        :return:
            A Json response from Credo
        """
        url = f"{self.BASE_URL}/third-party/payment-links/transactions"
        return self.get(url=url)

    def get_link_transaction_by_id(self, link_id: int):
        """

        :param link_id:

        :return:
         A JSON Response from Credo


        """
        url = f"{self.BASE_URL}/third-party/payment-links/transactions/{link_id}"
        return self.get(url=url)

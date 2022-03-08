from . import CredoBase
from typing import Union


class DirectCharge(CredoBase):
    """
            A class used to interact with the direct charge and 3ds direct charge module of the Credo API

            ...

            Attributes
            ----------
            public_key : str
                The users Credo Public Key
            secret_key : str
                The user's Credo secret key

            Methods
            -------
           charge_card()

           verify_card()

           three_ds_charge()
            """

    def __init__(self, public_key: str, secret_key: str):

        """

        :param public_key:
        :param secret_key:
        """
        super().__init__(public_key=public_key, secret_key=secret_key)

    def charge_card(self, amount: int, currency: str, card_number: str, expiry_month: str,
                    expiry_year: str, security_code: str, trans_ref: str, customer_email: str,
                    customer_name: str, customer_phone: str, payment_slug: str):
        """

        :param amount:
        :param currency:
        :param card_number:
        :param expiry_month:
        :param expiry_year:
        :param security_code:
        :param trans_ref:
        :param customer_email:
        :param customer_name:
        :param customer_phone:
        :param payment_slug:

        :return:
            A Json response from Credo
        """
        url = f"{self.BASE_URL}/payments/card/third-party/pay"
        body = {
            "orderAmount": amount,
            "orderCurrency": currency,
            "cardNumber": card_number,
            "expiryMonth": expiry_month,
            "expiryYear": expiry_year,
            "securityCode": security_code,
            "transRef": trans_ref,
            "customerEmail": customer_email,
            "customerName": customer_name,
            "customerPhoneNo": customer_phone,
            "paymentSlug": payment_slug
        }

        return self.post(url=url, data=body)

    def verify_card(self, card_number: str, currency: str, payment_slug: str):
        """

        :param card_number:
        :param currency:
        :param payment_slug:

        :return:
            A Json Response from Credo
        """
        url = f"{self.BASE_URL}/payments/card/third-party/3ds-verify-card-number"
        body = {
            "cardNumber": card_number,
            "orderCurrency": currency,
            "paymentSlug": payment_slug

        }

        return self.post(url=url, data=body)

    def three_ds_charge(self, amount: int, trans_ref: str, customer_email: str, customer_name: str, currency: str,
                        customer_phone: str, payment_slug: str, order_id: str, transaction_id: str, card_number: str,
                        expiry_month: str, expiry_year: str, cvv: str, challenge_window_size: str, browser: str,
                        fail_url: str, success_url: str):

        """

        :param amount:
        :param trans_ref:
        :param customer_email:
        :param customer_name:
        :param currency:
        :param customer_phone:
        :param payment_slug:
        :param order_id:
        :param transaction_id:
        :param card_number:
        :param expiry_month:
        :param expiry_year:
        :param cvv:
        :param challenge_window_size:
        :param browser:
        :param fail_url:
        :param success_url:

        :return:
            A Json response from Credo
        """
        headers = self.secret_key_headers
        url = f"{self.BASE_URL}//payments/card/third-party/3ds-pay"
        body = {
            "orderAmount": amount,
            "transRef": trans_ref,
            "customerEmail": customer_email,
            "customerName": customer_name,
            "orderCurrency": currency,
            "customerPhoneNo": customer_phone,
            "paymentSlug": payment_slug,
            "orderId": order_id,
            "transactionId": transaction_id,
            "cardNumber": card_number,
            "expiryMonth": expiry_month,
            "expiryYear": expiry_year,
            "securityCode": cvv,
            "secureChallengeWindowSize": challenge_window_size,
            "browser": browser,
            "successTransactionUrl": success_url,
            "failedTransactionUrl": fail_url
        }

        return self.post(url=url, data=body, headers=headers)

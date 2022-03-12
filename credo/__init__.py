import json
import requests
from typing import Union


class CredoBase:

    def __init__(self, public_key: str, secret_key: str):
        self.BASE_URL = 'https://api.credocentral.com/credo-payment/v1'
        self.public_key_headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                                   'Authorization': public_key}
        self.secret_key_headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                                   'Authorization': secret_key}

    def _to_format(self, response: requests.Response):
        return response.status_code, response.json()

    def get(self, url: str, headers: dict = None, ):
        return self._to_format(requests.get(url=url, headers=headers or self.public_key_headers))

    def post(self, url: str, data: Union[dict, None] = None, headers: Union[None, dict] = None):
        return self._to_format(requests.post(url, json=data, headers=headers or self.public_key_headers))

    def patch(self, url: str, data: Union[dict, None] = None, headers: Union[None, dict] = None):
        if data:
            return self._to_format(requests.patch(url=url, json=data, headers=headers or self.public_key_headers))
        else:
            return self._to_format(requests.patch(url=url, headers=headers or self.public_key_headers))

# credo-python

A python sdk for interacting with the Credo API

----

## Usage

---

### Banks and Currencies

methods

- get_banks
- get_currencies

```python
from credo.banks_and_currencies import BanksCurrencies
banks_and_currs = BanksCurrencies(public_key='your-public-key', secret_key='your-secret-key')
# gets list of all banks
banks = banks_and_currs.get_banks()
# Sample response 
# [
#     {
#         "id": 1,
#         "code": "044",
#         "countryUuid": "nig45FDD-Jtr7-ygy7Df",
#         "name": "Access Bank"
#     },
#     {
#         "id": 18,
#         "code": "032",
#         "countryUuid": "nig45FDD-Jtr7-ygy7Df",
#         "name": "Union Bank of Nigeria"
#     }
# ]
currencies = banks_and_currs.get_currencies()
# Sample response
# [
#   {'id': 1, 'code': 'USD', 'isDefault': 0, 'name': 'United States Dollars', 'symbol': '$'}, {'id': 2, 'code': 'NGN', 'isDefault': 1, 'name': 'Nigerian Naira', 'symbol': '?'})
```

### Customers
methods

- add
- update
- fetch
- blacklist
- fetch_transactions

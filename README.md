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
status, banks = banks_and_currs.get_banks()
# print(banks)
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
status, currencies = banks_and_currs.get_currencies()
# print(currencies)
# [
#   {'id': 1, 'code': 'USD', 'isDefault': 0, 'name': 'United States Dollars', 'symbol': '$'}, {'id': 2, 'code': 'NGN', 'isDefault': 1, 'name': 'Nigerian Naira', 'symbol': '?'})
```

### Customers
methods

- add
- update
- fetch
- fetch_all
- blacklist
- fetch_transactions

```python
from credo.customers import Customers
customers  = Customers(public_key='your-public-key', secret_key='your-secret-key')
# Adds a customer
status, customer = customers.add(full_name='Random Name', email='rando.nam@gmail.com',
                                             phone_number='23480123456789',
                                             billing_address1='random ', billing_address2='random', district='random',
                                             state='random',facebook_username=None,
                                             instagram_username=None,
                                             twitter_username=None)
# fetches all customers in your integration
status, customer = customers.fetch_all()

# fetches the customer with the id passed
status, customer = customers.fetch(141)

# fetches all transactions for a customer whose ID is passed
status, customer = customers.fetch_transactions(141)

# blacklists the customer whose id is passed
status, customer = customers.blacklist(141)


```

### Direct Charge

methods

- charge_card
- verify_card
- three_ds_charge

```python
from credo.direct_charge import DirectCharge

direct_charge = DirectCharge(public_key='your-public-key', secret_key='your-secret-key')

# Charge a card without 3DS verification
status, charge_card = direct_charge.charge_card(amount=2000, currency='NGN', card_number='5204730000001003',
                                                        expiry_month="12", expiry_year="25", security_code="123",
                                                        trans_ref="iy67f64hvc61", customer_email='random@mil.com',
                                                        customer_phone="23480123456789", customer_name='Random',
                                                        payment_slug="0H0UOEsawNjkIxgsporr")
```

### Standard Payment

methods

- initiate_payment
- verify_payment

```python
from credo.payment import Payment

payment = Payment(public_key='your-public-key', secret_key='your-secret-key')

# to initiate a payment
status, new_payment = payment.initiate_payment(amount=3000, currency='NGN', customer_name='Random',
                                                         customer_email='random@gmail.com',
                                                         customer_phone='23480123456789',
                                                         trans_ref='iy67f64hvc62', payment_options='CARD,BANK',
                                                         redirect_url='https://github.com/BdVade/credo-python')
# to verify a payment

status, verify_payment = payment.verify_payment(transaction_reference='iy67f64hvc62')
```

### Payment Link
methods


### Transactions

```python
from credo.transactions import Transactions


transactions = Transactions(public_key='your-public-key', secret_key='your-secret-key')

# To get a list of all your transactions
status, all_transactions = transactions.all()

# To get a transaction by it's id
status, transaction = transactions.get_one(transaction_id=5)

# refund a transaction by its id

status, refund = transactions.refund(transaction_id=5)
```
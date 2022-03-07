import requests
import json

body = {
    "name": "Payment for Jumbo Chops",
    "description": "3 chickens, 1 bag of chips, 2 plantains.",
    "typeId": 1,
    "amount": 4000,
    "redirectUrl": "http://myapp.com/orders/eyu67234ff/paymentComplete",
    "successMessage": "Thanks for your purchase, you beautiful human!",
    "currencies": "NGN",

}
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'pk_demo-fKq5DnKgI3ISchDxVEySOS4Z9X4hck.D1gJjoVG5p-d'
}

response = requests.post(
    'https://api.credocentral.com/credo-payment/v1/third-party/payment-links/links/',
    headers=headers,
    json=body
)

print(response.json())

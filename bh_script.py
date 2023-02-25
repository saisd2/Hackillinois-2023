import requests
import json
from random import randrange

organization_id = "24A8F9AC4C974D6DB81FBC8B66822011"
row_limit = 100  # contact us before increasing this limit, you can run this script multiple times 
endpoint = "https://api.bluehillpayments.io"


def create_customer(dataframe):
    url = "https://api.bluehillpayments.io/customers/v2/create"

    payload = json.dumps(
        {
            "organizationId": organization_id,
            "firstName": dataframe["first_name"],
            "lastName": dataframe["last_name"],
            "street": dataframe["address"],
            "town": dataframe["town"],
            "zipCode": dataframe["zip"],
            "state": dataframe["state"],
            "email": dataframe["email"],
            "phoneNumber": dataframe["phone"],
            "company": dataframe["company"],
        }
    )
    headers = {"Content-Type": "application/json"}
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


def create_charge(customer_id, amount, payment_method_id):
    url = "https://api.bluehillpayments.io/transactions/v2/create2"

    payload = json.dumps(
        {
            "amount": amount,
            "customerId": customer_id,
            "paymentMethodId": payment_method_id,
            "organizationId": organization_id,
            "isLive": False,
        }
    )
    headers = {"Content-Type": "application/json"}
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


def create_payment_method(card_data):
    url = "https://api.bluehillpayments.io/payment-method/create"
    payload = json.dumps(card_data)
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)
    return response.json()


if __name__ == "__main__":
    # create customer
    customer = {
        "first_name": "John",
        "last_name": "Smith",
        "address": "123 Main St",
        "town": "Anytown",
        "zip": "12345",
        "state": "NY",
        "email": "jsmith@email.com",
        "phone": "1234567890",
        "company": "Acme Inc.",
    }
    customer = create_customer(customer)
    customer_id = customer["data"]["id"]

    # create payment method
    card_data = {
        "customerId": customer_id,
        "cardNumber": "4242424242424242",
        "expirationMonth": "08",
        "expirationYear": "2026",
        "cvv": "264",
        "type": "card",
        "isLive": False,
    }
    payment_method = create_payment_method(card_data)
    payment_method_id = payment_method["id"]

    # create charges
    for _ in range(20):
        create_charge(customer_id, randrange(1, 100), payment_method_id)
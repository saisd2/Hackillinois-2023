import requests

# define the endpoint URL
url = 'http://127.0.0.1:5000/check_suspicious'

# define the transaction data
transaction = {
    'company': 'Incorporated Academy',
    'amount': 1000.0,
    'span': "yolo"
}

# make a POST request to the API
response = requests.post(url, json=transaction)

# get the response data as a JSON object
result = response.json()

# check if the transaction is suspicious
if result['suspicious']:
    print('Transaction is suspicious')
else:
    print('Transaction is not suspicious')
import pandas as pd
import requests

# Read the list of IDs from a txt file
with open('/Users/dongyu/Desktop/College/HACKATHON/transaction_id.txt', 'r') as file:
    ids = [line.strip() for line in file]

# Make a GET request for each ID and store the response in a list
responses = []
for id in ids:
    #id = "EF1C95D01793405CB635446D6FBD09AC"
    url = "https://api.bluehillpayments.io/transactions/v2/get/" + id
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    responses.append(response.json())

# Combine the responses into a single dataframe

# create a DataFrame from the data
# df = pd.DataFrame(responses[0]['data']['customer'])
# print([responses[0]['data']['customer']])

data_d = {}
data_d = responses[0]['data']['customer']
data_d.update(responses[0]['data']['transaction'])

# create the DataFrame
df = pd.DataFrame([data_d])

for i in range(len(responses)):
    data_d = {}
    data_d = responses[i]['data']['customer']
    data_d.update(responses[i]['data']['transaction'])
    df.loc[len(df.index)] = data_d
# df = pd.concat([pd.DataFrame(r) for r in responses], ignore_index=True)
print(df.columns)

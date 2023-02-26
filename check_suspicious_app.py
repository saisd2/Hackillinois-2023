from flask import Flask, request
import pandas as pd
import requests
from flask_cors import CORS, cross_origin
app = Flask(__name__)

# Read the list of IDs from a txt file
with open('transaction_id.txt', 'r') as file:
    ids = [line.strip() for line in file]

# Make a GET request for each ID and store the response in a list
def score(company):
    out = []
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
    # get the max transaction
    df_success = pd.DataFrame(responses)
    df['status'] = df_success['status']
    gb_max = df.groupby('company')['amount'].agg('max')
    out.append(gb_max[company])
    #get the min transaction
    gb_min = df.groupby('company')['amount'].agg('min')
    out.append(gb_min[company])
    gb_total_sum = df.groupby('company')['amount'].agg('sum')
    num_passed = ((df['processedGateway'] == 2) & (df['company'] == company)).sum()
    # print(num_passed)
    passed_amount = df[(df['processedGateway'] == 2) & (df['company'] == company)]['amount'].sum()
    # print(passed_amount)
    sorted_amount = df['amount'].sort_values()
    score = (num_passed *  passed_amount)/(gb_total_sum[company] * (df['company'] == company).sum())
    out.append(score)
    # print(gb_total_sum[company])
    # print((df['company'] == company).sum())
    # print(score)
    # print(df[df['company'] == company])
    first_quartile = df[df['company'] == company]['amount'].quantile(0.25)
    median = df[df['company'] == company]['amount'].quantile(0.5)
    third_quartile = df[df['company'] == company]['amount'].quantile(0.75)
    lower_bound = median - (third_quartile-first_quartile) * 1.5
    upper_bound = median + (third_quartile-first_quartile) * 1.5
    out.append(lower_bound)
    # print(lower_bound)
    out.append(upper_bound)
    return out

print(score("Incorporated Academy"))
# define the API endpoint
@app.route('/check_suspicious', methods=['POST'])
@cross_origin()
def check_suspicious():
    # get the transaction data from the request body
    transaction_id = request.get_json()
    print(transaction_id)

    # create a DataFrame from the transaction data
    df = pd.DataFrame([transaction_id])

    # calculate the quartiles and bounds
    scores = score(transaction_id['company'])
    lower_bound = scores[-2]
    upper_bound = scores[-1]

    # determine if the transaction is suspicious
    print(transaction_id['amount'])
    print(upper_bound)
    suspicious = (float(transaction_id['amount']) < float(lower_bound)) | (float(transaction_id['amount']) > float(upper_bound))

    # return the result as a JSON response
    return {'suspicious': bool(suspicious), 'score': scores[2]*100}

if __name__ == '__main__':
    app.run(debug=True)
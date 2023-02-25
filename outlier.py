import requests
import json
import numpy as np
from scipy.stats import zscore

# replace these values with your own Bluehill API credentials
BLUEHILL_API_KEY = "8991B8544560496B8CA9AA1D5FE6FE4E"
BLUEHILL_API_SECRET = "your_api_secret"

# retrieve transactions from Bluehill API
headers = {"Authorization": f"Bearer {BLUEHILL_API_KEY}:{BLUEHILL_API_SECRET}"}
url = "https://api.bluehill.com/v1/transactions"
response = requests.get(url, headers=headers)
transactions = json.loads(response.text)

# calculate z-scores for transaction amounts and times
amounts = [transaction["amount"] for transaction in transactions]
amount_zscores = zscore(amounts)
times = [transaction["timestamp"] for transaction in transactions]
time_zscores = zscore(times)

# identify outliers based on z-score threshold (e.g. 3)
outlier_threshold = 3
outliers = np.where(np.abs(amount_zscores) > outlier_threshold)[0].tolist() + \
           np.where(np.abs(time_zscores) > outlier_threshold)[0].tolist()

# print indices of identified outliers
print(f"Outliers: {outliers}")

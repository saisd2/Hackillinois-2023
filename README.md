# Hackillinois-2023
Hackillinois 2023 submission

### Payment Security Tool
This tool is designed to help businesses detect and prevent fraudulent transactions by analyzing transaction amounts and times.

#### How it Works
The Payment Security Tool uses the Bluehill API to analyze transaction data. It compares the transaction amount and time with other transactions made by the same user and other users. If the transaction amount or time is significantly different from other transactions, it will flag the transaction as potentially fraudulent. You can check transactions using the user friendly dashboard website to see if a transaction will be flagged as potentially fraudulent.

#### Getting Started
To use this tool, you will need to sign up for a Bluehill API account and obtain an API key. Once you have your API key, you can clone this repository and configure the config.py file with your API key and other settings. Ensure that you have React, Python, Flask, and the other imports installed before running.

#### Usage
The app will be primarily accessed through the dashboard webapp, use customer information and place a transaction to see if it may be flagged as fraudulent, as well as to see the customer's risk score. Results will show up as alerts in the website, and may take a second while the request is processing. Both the python backend and react frontend will need to be running locally to start:

```
python check_suspicious_app.py
```
```
cd dashboard
npm start
```

License
This tool is licensed under the MIT License. See the LICENSE file for more information.

# Hackillinois-2023
Hackillinois 2023 submission
Payment Security Tool
This tool is designed to help businesses detect and prevent fraudulent transactions by analyzing transaction amounts and times.

How it Works
The Payment Security Tool uses the Bluehill API to analyze transaction data. It compares the transaction amount and time with other transactions made by the same user and other users. If the transaction amount or time is significantly different from other transactions, it will flag the transaction as potentially fraudulent.

Getting Started
To use this tool, you will need to sign up for a Bluehill API account and obtain an API key. Once you have your API key, you can clone this repository and configure the config.py file with your API key and other settings.

Usage
To use the Payment Security Tool, run the main.py script with the transaction data as input. The transaction data should be in CSV format with columns for transaction ID, user ID, transaction amount, and transaction time.

bash
Copy code
python main.py transactions.csv
The tool will output a new CSV file with columns for transaction ID, user ID, transaction amount, transaction time, and a flag indicating whether the transaction is potentially fraudulent.

License
This tool is licensed under the MIT License. See the LICENSE file for more information.

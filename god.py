import requests
import pandas as pd
import sqlite3
from config import API_KEY

symbol = []
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
response = requests.get(url)
data = response.json()
daily = data["Time Series (Daily)"]
df = pd.DataFrame(daily).T
df = df.apply(pd.to_numeric)
conn = sqlite3.connect('stocks.db')
df.to_sql(f'{symbol}_daily', conn, if_exists='replace')
check = pd.read_sql(f'SELECT * FROM {symbol}_daily', conn)
print(check)

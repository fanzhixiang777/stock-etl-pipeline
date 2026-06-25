import requests
import pandas as pd
import sqlite3
from config import API_KEY


url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={API_KEY}"
response = requests.get(url)
data = response.json()
daily = data["Time Series (Daily)"]
df = pd.DataFrame(daily).T
df = df.apply(pd.to_numeric)
conn = sqlite3.connect('stocks.db')
df.to_sql('ibm_daily', conn, if_exists='replace')
check = pd.read_sql('SELECT * FROM ibm_daily', conn)
print(check)
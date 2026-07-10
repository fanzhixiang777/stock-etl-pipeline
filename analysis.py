import pandas as pd
import sqlite3

sybmol = []
conn = sqlite3.connect('stocks.db')
check = pd.read_sql(f'SELECT * FROM {sybmol}_daily', conn)
check = check.rename(columns={'index': 'date', '4. close': 'close'})
check = check.sort_values('date')
check['MA5'] = check['close'].rolling(5).mean()
check['prev_close'] = check['close'].shift(1)
check['return'] = (check['close'] - check['prev_close']) / check['prev_close']
volatility = check['return'].std()
print(check['MA5'])
print(check['return'])
print(volatility)

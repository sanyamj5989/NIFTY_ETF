import yfinance as yf
import pandas as pd
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')
data = yf.download('NIFTYBEES.BO', start='2025-01-01', end=today)
df = pd.DataFrame(data)
df.columns = df.columns.get_level_values(0)

# Calculate previous day's close
df['Prev_Close'] = df['Close'].shift(1)

# Calculate metrics
df['Open_Gap_%'] = ((df['Open'] - df['Prev_Close']) / df['Prev_Close']) * 100
df['Close_%'] = ((df['Close'] - df['Open']) / df['Open']) * 100

# Combine signals
df['Buy_Signal_Open'] = df['Open_Gap_%'] <= -1
df['Buy_Signal_Close'] = df['Close_%'] <= -1

df['Buy_Signal'] = df['Buy_Signal_Open'] | df['Buy_Signal_Close']

# Set Buy Price
df['Buy_Price'] = None
df.loc[df['Buy_Signal_Open'], 'Buy_Price'] = df['Open']
df.loc[df['Buy_Signal_Close'], 'Buy_Price'] = df['Close']

# Filter buy days
buy_days = df[df['Buy_Signal'] == True]

# Average buy price
average_buy_price = buy_days['Buy_Price'].mean()

# Latest available close price
latest_close_price = df['Close'].iloc[-1]

# Calculate return percentage
return_percentage = ((latest_close_price - average_buy_price) / average_buy_price) * 100

# Output
print("Buy Signal Days (Gap-down open ≥ 1% OR day's close ≥ 1% down):")
print(buy_days[['Prev_Close', 'Open', 'Low', 'Open_Gap_%', 'Close_%', 'Buy_Price']])
print(f"\nTotal Buy Days: {buy_days.shape[0]}")
print(f"Average Buy Price on Buy Signal Days: ₹{average_buy_price:.2f}")
print(f"Latest Closing Price: ₹{latest_close_price:.2f}")
print(f"Return if held until now: {return_percentage:.2f}%")


# NIFTY_ETF
Strategy backtest for identifying intraday buying opportunities based on gap-down and intraday dip patterns using NIFTYBEES data.
# Intraday Gap-Down Buy Strategy on NIFTYBEES

This project analyzes and backtests an intraday trading strategy using historical NIFTYBEES data. The strategy identifies two types of buying opportunities:

1. Gap-Down Buy at Open: If the market opens 1% lower than the previous day’s close, a buy signal is generated at the opening price.
2. Intraday Dip Buy at Close: If the market closes 1% below its opening price, a second buy signal is generated at the closing price.

If both conditions occur on the same day, two buys are recorded.

## 📊 Data & Tools
- Ticker: NIFTYBEES (NSE)
- Data Source: [Yahoo Finance](https://finance.yahoo.com/quote/NIFTYBEES.NS/)
- Library: `yfinance`, `pandas`

## 🚀 What This Project Does
- Downloads historical price data using `yfinance`
- Detects and logs buy signals based on the strategy logic
- Computes total number of buy signals and average returns

## 📈 Example Output
- Data Selected: From 1st Jan 2025 to latest date (4th July)
- Total Buy Days: 13
- Average Buy Price on Buy Signal Days: ₹264.24
- Latest Closing Price: ₹286.09
- Return if held until now: 8.27%




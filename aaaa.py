import yfinance as yf
import pandas as pd
from datetime import datetime

def calculate_rsi(data, period=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)

    avg_gain = gain.rolling(window=period, min_periods=1).mean()
    avg_loss = loss.rolling(window=period, min_periods=1).mean()

    # Use Wilder's smoothing method
    gain_smooth = avg_gain.ewm(alpha=1/period, adjust=False).mean()
    loss_smooth = avg_loss.ewm(alpha=1/period, adjust=False).mean()

    rs = gain_smooth / loss_smooth
    rsi = 100 - (100 / (1 + rs))
    return rsi

def check_rsi_below_30(stock_list):
    results = []
    for stock in stock_list:
        data = yf.download(stock, period="6mo")  # Fetch 6 months of data
        if not data.empty:
            data['RSI'] = calculate_rsi(data)
            if data['RSI'].iloc[-1] < 30:  # Check the most recent RSI value
                results.append(stock)
    return results

# List of stocks to check
stock_list = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]

# Check RSI
stocks_below_30 = check_rsi_below_30(stock_list)

print("Stocks with RSI below 30 today:")
for stock in stocks_below_30:
    print(stock)

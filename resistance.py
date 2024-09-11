import yfinance as yf
import datetime
import csv

# Function to get stocks that are near resistance on a specific date
def find_resistance_stocks(stock_symbols, specific_date):
    resistance_stocks = []
    specific_date = datetime.datetime.strptime(specific_date, '%Y-%m-%d')
    start_date = specific_date - datetime.timedelta(days=120)  # approximately 4 months

    for symbol in stock_symbols:
        # Get historical market data up to the specific date
        data = yf.download(symbol, start=start_date, end=specific_date + datetime.timedelta(days=1))

        if not data.empty:
            # Get the lowest price in the last 4 months
            lowest_price = data['Low'].min()

            # Get the closing price on the specific date
            if specific_date.strftime('%Y-%m-%d') in data.index:
                specific_close_price = data.loc[specific_date.strftime('%Y-%m-%d'), 'Low']

                # Calculate the ratio
                ratio = lowest_price / specific_close_price
                print(ratio,lowest_price,specific_close_price)
                # Check if the ratio is within the specified range
                if 0.995 <= ratio <= 1.005:
                    resistance_stocks.append(symbol)

    return resistance_stocks

# Example usage

# Read stock symbols from the CSV file
with open(r"Untitled spreadsheet - Sheet1.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header if present
    stock_symbols = [row[1] for row in reader]
specific_date = '2024-08-13'  # Replace with your specific date in 'YYYY-MM-DD' format
resistance_stocks = find_resistance_stocks(stock_symbols, specific_date)
print("Stocks near resistance on", specific_date, ":", resistance_stocks)

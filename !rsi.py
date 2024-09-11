import yfinance as yf
import pandas as pd
from datetime import datetime
import csv

def calculate_rsi(data, period=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)

    avg_gain = gain.rolling(window=period, min_periods=1).mean()
    avg_loss = loss.rolling(window=period, min_periods=1).mean()

    gain_smooth = avg_gain.ewm(alpha=1/period, adjust=False).mean()
    loss_smooth = avg_loss.ewm(alpha=1/period, adjust=False).mean()

    rs = gain_smooth / loss_smooth
    rsi = 100 - (100 / (1 + rs))
    return rsi

def check_rsi_on_date(stock_list, check_date):
    results = []
    for stock in stock_list:
        data = yf.download(stock, period="6mo") 
        if not data.empty:
            data['RSI'] = calculate_rsi(data)
            if check_date in data.index:
                close_price = data['Close'].loc[check_date]
                rsi_value = data['RSI'].loc[check_date]
                if rsi_value < 30 and close_price < 25:  
                    results.append((stock, rsi_value))  # Append the stock symbol and RSI value
    return results

# Load symbols from CSV
with open(r"Untitled spreadsheet - Sheet1.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)  
symbols = [row[1] for row in rows]

# Specify the date you want to check (format: YYYY-MM-DD)
specific_date = '2024-08-12'

# Convert the string to a datetime object for comparison
check_date = datetime.strptime(specific_date, '%Y-%m-%d')

# Check RSI for the specific date
stocks_below_30 = check_rsi_on_date(symbols, check_date)

# Sort the stocks by RSI value from lowest to highest
stocks_below_30_sorted = sorted(stocks_below_30, key=lambda x: x[1])

# Extract just the stock symbols into a list
sorted_stock_names = [stock for stock, rsi in stocks_below_30_sorted]

# Print the list of stock names
print(sorted_stock_names)
#['CNTM', 'CDT', 'AIEV', 'HPH', 'GIPR', 'HLVX', 'CONN', 'GRI', 'TANH', 'VWE', 'NCI', 'XTIA', 'MULN', 'FAAS', 'VBIV', 'TGL', 'JAGX', 'SYTA', 'XPON', 'CNSP', 'CRIS', 'FRGT', 'MBLY', 'VCIG', 'APTO', 'GRAB', 'ENTO', 'TNXP', 'TCRT', 'HYZN', 'BZ', 'CRSR', 'NMHI', 'SPI', 'SEEL', 'AMLI', 'CETX', 'MFI', 'INTC', 'XOS', 'MICS', 'MOBX', 'DGLY', 'SGD', 'GUTS', 'TPST', 'LGMK', 'SPRC', 'VLCN', 'SLGL', 'CLEU', 'RNAZ', 'VERB', 'NXTT', 'ARBB', 'IFBD', 'BGFV', 'HEPA', 'ATEC', 'ELAB', 'SEED', 'LAES', 'PHIO', 'BIMI', 'GPAK', 'MAXN', 'GWAV', 'IMAB', 'ELBM', 'AVTE', 'IART', 'GENE', 'GRYP', 'SILC', 'BHAT', 'GTI', 'TCPC', 'BMRA', 'RENB', 'CWD', 'PET', 'AYTU', 'SGML', 'FTFT', 'ONVO', 'NWTN', 'HIMX', 'ALXO', 'AVDX', 'HSDT', 'JWEL', 'SPPL', 'SGMA', 'AQMS', 'SONN', 'DTSS', 'MLCO', 'SPEC', 'PRPH', 'MNY', 'ALLR', 'AGEN', 'MFIC', 'LYFT', 'SXTP', 'ICCT', 'AENT', 'OCSL', 'VRAR', 'MNDR', 'MMAT', 'SOND', 'UK', 'BJDX', 'TURN', 'APDN', 'SPWR', 'SGBX', 'REVB', 'RANI', 'MXL', 'IBRX', 'ALCE', 'OPTX', 'YGMZ']
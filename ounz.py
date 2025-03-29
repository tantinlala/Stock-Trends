import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the ticker symbol for the OUNZ ETF
ticker_gold = "OUNZ"
ticker_sp500 = "VOO"

# Define the downturn period for the U.S.–China Trade War
trade_war_start, trade_war_end = pd.to_datetime("2018-03-01"), pd.to_datetime("2020-01-15")

# Define the time period to fetch data (e.g., from 2014 to the present)
start_date = trade_war_start
end_date = trade_war_end

# Download historical data for the OUNZ ETF
data = yf.download(ticker_gold, start=start_date, end=end_date)

# Make sure the index is in datetime format
data.index = pd.to_datetime(data.index)

# Download historical data for the S&P 500 ETF
data_sp500 = yf.download(ticker_sp500, start=start_date, end=end_date)

# Make sure the index is in datetime format
data_sp500.index = pd.to_datetime(data_sp500.index)

# Normalize the data for OUNZ
data['Normalized Close'] = data['Close'] / data['Close'].iloc[0]

# Normalize the data for S&P 500
data_sp500['Normalized Close'] = data_sp500['Close'] / data_sp500['Close'].iloc[0]

# Create the base time series plot of the normalized closing price
plt.figure(figsize=(12,6))
plt.plot(data.index, data['Normalized Close'], label='OUNZ Normalized Price', color='black')
plt.plot(data_sp500.index, data_sp500['Normalized Close'], label='VOO Normalized Price', color='blue')

# To avoid duplicate labels in the legend, we combine handles and labels uniquely.
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), loc='upper left')

# Title and axis labels
plt.title("OUNZ ETF Price Trend with Highlighted Economic Periods")
plt.xlabel("Date")
plt.ylabel("Normalized Price")
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()

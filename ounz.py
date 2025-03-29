import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Define the ticker symbol for the OUNZ ETF
ticker_gold = "OUNZ"
ticker_sp500 = "VOO"

# Define the time period to fetch data (e.g., from 2014 to the present)
start_date = "2014-01-01"
end_date = datetime.datetime.today().strftime('%Y-%m-%d')

# Download historical data for the OUNZ ETF
data = yf.download(ticker_gold, start=start_date, end=end_date)

# Make sure the index is in datetime format
data.index = pd.to_datetime(data.index)

# Download historical data for the S&P 500 ETF
data_sp500 = yf.download(ticker_sp500, start=start_date, end=end_date)

# Make sure the index is in datetime format
data_sp500.index = pd.to_datetime(data_sp500.index)

# Create the base time series plot of the closing price
plt.figure(figsize=(12,6))
plt.plot(data.index, data['Close'], label='OUNZ Close Price', color='black')

# Add the S&P 500 closing price to the plot
plt.plot(data_sp500.index, data_sp500['Close'], label='VOO Close Price', color='blue')

# Define economic periods to highlight (dates are illustrative)
# Downturn periods (shaded in red)
downturn_periods = {
    "U.S.–China Trade War": ("2018-03-01", "2020-01-15")
}

# Add shaded areas for downturn periods
for label, (start, end) in downturn_periods.items():
    plt.axvspan(pd.to_datetime(start), pd.to_datetime(end), color='red', alpha=0.3, label=label)

# To avoid duplicate labels in the legend, we combine handles and labels uniquely.
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), loc='upper left')

# Title and axis labels
plt.title("OUNZ ETF Price Trend with Highlighted Economic Periods")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()

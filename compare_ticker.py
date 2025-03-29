import argparse
import datetime
import pandas as pd
from data_downloader import download_data
from data_plotter import plot_data

# Define the ticker symbols and time period
def main():
    parser = argparse.ArgumentParser(description="Compare a stock ticker to the S&P 500.")
    parser.add_argument("ticker", type=str, help="The stock ticker symbol to compare.")
    parser.add_argument("start", type=str, help="The start date for the data (YYYY-MM-DD).")
    parser.add_argument("end", type=str, nargs="?", default=datetime.date.today().strftime("%Y-%m-%d"), help="The end date for the data (YYYY-MM-DD). Defaults to today's date.")

    args = parser.parse_args()

    ticker = args.ticker
    start_date = pd.to_datetime(args.start)
    end_date = pd.to_datetime(args.end)

    ticker_sp500 = "VOO"

    # Download data for the given ticker and S&P 500
    data = download_data(ticker, start_date, end_date)
    data_sp500 = download_data(ticker_sp500, start_date, end_date)

    # Plot the data
    plot_data(data, data_sp500, f"{ticker} vs S&P 500 Price Trend", ticker)

if __name__ == "__main__":
    main()

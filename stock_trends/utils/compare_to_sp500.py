# compare_to_sp500.py
import pandas as pd
from stock_trends.utils.data_downloader import download_data
from stock_trends.utils.data_plotter import plot_data

def compare_to_sp500(ticker, start_date, end_date):
    ticker_sp500 = "VOO"

    # Download data for the given ticker and S&P 500
    data = download_data(ticker, start_date, end_date)
    data_sp500 = download_data(ticker_sp500, start_date, end_date)

    # Plot the data
    plot_data(data, data_sp500, f"{ticker} vs S&P 500 Price Trend", ticker, ticker_sp500)
import yfinance as yf
import pandas as pd

def download_data(ticker, start_date, end_date):
    """
    Downloads and normalizes historical stock data from Yahoo Finance.

    Parameters:
        ticker (str): The stock ticker symbol.
        start_date (datetime): The start date for the data.
        end_date (datetime): The end date for the data.

    Returns:
        pd.DataFrame: A DataFrame containing the normalized historical stock data.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    data['Close'] = data['Close'] / data['Close'].iloc[0]  # Normalize the 'Close' prices
    return data
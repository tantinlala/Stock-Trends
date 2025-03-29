# compare_to_sp500.py
import pandas as pd
from stock_trends.utils.data_downloader import download_data
from stock_trends.utils.data_plotter import plot_data

def compare_to_sp500(tickers, start_date, end_date, title=None):
    """
    Compare multiple stock tickers to the S&P 500 index.
    
    Parameters:
        tickers (list or str): Either a single ticker symbol or a list of ticker symbols
        start_date: The start date for data collection
        end_date: The end date for data collection
        title (str, optional): Custom title for the plot
    """
    ticker_sp500 = "VOO"
    
    # Convert single ticker to a list for consistent processing
    if isinstance(tickers, str):
        tickers = [tickers]
    
    # Download data for all tickers
    data_list = []
    for ticker in tickers:
        data = download_data(ticker, start_date, end_date)
        data_list.append(data)
    
    # Add S&P 500 to the data and tickers lists
    sp500_data = download_data(ticker_sp500, start_date, end_date)
    data_list.append(sp500_data)
    tickers_with_sp500 = tickers + [ticker_sp500]
    
    # Create plot title if not provided
    if title is None:
        if len(tickers) == 1:
            title = f"{tickers[0]} vs S&P 500 Price Trend"
        else:
            tickers_str = ", ".join(tickers)
            title = f"{tickers_str} vs S&P 500 Price Trend"
    
    # Plot the data
    plot_data(data_list, title, tickers_with_sp500)
import matplotlib.pyplot as plt
import numpy as np

def plot_data(data_list, title, ticker_list):
    """
    Plots the stock data for multiple tickers with the S&P 500 as reference.

    Parameters:
        data_list (list): List of pd.DataFrames containing stock data for each ticker.
        title (str): The title of the plot.
        ticker_list (list): List of ticker symbols corresponding to the data.
    """
    plt.figure(figsize=(12, 6))
    
    # Generate a color cycle for the different tickers
    colors = plt.cm.tab10(np.linspace(0, 1, len(ticker_list)))
    
    # Plot each ticker's data
    for i, (data, ticker) in enumerate(zip(data_list, ticker_list)):
        plt.plot(data['Close'], label=ticker, color=colors[i])
    
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()
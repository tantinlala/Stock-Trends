import matplotlib.pyplot as plt

def plot_data(data_first, data_second, title, ticker_first, ticker_second):
    """
    Plots the stock data with highlighted economic periods.

    Parameters:
        data (pd.DataFrame): The stock data for the main ticker.
        data_sp500 (pd.DataFrame): The stock data for the S&P 500.
        title (str): The title of the plot.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data_first['Close'], label=ticker_first)
    plt.plot(data_second['Close'], label=ticker_second, alpha=0.7)
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()
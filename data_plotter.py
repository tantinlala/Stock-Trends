import matplotlib.pyplot as plt

def plot_data(data, data_sp500, title, ticker):
    """
    Plots the stock data with highlighted economic periods.

    Parameters:
        data (pd.DataFrame): The stock data for the main ticker.
        data_sp500 (pd.DataFrame): The stock data for the S&P 500.
        title (str): The title of the plot.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label=ticker)
    plt.plot(data_sp500['Close'], label='S&P 500', alpha=0.7)
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()
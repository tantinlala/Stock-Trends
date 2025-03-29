import argparse
import datetime
import pandas as pd
from stock_trends.utils.compare_to_sp500 import compare_to_sp500

def main():
    parser = argparse.ArgumentParser(description="Compare a stock ticker to the S&P 500.")
    parser.add_argument("ticker", type=str, help="The stock ticker symbol to compare.")
    parser.add_argument("start", type=str, help="The start date for the data (YYYY-MM-DD).")
    parser.add_argument("end", type=str, nargs="?", default=datetime.date.today().strftime("%Y-%m-%d"), help="The end date for the data (YYYY-MM-DD). Defaults to today's date.")

    args = parser.parse_args()

    ticker = args.ticker
    start_date = pd.to_datetime(args.start)
    end_date = pd.to_datetime(args.end)

    compare_to_sp500(ticker, start_date, end_date)

if __name__ == "__main__":
    main()

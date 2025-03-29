import argparse
import datetime
import pandas as pd
from stock_trends.utils.compare_to_sp500 import compare_to_sp500

def main():
    parser = argparse.ArgumentParser(description="Compare stock tickers to the S&P 500.")
    parser.add_argument("tickers", type=str, nargs='+', help="One or more stock ticker symbols to compare.")
    parser.add_argument("start", type=str, help="The start date for the data (YYYY-MM-DD).")
    parser.add_argument("end", type=str, nargs="?", default=datetime.date.today().strftime("%Y-%m-%d"), help="The end date for the data (YYYY-MM-DD). Defaults to today's date.")
    parser.add_argument("--description", "-d", type=str, help="Optional description of the time period to add to the plot title.")

    args = parser.parse_args()

    tickers = args.tickers
    start_date = pd.to_datetime(args.start)
    end_date = pd.to_datetime(args.end)
    
    # Create custom title if description is provided
    if args.description:
        tickers_str = ", ".join(tickers)
        title = f"{tickers_str} vs S&P 500: {args.description}"
    else:
        title = None

    compare_to_sp500(tickers, start_date, end_date, title)

if __name__ == "__main__":
    main()

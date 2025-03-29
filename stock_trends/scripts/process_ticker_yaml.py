import yaml
import pandas as pd
from stock_trends.utils.compare_to_sp500 import compare_to_sp500
import argparse

def main():
    parser = argparse.ArgumentParser(description="Process a YAML file of tickers and dates.")
    parser.add_argument("yaml_file", type=str, help="Path to the YAML file containing tickers and dates.")
    args = parser.parse_args()

    yaml_file = args.yaml_file

    # Load the YAML file
    with open(yaml_file, "r") as file:
        data = yaml.safe_load(file)

    # Iterate through the list of tickers and dates
    for entry in data:
        ticker = entry["ticker"]
        start_date = pd.to_datetime(entry["start_date"])
        end_date = pd.to_datetime(entry["end_date"])

        # Call compare_to_sp500 for each entry
        compare_to_sp500(ticker, start_date, end_date)

if __name__ == "__main__":
    main()
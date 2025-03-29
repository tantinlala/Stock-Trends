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

    # Iterate through the list of entries
    for entry in data:
        # Get the list of tickers
        tickers = entry["tickers"]
        start_date = pd.to_datetime(entry["start_date"])
        end_date = pd.to_datetime(entry["end_date"])
        
        # Get description if available, otherwise use None
        description = entry.get("description")
        
        # If description exists, create a custom title, otherwise use the default
        if description:
            tickers_str = ", ".join(tickers)
            title = f"{tickers_str} vs S&P 500: {description}"
        else:
            title = None

        # Call compare_to_sp500 with the list of tickers
        compare_to_sp500(tickers, start_date, end_date, title)

if __name__ == "__main__":
    main()
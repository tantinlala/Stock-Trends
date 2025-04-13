# Stock Trends Repository

This repository provides various tools for analyzing financial assets. 

## Repository Structure

- `stock_trends/data/`
  - Contains YAML files as inputs to various scripts.
- `stock_trends/scripts/`
  - Contains scripts for processing and analyzing stock data.
- `stock_trends/utils/`
  - Contains utility modules for downloading, plotting, and comparing stock data.

## How to Use

### Install Dependencies and Package

Install the required dependencies and the Python package by running:

```bash
pip install -e .
```

### Visualize Stock Trends

You can visualize stock trends by running the plotting script. Below is an example of a generated plot:

![Stock Trends Example](fed_hike_china_trade_war.png)

#### Steps to Use

1. **Create a YAML File**

Before processing the YAML files, you can create your own YAML file to define the stock tickers and time periods you want to analyze. Use the following structure as a reference:

```yaml
- tickers: [AAPL, MSFT, GOOGL]
  start_date: 2021-01-01
  end_date: 2021-12-31
  description: Example Analysis
```

Save this file in the `stock_trends/data/` directory with a `.yaml` extension.

2. **Run process-ticker-yaml console script**

The `process-ticker-yaml` script processes YAML files containing stock tickers and time periods for analysis. After installation, you can use it as follows:

```bash
process-ticker-yaml stock_trends/data/historical_tickers.yaml
```

This will process the specified YAML file and prepare the data for further analysis.

### Optimally allocate portfolio between two assets

The `allocate-portfolio` script is a tool for optimizing portfolio allocation between two assets (e.g., stocks and gold) based on two scenarios and a minimum acceptable payoff. It solves two optimization problems:

1. **Constrain Scenario A (>= minimum payoff), Maximize Scenario B.**
2. **Constrain Scenario B (>= minimum payoff), Maximize Scenario A.**

#### Steps to Use:

1. **Create a YAML Configuration File**  
   Define the returns for each asset in both scenarios and the minimum acceptable payoff. Use the following structure:

   ```yaml
   scenario_A:
     stonks: 0.05  # 5% return for stocks in scenario A
     gold: 0.02    # 2% return for gold in scenario A
   scenario_B:
     stonks: -0.03 # -3% return for stocks in scenario B
     gold: 0.01    # 1% return for gold in scenario B
   min_acceptable_payoff: 0.01  # Minimum acceptable payoff (1%)
   ```

   Save this file in the `stock_trends/data/` directory with a `.yaml` extension.

2. **Run the Script**  
   Execute the script using the following command:

   ```bash
   allocate-portfolio stock_trends/data/portfolio_config.yaml
   ```

3. **View Results**  
   The script will output the optimal allocation between stocks and gold for the given scenarios and constraints. It will also indicate which optimization problem provided the best result.

import argparse
import yaml
import sys
from scipy.optimize import linprog
import numpy as np

def load_config(yaml_path):
    """Loads configuration from a YAML file."""
    try:
        with open(yaml_path, 'r') as f:
            config = yaml.safe_load(f)
        # Basic validation
        required_keys = ['scenario_A', 'scenario_B', 'min_acceptable_payoff']
        if not all(key in config for key in required_keys):
            raise ValueError("YAML missing required keys (scenario_A, scenario_B, min_acceptable_payoff)")
        if not all(asset in config['scenario_A'] for asset in ['stonks', 'gold']):
             raise ValueError("YAML scenario_A missing 'stonks' or 'gold' key")
        if not all(asset in config['scenario_B'] for asset in ['stonks', 'gold']):
             raise ValueError("YAML scenario_B missing 'stonks' or 'gold' key")
        return config
    except FileNotFoundError:
        print(f"Error: YAML file not found at {yaml_path}", file=sys.stderr)
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error in YAML structure: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred loading config: {e}", file=sys.stderr)
        sys.exit(1)

def calculate_portfolio_return(w_stonks, r_stonks, r_gold):
    """Calculates the portfolio return for a given allocation."""
    w_gold = 1.0 - w_stonks
    return w_stonks * r_stonks + w_gold * r_gold

def solve_optimization(config):
    """Solves the two optimization problems and returns the best result."""

    rA_stonks = config['scenario_A']['stonks']
    rA_gold = config['scenario_A']['gold']
    rB_stonks = config['scenario_B']['stonks']
    rB_gold = config['scenario_B']['gold']
    min_payoff = config['min_acceptable_payoff']

    results = {}

    # --- Problem 1: Constrain A (>= min_payoff), Maximize B ---
    # Maximize: P_B = w_stonks * rB_stonks + (1 - w_stonks) * rB_gold
    #          P_B = w_stonks * (rB_stonks - rB_gold) + rB_gold
    # Minimize: -P_B = w_stonks * (rB_gold - rB_stonks) - rB_gold
    # Objective function coefficients for linprog (only variable part matters):
    c1 = [rB_gold - rB_stonks]

    # Constraint: P_A >= min_payoff
    # w_stonks * rA_stonks + (1 - w_stonks) * rA_gold >= min_payoff
    # w_stonks * (rA_stonks - rA_gold) + rA_gold >= min_payoff
    # w_stonks * (rA_stonks - rA_gold) >= min_payoff - rA_gold
    # If (rA_stonks - rA_gold) is negative (like in example):
    #   w_stonks <= (min_payoff - rA_gold) / (rA_stonks - rA_gold)
    # If (rA_stonks - rA_gold) is positive:
    #   w_stonks >= (min_payoff - rA_gold) / (rA_stonks - rA_gold)
    # Linprog constraint form: A_ub @ x <= b_ub
    # Constraint: -P_A <= -min_payoff
    # - (w_stonks * rA_stonks + (1 - w_stonks) * rA_gold) <= -min_payoff
    # w_stonks * (-rA_stonks + rA_gold) - rA_gold <= -min_payoff
    # w_stonks * (rA_gold - rA_stonks) <= rA_gold - min_payoff
    A_ub1 = [[rA_gold - rA_stonks]]
    b_ub1 = [rA_gold - min_payoff]

    # Bounds for w_stonks
    bounds = [(0, 1)]

    print("--- Solving Problem 1: Constrain A >= min, Maximize B ---")
    res1 = linprog(c1, A_ub=A_ub1, b_ub=b_ub1, bounds=bounds, method='highs') # 'highs' is default & robust

    if res1.success:
        w_stonks1 = res1.x[0]
        p_a1 = calculate_portfolio_return(w_stonks1, rA_stonks, rA_gold)
        p_b1 = calculate_portfolio_return(w_stonks1, rB_stonks, rB_gold)
        results['problem1'] = {'w_stonks': w_stonks1, 'p_a': p_a1, 'p_b': p_b1, 'max_value': p_b1}
        print(f"Success: w_stonks={w_stonks1:.4f}, P_A={p_a1:.4%}, P_B={p_b1:.4%}")
    else:
        print(f"Failed: {res1.message}")
        results['problem1'] = None


    # --- Problem 2: Constrain B (>= min_payoff), Maximize A ---
    # Maximize: P_A = w_stonks * rA_stonks + (1 - w_stonks) * rA_gold
    #          P_A = w_stonks * (rA_stonks - rA_gold) + rA_gold
    # Minimize: -P_A = w_stonks * (rA_gold - rA_stonks) - rA_gold
    # Objective function coefficients:
    c2 = [rA_gold - rA_stonks]

    # Constraint: P_B >= min_payoff
    # w_stonks * (rB_stonks - rB_gold) + rB_gold >= min_payoff
    # Constraint form: A_ub @ x <= b_ub
    # -P_B <= -min_payoff
    # w_stonks * (rB_gold - rB_stonks) <= rB_gold - min_payoff
    A_ub2 = [[rB_gold - rB_stonks]]
    b_ub2 = [rB_gold - min_payoff]

    print("\n--- Solving Problem 2: Constrain B >= min, Maximize A ---")
    res2 = linprog(c2, A_ub=A_ub2, b_ub=b_ub2, bounds=bounds, method='highs')

    if res2.success:
        w_stonks2 = res2.x[0]
        p_a2 = calculate_portfolio_return(w_stonks2, rA_stonks, rA_gold)
        p_b2 = calculate_portfolio_return(w_stonks2, rB_stonks, rB_gold)
        results['problem2'] = {'w_stonks': w_stonks2, 'p_a': p_a2, 'p_b': p_b2, 'max_value': p_a2}
        print(f"Success: w_stonks={w_stonks2:.4f}, P_A={p_a2:.4%}, P_B={p_b2:.4%}")
    else:
        print(f"Failed: {res2.message}")
        results['problem2'] = None

    # --- Compare Results ---
    best_result = None
    if results.get('problem1') and results.get('problem2'):
        if results['problem1']['max_value'] >= results['problem2']['max_value']:
            best_result = ('problem1', results['problem1'])
        else:
            best_result = ('problem2', results['problem2'])
    elif results.get('problem1'):
        best_result = ('problem1', results['problem1'])
    elif results.get('problem2'):
        best_result = ('problem2', results['problem2'])

    return best_result


def main():
    parser = argparse.ArgumentParser(description="Optimize portfolio allocation based on scenarios and constraints.")
    parser.add_argument("yaml_file", help="Path to the YAML configuration file.")
    args = parser.parse_args()

    config = load_config(args.yaml_file)
    print(f"\nLoaded configuration from: {args.yaml_file}")
    print(f"Scenario A Returns: Stonks={config['scenario_A']['stonks']:.2%}, Gold={config['scenario_A']['gold']:.2%}")
    print(f"Scenario B Returns: Stonks={config['scenario_B']['stonks']:.2%}, Gold={config['scenario_B']['gold']:.2%}")
    print(f"Minimum Acceptable Payoff: {config['min_acceptable_payoff']:.2%}")

    print("\nStarting optimization...")
    best_result = solve_optimization(config)

    print("\n--- Final Optimal Allocation ---")
    if best_result:
        name, data = best_result
        w_s = data['w_stonks']
        w_g = 1.0 - w_s
        print(f"Chosen solution from: {'Constrain A, Maximize B' if name == 'problem1' else 'Constrain B, Maximize A'}")
        print(f"Allocation: Stonks = {w_s:.2%}, Gold = {w_g:.2%}")
        print(f"Expected Return Scenario A: {data['p_a']:.4%}")
        print(f"Expected Return Scenario B: {data['p_b']:.4%}")
    else:
        print("No feasible solution found for either optimization problem.")

if __name__ == "__main__":
    main()
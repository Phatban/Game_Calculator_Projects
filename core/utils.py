"""
core/utils.py

Common utilities for probability calculations and reward simulations.
"""

import numpy as np

def calculate_expected_value(rewards):
    """
    Calculate expected value from a dictionary of rewards and probabilities.
    
    Parameters:
        rewards (dict): Keys are rewards, values are probabilities.
    
    Returns:
        float: Expected value.
    """
    return sum(reward * prob for reward, prob in rewards.items())

def simulate_spins(rewards, n_trials=10000):
    """
    Simulate spins using given reward probabilities.
    
    Parameters:
        rewards (dict): Keys are rewards, values are probabilities.
        n_trials (int): Number of spins.
    
    Returns:
        np.ndarray: Array of simulated results.
    """
    outcomes = list(rewards.keys())
    probabilities = list(rewards.values())
    return np.random.choice(outcomes, size=n_trials, p=probabilities)

def compute_rtp(results, payouts):
    """
    Compute RTP from simulation results and payout values.
    
    Parameters:
        results (array): List of obtained symbols or results.
        payouts (dict): Keys are results, values are payout amounts.
    
    Returns:
        float: RTP value.
    """
    total_return = sum(payouts.get(r, 0) for r in results)
    return total_return / len(results)

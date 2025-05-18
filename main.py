"""
main.py

Demo script using utility functions from core/utils.py
"""

from core.utils import calculate_expected_value, simulate_spins, compute_rtp

# Define a simple reward structure
rewards = {0: 0.6, 10: 0.3, 100: 0.1}
payouts = {0: 0, 10: 10, 100: 100}

# Calculate expected value
ev = calculate_expected_value(rewards)
print(f"Expected Value: {ev}")

# Simulate spins
results = simulate_spins(rewards, n_trials=10000)

# Compute RTP
rtp = compute_rtp(results, payouts)
print(f"Simulated RTP: {rtp}")

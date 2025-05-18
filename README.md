# 🎰 Game Calculator Projects

A collection of Python simulations and calculators designed to assist in the design and evaluation of game mechanics involving probability and rewards.

---

## 📁 Project List (Jupyter Notebooks)

These notebooks include visualization, simulation, and RTP analysis:

- **SpinSimulation_Visualizer**: Simulates multiple spin results to understand reward distribution randomness.
- **ExpectedValue_RTP_Calculator**: Calculates expected value and RTP (Return To Player) based on reward definitions.
- **Reward_Balancing_Optimizer**: Optimizes reward values to achieve a target RTP in game design.
- **GachaBox_Simulator**: Simulates Gacha draws and analyzes statistics for rare item probabilities.
- **SlotMachine_RTP_Simulator**: Simulates slot machine spins and calculates actual RTP based on spin outcomes.

---

## 🧠 Core Utilities

Reusable logic can be found in:

```
core/utils.py
```

Functions:
- `calculate_expected_value(rewards)`
- `simulate_spins(rewards, n_trials)`
- `compute_rtp(results, payouts)`

---

## 🚀 How to Run the Demo Script

You can run the main demonstration using:

```bash
python main.py
```

This script shows how to compute expected value and simulate RTP using predefined reward structures.

---

## 🧩 Requirements

Install necessary libraries using:

```bash
pip install -r requirements.txt
```

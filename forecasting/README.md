# SmartDemandLab Forecasting Module

This repository contains the forecasting and anomaly‑detection pipeline for **SmartDemandLab**. The goal is to predict the next 15‑minute active‑power measurement and assess the risk of exceeding the contracted demand (including the regulatory 5 % tolerance).

## Directory Structure
```
forecasting/
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── data/                     # Data handling utilities
│   └── data.py               # Load, clean, and window data
├── models/                   # Model definitions
│   ├── base.py               # Abstract model interface
│   ├── arima_model.py        # Classical statistical model
│   ├── xgboost_model.py      # Gradient‑boosting model
│   ├── lstm_model.py         # LSTM forecasting model
│   └── autoencoder.py        # LSTM Autoencoder for anomaly detection
├── scripts/                  # End‑to‑end scripts
│   ├── train.py              # Train all candidate models
│   ├── evaluate.py           # Evaluate on validation/test sets
│   ├── simulate.py           # Run the full billing‑cycle simulation
│   └── generate_synthetic.py # Create synthetic demand data
└── notebooks/                # Exploratory notebooks (optional)
    └── analysis.ipynb
```

## Quick Start
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Generate synthetic data (or point to real CSV files):
   ```bash
   python scripts/generate_synthetic.py --output data/synthetic.csv
   ```
3. Train models:
   ```bash
   python scripts/train.py --data data/synthetic.csv
   ```
4. Evaluate and run the simulation:
   ```bash
   python scripts/evaluate.py
   python scripts/simulate.py
   ```

The pipeline follows the **Implementation Plan** created earlier, including data preprocessing, model comparison, anomaly detection, and a decision engine for alerts.

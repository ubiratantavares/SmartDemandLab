import pandas as pd
import numpy as np
from pathlib import Path


def load_memory_of_mass(csv_path: str) -> pd.DataFrame:
    """Load raw CSV exported from the meter memory of mass.
    Expected columns: timestamp (ISO), W (active power in W), DCR, etc.
    The function converts W to kW, applies meter constant if needed, and
    returns a DataFrame indexed by a 15‑minute datetime index.
    """
    df = pd.read_csv(csv_path, parse_dates=["timestamp"])
    # Ensure 15‑min frequency
    df = df.set_index("timestamp").asfreq("15T")
    # Convert to kW (assuming column 'W' is in Watts)
    if "W" in df.columns:
        df["kW"] = df["W"] / 1000.0
    # Clean missing values (forward fill)
    df = df.ffill().bfill()
    return df


def create_sliding_windows(series: pd.Series, window_size: int = 16) -> (np.ndarray, np.ndarray):
    """Create overlapping windows for supervised learning.
    Returns X of shape (n_samples, window_size) and y of shape (n_samples,).
    """
    values = series.values
    n_samples = len(values) - window_size
    X = np.lib.stride_tricks.sliding_window_view(values, window_shape=window_size)[:n_samples]
    y = values[window_size:]
    return X, y

from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    counts = Counter(x.tolist())
    high_freq = max(counts.values())
    mode = min(value for value, count in counts.items() if count == high_freq)
    
    return {
        "mean": float(np.mean(x)),
        "median": float(np.median(x)),
        "mode": float(mode)
    }
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class FeatureScaler:
    def __init__(self, data):
        self.data = np.array(data)

    def min_max_scale(self):
        """Scales data to a fixed range [0, 1]."""
        min_val = np.min(self.data)
        max_val = np.max(self.data)
        return (self.data - min_val) / (max_val - min_val)

    def standardize(self):
        """Scales data to have Mean=0 and StdDev=1 (Z-score)."""
        mean_val = np.mean(self.data)
        std_val = np.std(self.data)
        return (self.data - mean_val) / std_val

if __name__ == "__main__":
    # Generate random data (e.g., house prices in Lakhs)
    np.random.seed(42)
    raw_data = np.random.normal(loc=50, scale=15, size=1000)

    scaler = FeatureScaler(raw_data)
    min_max = scaler.min_max_scale()
    z_score = scaler.standardize()

    # --- Visualization ---
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    axes[0].hist(raw_data, bins=30, color='gray', alpha=0.7)
    axes[0].set_title("Original Data\n(Range: ~10 to ~90)")

    axes[1].hist(min_max, bins=30, color='blue', alpha=0.7)
    axes[1].set_title("Min-Max Scaling\n(Range: 0 to 1)")

    axes[2].hist(z_score, bins=30, color='green', alpha=0.7)
    axes[2].set_title("Standardization\n(Mean: 0, Std: 1)")

    plt.tight_layout()
    plt.savefig('docs/scaler_comparison.png')
    plt.show()
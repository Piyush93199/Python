import pandas as pd
import numpy as np

class CategoricalEncoder:
    def __init__(self, data):
        self.df = data.copy()

    def label_encode(self, column):
        """Maps each unique category to a specific integer."""
        unique_vals = sorted(self.df[column].unique())
        # Create a mapping dictionary: {'Electronics': 0, 'Home': 1, ...}
        mapping = {val: i for i, val in enumerate(unique_vals)}
        
        encoded_series = self.df[column].map(mapping)
        return encoded_series, mapping

    def one_hot_encode(self, column):
        """Creates a binary matrix where each column represents a category."""
        unique_vals = sorted(self.df[column].unique())
        one_hot_data = {}

        for val in unique_vals:
            # Create a 1 if the value matches, 0 otherwise
            one_hot_data[f"{column}_{val}"] = (self.df[column] == val).astype(int)
        
        return pd.DataFrame(one_hot_data)

# --- Execution ---
if __name__ == "__main__":
    # Sample Dataset
    data = pd.DataFrame({
        'Product_ID': [101, 102, 103, 104, 105],
        'Category': ['Electronics', 'Clothing', 'Home', 'Electronics', 'Clothing']
    })

    encoder = CategoricalEncoder(data)

    print("--- Original Data ---")
    print(data)

    # 1. Label Encoding
    le_series, le_mapping = encoder.label_encode('Category')
    print("\n--- Label Encoding Results ---")
    print(f"Mapping: {le_mapping}")
    print(le_series)

    # 2. One-Hot Encoding
    ohe_df = encoder.one_hot_encode('Category')
    print("\n--- One-Hot Encoding Results ---")
    print(ohe_df)
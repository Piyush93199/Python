import pandas as pd
import numpy as np
import os

def manual_train_test_split(df, test_size=0.2, random_state=None):
    """
    Shuffles and splits a DataFrame into training and testing sets.
    test_size: float between 0 and 1 (default 0.2 for 20% test)
    """
    if random_state:
        np.random.seed(random_state)
    
    # 1. Shuffle the indices
    indices = np.random.permutation(len(df))
    
    # 2. Calculate the split point
    test_set_size = int(len(df) * test_size)
    
    # 3. Slice the indices
    test_indices = indices[:test_set_size]
    train_indices = indices[test_set_size:]
    
    # 4. Return the split DataFrames
    return df.iloc[train_indices], df.iloc[test_indices]

def run_experiment():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, "..", "data", "raw_data.csv")
    
    df = pd.read_csv(path)
    print(f"📋 Original Dataset Size: {len(df)} rows")
    
    # Perform 80/20 split
    train_df, test_df = manual_train_test_split(df, test_size=0.2, random_state=42)
    
    print("\n✅ Split Complete!")
    print(f"🏠 Training Set ({len(train_df)} rows):")
    print(train_df)
    
    print(f"\n🧪 Test Set ({len(test_df)} rows):")
    print(test_df)

if __name__ == "__main__":
    run_experiment()
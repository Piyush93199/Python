import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import glob

def get_data_path():
    """Dynamically finds the data folder relative to this script's location."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Goes up one level from 'src' to 'Outlier_Detector', then into 'data'
    return os.path.join(script_dir, "..", "data")

def load_latest_csv(folder_path):
    """Finds the most recent CSV file in the directory."""
    files = glob.glob(os.path.join(folder_path, "*.csv"))
    if not files:
        print(f"❌ No CSV files found in: {folder_path}")
        return None
    
    latest_file = max(files, key=os.path.getmtime)
    print(f"📂 Loading Dataset: {os.path.basename(latest_file)}")
    return pd.read_csv(latest_file)

def detect_outliers_iqr(df):
    """Calculates IQR and identifies outlier boundaries."""
    # Select the last numerical column (usually the target variable)
    num_cols = df.select_dtypes(include=[np.number]).columns
    if len(num_cols) == 0:
        print("❌ No numerical data found.")
        return None
    
    col = num_cols[-1]
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR
    
    outliers = df[(df[col] < lower_limit) | (df[col] > upper_limit)]
    
    print(f"\n📊 Statistics for '{col}':")
    print(f"   IQR: {IQR:.2f} | Range: [{lower_limit:.2f}, {upper_limit:.2f}]")
    print(f"   Total Outliers: {len(outliers)}")
    
    return col, outliers, lower_limit, upper_limit

if __name__ == "__main__":
    path = get_data_path()
    data = load_latest_csv(path)
    
    if data is not None:
        result = detect_outliers_iqr(data)
        if result:
            col_name, outlier_df, low, high = result
            
            # Visualization
            plt.figure(figsize=(10, 5))
            plt.boxplot(data[col_name], vert=False, patch_artist=True, 
                        boxprops=dict(facecolor='lightgreen', color='black'))
            plt.axvline(low, color='red', linestyle='--', label='Lower Limit')
            plt.axvline(high, color='blue', linestyle='--', label='Upper Limit')
            plt.title(f"IQR Outlier Detection: {col_name}")
            plt.legend()
            plt.grid(axis='x', linestyle=':', alpha=0.7)
            plt.show()
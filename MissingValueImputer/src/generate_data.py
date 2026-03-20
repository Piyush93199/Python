import pandas as pd
import numpy as np
import random

def generate_large_dataset(rows=100000):
    print(f"Generating {rows} rows of realistic logistics data...")
    
    data = {
        'Order_ID': [f"ORD-{10000+i}" for i in range(rows)],
        'Product_Category': [random.choice(['Electronics', 'Clothing', 'Home', 'Beauty', 'Sports']) for _ in range(rows)],
        
        # Numerical Columns with different distributions
        'Item_Weight_KG': np.random.normal(5, 2, rows).clip(0.1, 50), # Bell curve
        'Shipping_Cost': np.random.exponential(15, rows).clip(5, 200), # Skewed
        'Customer_Age': np.random.randint(18, 75, rows),             # Uniform
        'Delivery_Days': np.random.poisson(3, rows),                 # Discrete
        
        'Region': [random.choice(['North', 'South', 'East', 'West', 'Central']) for _ in range(rows)]
    }

    df = pd.DataFrame(data)

    # --- Introduce "Realistic" Missing Data (NaNs) ---
    # 1. Weight: 8% missing (random sensor failure)
    df.loc[df.sample(frac=0.08).index, 'Item_Weight_KG'] = np.nan
    
    # 2. Shipping Cost: 5% missing (entry error)
    df.loc[df.sample(frac=0.05).index, 'Shipping_Cost'] = np.nan
    
    # 3. Customer Age: 15% missing (optional field)
    df.loc[df.sample(frac=0.15).index, 'Customer_Age'] = np.nan

    # Save to CSV
    file_name = 'data/large_logistics_data.csv'
    df.to_csv(file_name, index=False)
    print(f"Success! Dataset saved to {file_name}")
    print(f"File Size: ~{df.memory_usage().sum() / 1e6:.2f} MB")

if __name__ == "__main__":
    import os
    if not os.path.exists('data'):
        os.makedirs('data')
    generate_large_dataset(100000)
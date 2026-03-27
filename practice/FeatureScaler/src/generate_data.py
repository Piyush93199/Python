import pandas as pd
import numpy as np
import os

def generate_scaling_data(rows=1000):
    # Ensure data directory exists
    if not os.path.exists('data'):
        os.makedirs('data')

    print(f"Generating {rows} rows of multi-scale data...")

    # Seed for reproducibility
    np.random.seed(42)

    data = {
        'House_ID': [f"H-{1000+i}" for i in range(rows)],
        
        # Feature 1: Small scale (Age of house in years: 0 to 50)
        'Age_Years': np.random.randint(0, 51, rows),
        
        # Feature 2: Large scale (Price in Lakhs: 10 to 500)
        'Price_Lakhs': np.random.normal(250, 75, rows).clip(10, 500),
        
        # Feature 3: Very Large scale (Square Footage: 500 to 5000)
        'Sq_Footage': np.random.uniform(500, 5000, rows).round(0),
        
        # Categorical tag (just for realism)
        'Location': np.random.choice(['Urban', 'Suburban', 'Rural'], rows)
    }

    df = pd.DataFrame(data)
    
    file_path = 'data/house_prices.csv'
    df.to_csv(file_path, index=False)
    
    print(f"✅ Success! Dataset created at: {file_path}")
    print("\nSample Data (Notice the difference in scales):")
    print(df[['Age_Years', 'Price_Lakhs', 'Sq_Footage']].head())

if __name__ == "__main__":
    generate_scaling_data()
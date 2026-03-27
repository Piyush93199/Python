import pandas as pd
import numpy as np
import random
import os

def create_sample_csv(rows=1000):
    # Ensure data directory exists
    if not os.path.exists('data'):
        os.makedirs('data')

    print(f"Generating {rows} rows of categorical data...")

    data = {
        'Employee_ID': [f"EMP-{1000+i}" for i in range(rows)],
        
        # Categorical Column 1: High cardinality (5 values)
        'Department': [random.choice(['Engineering', 'HR', 'Sales', 'Marketing', 'Finance']) for _ in range(rows)],
        
        # Categorical Column 2: Low cardinality (3 values)
        'Office_Location': [random.choice(['New Delhi', 'Mumbai', 'Bangalore']) for _ in range(rows)],
        
        # Categorical Column 3: Binary (2 values)
        'Remote_Work': [random.choice(['Yes', 'No']) for _ in range(rows)],
        
        # Numerical Column (for reference)
        'Years_Experience': np.random.randint(1, 15, rows),
        'Performance_Score': np.random.uniform(1.0, 5.0, rows).round(1)
    }

    df = pd.DataFrame(data)
    
    file_path = 'data/employees.csv'
    df.to_csv(file_path, index=False)
    
    print(f"✅ Success! Sample dataset created at: {file_path}")
    print(df.head()) # Show a preview

if __name__ == "__main__":
    create_sample_csv()
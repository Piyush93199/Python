import pandas as pd
import sys

def explore_csv(file_path):
    try:
        # Load the dataset
        df = pd.read_csv(file_path)
        
        print(f"\n{'='*20} DATA REPORT: {file_path} {'='*20}")
        
        # 1. Basic Shape
        print(f"\n[1] Dimensions: {df.shape[0]} rows, {df.shape[1]} columns")
        
        # 2. Data Types & Missing Values
        print("\n[2] Schema & Missing Values:")
        info_df = pd.DataFrame({
            'Data Type': df.dtypes,
            'Missing Values': df.isnull().sum(),
            '% Missing': (df.isnull().sum() / len(df) * 100).round(2)
        })
        print(info_df)
        
        # 3. Basic Statistics for Numerical Columns
        print("\n[3] Numerical Summary:")
        if not df.select_dtypes(include=['number']).empty:
            print(df.describe().T.round(2))
        else:
            print("No numerical columns found.")
            
        # 4. Unique Values for Categorical Columns
        print("\n[4] Categorical Summary (Unique Counts):")
        cat_cols = df.select_dtypes(include=['object', 'category']).columns
        if not cat_cols.empty:
            for col in cat_cols:
                print(f"- {col}: {df[col].nunique()} unique values")
        else:
            print("No categorical columns found.")
            
        print(f"\n{'='*55}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python data_explorer.py your_data.csv")
    else:
        explore_csv(sys.argv[1])
import pandas as pd
import os

def engineer_date_features(df, date_column):
    """
    Transforms a string date column into useful ML features.
    """
    # 1. Convert to datetime objects
    df[date_column] = pd.to_datetime(df[date_column])
    
    # 2. Extract basic components
    df['Year'] = df[date_column].dt.year
    df['Month'] = df[date_column].dt.month
    df['Day'] = df[date_column].dt.day
    
    # 3. Extract Day of Week (0=Monday, 6=Sunday)
    df['Day_of_Week'] = df[date_column].dt.dayofweek
    
    # 4. Extract Day Name (for readability)
    df['Day_Name'] = df[date_column].dt.day_name()
    
    # 5. Create Binary Feature: Is_Weekend (Saturday=5, Sunday=6)
    df['Is_Weekend'] = df['Day_of_Week'].apply(lambda x: 1 if x >= 5 else 0)
    
    return df

def run_experiment():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, "..", "data", "raw_dates.csv")
    
    df = pd.read_csv(path)
    print("📋 Original Data:")
    print(df)
    
    # Run the engineering
    df_transformed = engineer_date_features(df, 'Date')
    
    print("\n🚀 Engineered Features:")
    # Selecting specific columns to show the transformation
    cols_to_show = ['Date', 'Month', 'Day_Name', 'Day_of_Week', 'Is_Weekend']
    print(df_transformed[cols_to_show])

if __name__ == "__main__":
    run_experiment()
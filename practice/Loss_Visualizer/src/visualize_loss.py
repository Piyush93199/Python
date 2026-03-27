import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def load_data():
    """Loads the sample predictions CSV and ensures columns are numeric."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "..", "data", "sample_predictions.csv")
    
    df = pd.read_csv(data_path)
    
    # Convert columns to numeric, turning strings into NaN, then dropping them
    df['Predicted'] = pd.to_numeric(df['Predicted'], errors='coerce')
    df['Actual'] = pd.to_numeric(df['Actual'], errors='coerce')
    
    # Drop any row that couldn't be converted to a number
    df = df.dropna(subset=['Predicted', 'Actual'])
    
    print(f"📂 Loading data from: {os.path.basename(data_path)}")
    return df

def calculate_losses(df):
    """Calculates individual errors, absolute errors, and squared errors."""
    # 1. Calculate Raw Error (Residual)
    df['Error'] = df['Predicted'] - df['Actual']
    
    # 2. Calculate Absolute Error (for MAE)
    df['Absolute_Error'] = df['Error'].abs()
    
    # 3. Calculate Squared Error (for MSE)
    df['Squared_Error'] = df['Error'] ** 2
    
    # Calculate overall metrics
    mae = df['Absolute_Error'].mean()
    mse = df['Squared_Error'].mean()
    rmse = np.sqrt(mse) # Root Mean Squared Error (interpretable scale)
    
    print(f"\n📊 Global Metrics:")
    print(f"   MAE (Mean Absolute Error): {mae:.2f}")
    print(f"   MSE (Mean Squared Error): {mse:.2f}")
    print(f"   RMSE (Root MSE): {rmse:.2f}")
    
    return df

def visualize_comparison(df):
    """Generates plots to compare MSE and MAE behavior."""
    plt.figure(figsize=(14, 6))
    
    # Plot 1: Bar Chart of Errors per Data Point
    plt.subplot(1, 2, 1)
    x = np.arange(len(df))
    width = 0.35
    
    plt.bar(x - width/2, df['Absolute_Error'], width, label='Absolute Error (|e|)', color='skyblue', edgecolor='black')
    plt.bar(x + width/2, df['Squared_Error'], width, label='Squared Error (e²)', color='salmon', edgecolor='black', alpha=0.8)
    
    plt.axhline(df['Absolute_Error'].mean(), color='blue', linestyle='--', label='Mean Abs Error')
    
    plt.title("Error Penalty Comparison per Data Point")
    plt.xlabel("Data Point Index")
    plt.ylabel("Loss Value")
    plt.xticks(x)
    plt.legend()
    plt.grid(axis='y', linestyle=':', alpha=0.5)
    
    # Plot 2: Penalty Curves (Conceptual)
    plt.subplot(1, 2, 2)
    # Generate smooth error range from -50 to 50
    error_range = np.linspace(-50, 50, 100)
    
    # Define MAE and MSE curves
    mae_curve = np.abs(error_range)
    mse_curve = error_range ** 2
    
    # Scale MSE curve slightly down just for visual comparison on same plot
    plt.plot(error_range, mae_curve, label='MAE Penalty (|e|)', color='blue', linewidth=3)
    plt.plot(error_range, mse_curve / 10, label='MSE Penalty (e²/10 scaled)', color='red', linewidth=3, linestyle='--')
    
    plt.title("Loss Function Penalty Curves")
    plt.xlabel("Actual Prediction Error (e)")
    plt.ylabel("Loss / Penalty Value")
    plt.axvline(0, color='black', linewidth=1)
    plt.axhline(0, color='black', linewidth=1)
    plt.legend()
    plt.grid(linestyle=':', alpha=0.5)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    try:
        data = load_data()
        analyzed_data = calculate_losses(data)
        
        print("\n📝 Detailed Data Analysis:")
        print(analyzed_data[['Actual', 'Predicted', 'Error', 'Absolute_Error', 'Squared_Error']])
        
        visualize_comparison(analyzed_data)
        
    except FileNotFoundError:
        print("❌ Error: 'sample_predictions.csv' not found. Please run Step 2 first.")
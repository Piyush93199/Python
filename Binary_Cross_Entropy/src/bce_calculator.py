import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def load_test_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, "..", "data", "test_cases.csv")
    return pd.read_csv(path)

def calculate_bce(y_true, y_pred):
    """
    Computes Binary Cross-Entropy Loss.
    We add a tiny 'epsilon' to prevent log(0) which is undefined.
    """
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    
    # The BCE Formula
    loss = - (y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    return loss

def run_experiment():
    df = load_test_data()
    df['BCE_Loss'] = calculate_bce(df['Actual'], df['Predicted_Prob'])
    
    print("\n🧪 Binary Cross-Entropy Experiment Results:")
    print(df.to_string(index=False))
    
    # Visualization
    plt.figure(figsize=(10, 6))
    colors = ['green' if loss < 0.5 else 'red' for loss in df['BCE_Loss']]
    
    plt.bar(range(len(df)), df['BCE_Loss'], color=colors, edgecolor='black')
    plt.xticks(range(len(df)), [f"Act:{a}\nProb:{p}" for a, p in zip(df['Actual'], df['Predicted_Prob'])])
    
    plt.title("Log Loss Penalty per Prediction")
    plt.ylabel("Loss Value (Higher = Worse)")
    plt.xlabel("Test Scenarios (Actual Label vs Predicted Probability)")
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.show()

if __name__ == "__main__":
    run_experiment()
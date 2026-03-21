# 📊 Loss Visualizer

A clean and interactive Python tool designed to visualize and compare common loss functions used in machine learning, specifically focusing on **Mean Absolute Error (MAE)** and **Mean Squared Error (MSE)**.

---

## 🚀 Overview

The **Loss Visualizer** helps data scientists and ML enthusiasts understand how different loss functions penalize errors. By calculating and plotting these metrics, it provides a clear picture of why certain functions are more sensitive to outliers than others.

### 🔥 Key Metrics
- **MAE (Mean Absolute Error):** Measures the average magnitude of errors without considering their direction.
- **MSE (Mean Squared Error):** Squaring the errors emphasizes larger discrepancies, making it more sensitive to outliers.
- **RMSE (Root Mean Squared Error):** The square root of MSE, providing an interpretable error metric in the same units as the target variable.

---

## 🛠 Features

- **Automated Data Processing:** Loads predictions and actual values from a standard CSV format.
- **Detailed Analytics:** Prints global metrics (MAE, MSE, RMSE) and a per-point error breakdown.
- **Advanced Visualizations:**
  - **Error Comparison Bar Chart:** Illustrates per-point Absolute vs. Squared error penalties.
  - **Penalty Curves:** A conceptual side-by-side view showing the linear vs. quadratic growth of penalties.

---

## 📁 Project Structure

```text
Loss_Visualizer/
├── data/
│   └── sample_predictions.csv   # Dataset with Actual vs Predicted values
├── src/
│   └── visualize_loss.py        # Main execution script
├── .gitignore                   # Standard Python gitignore rules
├── requirements.txt             # Required Python libraries
└── README.md                    # Project documentation
```

---

## ⚡ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Piyush93199/Python.git
cd Loss_Visualizer
```

### 2. Set up a Virtual Environment (Optional but Recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 📊 Usage

To run the visualization and see the error analysis, execute:

```bash
python src/visualize_loss.py
```

### Sample Data Format (`data/sample_predictions.csv`)
Ensure your CSV follows this structure:
| Actual | Predicted |
| :--- | :--- |
| 100 | 105 |
| 200 | 195 |
| 500 | 850 |

---

## 🧪 Experiments

Observe how the plots change as you modify values in `data/sample_predictions.csv`. In particular, notice how MSE explodes when the "Actual" and "Predicted" values diverge significantly.

---

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

---

*Made with ❤️ by Piyush*

# 🔬 Binary Cross-Entropy (BCE) Calculator

![BCE Banner](./docs/bce_banner.png)

A lightweight Python tool to calculate and visualize Binary Cross-Entropy (Log Loss) across various prediction scenarios. This project helps in understanding how BCE penalizes incorrect predictions with high confidence.

## 🌟 Key Features

- **Accurate BCE Calculation**: Implementation of the Log Loss formula with epsilon clipping for numerical stability.
- **Data-Driven Evaluation**: Loads test cases from CSV files to assess model performance.
- **Dynamic Visualization**: Uses Matplotlib to generate intuitive bar charts showing the penalty/loss per scenario.
- **Numerical Stability**: Handles extreme probabilities (0 or 1) by clipping, avoiding `log(0)` errors.

## 📐 The Math Behind It

Binary Cross-Entropy is defined by the formula:

$$Loss = - \frac{1}{N} \sum_{i=1}^{N} [y_i \cdot \log(p_i) + (1 - y_i) \cdot \log(1 - p_i)]$$

Where:
- $y_i$ is the actual label (0 or 1).
- $p_i$ is the predicted probability of being class 1.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Piyush93199/Python.git
   cd Binary_Cross_Entropy
   ```

2. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Experiment

To execute the BCE calculation and see the visual results:

```bash
python src/bce_calculator.py
```

## 📊 Project Structure

```text
Binary_Cross_Entropy/
├── src/
│   └── bce_calculator.py    # Main calculation & plotting script
├── data/
│   └── test_cases.csv       # Dataset for experimentation
├── docs/
│   └── bce_banner.png       # README assets
├── requirements.txt         # Project dependencies
└── .gitignore               # Ignored files and folders
```

## 📝 Example CSV Input (`data/test_cases.csv`)

| Scenario | Actual | Predicted_Prob |
|----------|--------|----------------|
| Confident Success | 1 | 0.95 |
| Uncertain | 1 | 0.60 |
| Confident Failure | 0 | 0.85 |
| Almost Correct | 0 | 0.05 |

## 🤝 Contributing

Feel free to open issues or submit pull requests to enhance the calculator or add more visualization types!

---
Developed by **Piyush Chaubey** 🚀

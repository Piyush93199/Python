# 🏷️ CategoricalEncoder

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-data%20analysis-150458.svg)
![NumPy](https://img.shields.io/badge/numpy-numerical%20computing-013243.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-black.svg)](https://github.com/Piyush93199/Categorical-Encoder-Scratch)

**CategoricalEncoder** is a lightweight Python utility that implements custom Label Encoding and One-Hot Encoding for categorical data features using `pandas` and `numpy`. 

It demonstrates how categorical encoding works under the hood without relying on external machine learning libraries like `scikit-learn`. 🚀

## ✨ Features

- **🔢 Label Encoding**: Converts categorical text values into corresponding distinct integer labels.
- **🔥 One-Hot Encoding**: Transforms a categorical column into a binary sparse matrix format (dummy variables).
- **🗂️ Data Generator**: Includes a dataset generation script that creates randomized tabular records to simulate exploring or testing the encoders.

## 📂 Project Structure

- `src/categorical_encoder.py`: Contains the `CategoricalEncoder` class capable of carrying out both label and one-hot encoding operations.
- `src/generate_data.py`: A helper script that creates a mockup CSV file populated with categorical (e.g., Departments) and numerical data.
- `requirements.txt`: Lists the bare project dependencies (`pandas`, `numpy`).

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Piyush93199/Categorical-Encoder-Scratch.git
   cd Categorical-Encoder-Scratch
   ```
2. **(Optional but recommended) Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. **Install the necessary dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### 🛠️ Generating Sample Data
To create a fake tabular dataset, run the data generator:
```bash
python src/generate_data.py
```
This builds `data/employees.csv` containing columns across multiple data types with varied cardinalities.

### 📊 Encoding Data
You can interact with the `CategoricalEncoder` object directly to encode single features:

```python
import pandas as pd
from src.categorical_encoder import CategoricalEncoder

# Sample usage dataset
data = pd.DataFrame({
    'Product_ID': [101, 102, 103],
    'Category': ['Electronics', 'Clothing', 'Home']
})

# Instantiate the encoder
encoder = CategoricalEncoder(data)

# 1. Label Encoding
le_series, mapping = encoder.label_encode('Category')
print(f"Label Mapping: {mapping}")
print(le_series)

# 2. One-Hot Encoding
ohe_df = encoder.one_hot_encode('Category')
print(ohe_df)
```
You can also run `categorical_encoder.py` directly to see an interactive example:
```bash
python src/categorical_encoder.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

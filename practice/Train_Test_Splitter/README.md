# 🧪 Train Test Splitter

A robust Python utility to manually shuffle and split your datasets into training and testing sets. This tool is designed to provide greater control over the splitting process without relying heavily on complex libraries, while still utilizing the efficiency of `pandas` and `numpy`.

## ✨ Features

-   **Manual Control**: Understand exactly how your data is being shuffled and split.
-   **Reproducibility**: Set a `random_state` to ensure consistent results across different runs.
-   **CSV Integration**: Easily load data from CSV files and visualize the split results.
-   **Scalable**: Leverages `numpy` for high-performance index permutations.

---

## 🚀 Quick Start

### 📋 Prerequisites

Ensure you have Python installed, then install the required dependencies:

```bash
pip install -r requirements.txt
```

### 🛠️ Installation

```bash
git clone https://github.com/Piyush93199/Train_Test_Splitter.git
cd Train_Test_Splitter
```

### 🏃 Running the Splitter

Execute the main script to see it in action with the sample data provided:

```bash
python src/splitter.py
```

---

## 📂 Project Structure

```bash
Train_Test_Splitter/
├── data/               # Contains raw and processed data
│   └── raw_data.csv    # Your source dataset
├── src/                # Source code
│   └── splitter.py     # Main splitting logic and experiment script
├── .gitignore          # Comprehensive Python-centric git exclusions
├── requirements.txt    # Project dependencies
└── README.md           # You are here!
```

---

## ⚙️ How it Works

The core functionality lies in the `manual_train_test_split` function:

```python
def manual_train_test_split(df, test_size=0.2, random_state=None):
    # Shuffles indices and returns (train_df, test_df)
    ...
```

It takes a `pandas.DataFrame` and returns a tuple of two DataFrames, the first for training and the second for testing, based on the specified `test_size`.

---

## 🤝 Contributing

Contributions are welcome! If you find a bug or have a suggestion, please open an issue or submit a pull request.

---

## 📄 License

This project is open-source and available under the MIT License.

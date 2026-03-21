# 📊 Outlier Detector

A lightweight and efficient Python tool designed to identify outliers in numerical datasets using the **Interquartile Range (IQR)** method. This script automatically detects the latest CSV in your data folder and provides detailed statistics alongside visual representations.

## ✨ Features

- **Automated Data Discovery**: Dynamically locates the newest CSV file in your `data/` directory.
- **IQR-Based Detection**: Robust statistical methodology to identify outliers in the primary numerical column.
- **Statistical Summary**: Provides IQR, lower/upper boundaries, and a count of detected outliers.
- **Data Visualization**: Generates clear, annotated boxplots with boundary markers.
- **Clean Structure**: Organized project layout for easy extensibility.

## 📁 Project Structure

```text
Outlier_Detector/
├── data/               # Folder for CSV datasets
│   └── IBM_HR_Data.csv # Sample dataset
├── src/                # Project source code
│   └── outlier_detector.py
├── .gitignore          # Git exclusion rules
├── requirements.txt     # Project dependencies
└── README.md           # Documentation
```

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have **Python 3.7+** installed on your system.

### 2. Installation
Clone the repository and install the required libraries:

```bash
# Clone the repository
git clone https://github.com/Piyush93199/Python.git
cd Outlier_Detector

# (Optional) Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Usage
Place your CSV file in the `data/` directory, then run the script:

```bash
python src/outlier_detector.py
```

## 🛠 How It Works
1. **Load Data**: The script looks for the most recently modified CSV in the `data/` folder.
2. **Detect Outliers**: It selects the last numerical column in the dataset and calculates the **Interquartile Range (IQR)**:
   - **Q1**: 25th percentile
   - **Q3**: 75th percentile
   - **IQR**: Q3 - Q1
   - **Lower Bound**: Q1 - 1.5 * IQR
   - **Upper Bound**: Q3 + 1.5 * IQR
3. **Visualize**: A boxplot is generated showing the distribution and highlighting the outlier thresholds.

## 📦 Dependencies
- `pandas` - Data manipulation and analysis.
- `numpy` - Numerical computing.
- `matplotlib` - Data visualization.

---
*Created with ❤️ for Python Data Enthusiasts.*

# 📊 Pandas Data Explorer

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight and powerful command-line interface (CLI) tool designed for rapid Exploratory Data Analysis (EDA). This script automates the tedious parts of data cleaning and inspection by instantly generating insights into missing data, data types, and statistical summaries for any CSV dataset.

---

## 📑 Table of Contents
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Examples](#-examples)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- **📏 Shape Detection**: Instantly see row and column counts to understand the scale of your data.
- **🧩 Missing Value Heatmap**: Comprehensive view of missing data, displaying both exact counts and percentages of null values per column.
- **📈 Statistical Transpose**: A clean, readable summary table detailing Mean, Median, Min, Max, and Standard Deviation for all numerical features.
- **🔠 Categorical Insights**: Get quick unique value counts and frequencies for non-numerical (categorical) columns.
- **🚀 Fast and Lightweight**: Uses `pandas` natively to quickly process datasets from the command line.

## 🛠️ Prerequisites

Before you begin, ensure you have met the following requirements:
- **Python 3.8** or higher installed on your machine.
- `pip` or another python package manager.

## 📦 Installation

Clone the repository and install the required dependencies:

```bash
# Clone the repository (if applicable)
git clone https://github.com/yourusername/Data_Explorer.git
cd Data_Explorer

# Install the dependencies
pip install -r requirements.txt
```

*(Note: The `requirements.txt` should contain necessary dependencies, typically `pandas`.)*

## 🚀 Usage

Using the Data Explorer is incredibly simple. Just run the script and pass the path to your CSV file as an argument.

```bash
python src/data_explorer.py <path_to_your_file.csv>
```

## 💡 Examples

To test the script, you can use the provided sample dataset:

```bash
python src/data_explorer.py data/sample.csv
```

**Expected Output Breakdown:**
1. **Dataset Overview**: Prints total rows and columns.
2. **Missing Values**: Highlights columns with missing values and what percentage of data is missing.
3. **Data Types**: Summarizes all column data types.
4. **Summary Statistics**: Displays metrics like min, max, average, and quantiles.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check [issues page](#) if you have any questions or ideas for improvements.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---
*Built with ❤️ for Data Enthusiasts.*

# Date Feature Engineering Utility 📅

A simple, efficient Python script for transforming raw date strings into useful features for Machine Learning and data analysis.

## Overview

This project provides a utility to engineer time-based features from dates using `pandas`. It's designed to help you quickly extract valuable information from date-time columns, which can then be used to improve performance in predictive models.

## ✨ Features

The script automatically extracts the following features from a date column:
- **Year**: Numerical representation of the year.
- **Month**: Numerical representation of the month (1-12).
- **Day**: Numerical representation of the day of the month.
- **Day of Week**: Numerical representation (0=Monday, 6=Sunday).
- **Day Name**: Human-readable name (e.g., 'Monday', 'Tuesday').
- **Is Weekend**: Binary indicator (1 for Saturday/Sunday, 0 for weekdays).

## 📁 Project Structure

```text
Date_Feature_Engineering/
├── data/
│   └── raw_dates.csv      # Sample input data
├── src/
│   └── date_processor.py  # Main transformation logic
├── .gitignore             # Git ignore rules for Python projects
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher.
- `pandas` library.

### Installation

1. Clone or download this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run the `date_processor.py` script to see the feature engineering in action using the sample data:

```bash
python3 src/date_processor.py
```

### 💡 Example Output

The script transforms data like this:

| Date | Month | Day_Name | Day_of_Week | Is_Weekend |
| :--- | :--- | :--- | :--- | :--- |
| 2026-03-20 | 3 | Friday | 4 | 0 |
| 2026-03-21 | 3 | Saturday | 5 | 1 |
| 2026-03-22 | 3 | Sunday | 6 | 1 |

## 🛠️ Requirements

- `pandas>=3.0.1`

## 📄 License

This project is for educational purposes. Feel free to use and modify it.

# DataPrep Studio

DataPrep Studio is a powerful, desktop-based GUI application built with Python and PyQt5. It empowers Data Scientists and Analysts to rapidly clean, preprocess, and visualize their tabular datasets without writing a single line of code—all from a sleek natively embedded interface.

## 🚀 Features

* **Data Profiling**: Instantly view row/column counts, missing values, and data types.
* **Missing Value Imputation**: Handle missing data dynamically with `mean`, `median`, `mode`, or `constant` strategies.
* **Categorical Encoding**: Rapidly convert string labels via Label Encoding or One-Hot Encoding.
* **Feature Scaling**: Apply `Min-Max Scaling` and `Standardization` seamlessly.
* **Outlier Detection & Removal**: Detect and highlight anomalies utilizing `IQR` bounds or `Z-Score` thresholds.
* **Native Embedded Visualization**: Generate and view analytical diagrams (Histograms, Boxplots, and Correlation Heatmaps) via a fully-embedded matplotlib canvas. Retrieve past plots easily using the Plot History dropdown.
* **Train-Test Splitting**: Effortlessly split clean data and define custom seeds/test sizes.
* **Fluid UI & Animations**: Enjoy smooth panel transitions and animated message notifications in a clean, modern Light Mode aesthetic.
* **Synthetic Dataset Generator**: Create customizable sample datasets to test various data cleaning scenarios.
* **Data Exporting**: Save your final, clean datasets back to `.csv` or `.xlsx` files.

## 🛠️ Installation

1. Clone this repository or download the source code.
2. Initialize and activate a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Usage
Make sure your virtual environment is activated, then simply run the main application file:
```bash
python main.py
```

To generate a synthetic testing dataset with mixed data types, missing values, and outliers:
```bash
python data/generate_dataset.py --rows 1000 --output data/sample_dataset.csv
```

## 📁 Project Structure

* `/core/`: Handles pandas-based logic (encoders, imputers, scalers, outliers).
* `/gui/`: Contains all PyQt5 Dashboard components, control panels, and UI flow.
* `/visualization/`: Matplotlib & Seaborn integration scripts.
* `/data/`: (Optional) Drop your `.csv` dataset files here.
* `/logs/`: Application generated diagnostic files.
* `/assets/`: Place icons, themes, or images.
* `/docs/`: Documentation.

## 🤝 Contributing
Feel free to open issues or submit Pull Requests for new features (like Data Parsing Logs, JSON Exporting, etc.).

## 📝 License
MIT License

# Missing Value Imputer

The **Missing Value Imputer** is an interactive, GUI-based tool designed to help developers and data scientists evaluate different strategies for handling missing values (NaNs) in their datasets. It allows you to visualize how applying different imputation methods (Mean, Median, Mode, Zero-Fill) impacts the statistical properties of a specific feature.

It features a sleek, modern UI built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter), offering a real-time analysis report.

## 🚀 Features

- **Synthetic Data Generator**: Includes a script to generate realistic logistics datasets with randomized missing values for practical testing.
- **Modern User Interface**: A beautifully designed, Dark Mode enabled Graphical User Interface built with `customtkinter`.
- **Automatic Column Detection**: The tool automatically scans your dataset for numerical/categorical columns that contain missing values (`NaN`).
- **Strategy Comparison**: Quickly compare the new metrics (like the resulting `Mean`) of the imputed column after applying:
  - Mean Substitution
  - Median Substitution
  - Mode Substitution
  - Zero-Fill

## 📦 File Structure

- `src/imputer_tool.py`: The main GUI application to load CSV files and compare imputation strategies.
- `src/generate_data.py`: A helper script that generates `large_logistics_data.csv` inside the `data/` directory with randomly introduced missing values.
- `requirements.txt`: Project dependencies and libraries.
- `data/`: Directory where the datasets (like the generated CSV) are stored. (Ignored by Git, except for `.gitkeep`).

## 🛠️ Installation

1. **Clone the repository** (if applicable) or download the files.

2. **Create and Activate a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Linux/macOS
   .venv\Scripts\activate   # On Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 How to Use

### 1. Generating Test Data
If you don't have a dataset with missing values at hand, generate one automatically by running:
```bash
python src/generate_data.py
```
This will produce a `large_logistics_data.csv` file inside the `data/` folder.

### 2. Running the Imputer Tool
Launch the interactive tool by running:
```bash
python src/imputer_tool.py
```

### 3. Comparing Strategies
- Click **Browse CSV File** and select your dataset (e.g., `data/large_logistics_data.csv`).
- The program will automatically filter columns with missing information.
- Select your target column from the dropdown menu.
- Click **Compare Strategies** to view the resulting changes to the variable's metrics.

## 🤝 Next Steps
Possible future improvements could include:
- Visual plotting of distributions (e.g., using `matplotlib` inside the UI).
- Export functionality for the imputed data frame.
- Adding advanced imputation algorithms like KNN or Iterative (MICE) Imputers.

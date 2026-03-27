"""
Synthetic Dataset Generator for Data Cleaning Testing

Features:
- Configurable number of rows (n)
- Mixed data types (numeric + categorical)
- Random missing values
- Controlled outliers
- Reproducible via random seed
- Saves to CSV

Usage:
    python generate_dataset.py --rows 1000 --output sample_dataset.csv
"""

import numpy as np
import pandas as pd
import argparse
import random


def generate_dataset(n=1000, missing_rate=0.1, outlier_rate=0.02, seed=42):
    np.random.seed(seed)
    random.seed(seed)

    # ----- Base Data -----
    data = {
        "Age": np.random.normal(loc=35, scale=10, size=n).astype(int),
        "Salary": np.random.normal(loc=50000, scale=15000, size=n),
        "Experience": np.random.normal(loc=10, scale=5, size=n),
        "Department": np.random.choice(
            ["HR", "IT", "Sales", "Marketing", "Finance"], size=n
        ),
        "City": np.random.choice(
            ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata"], size=n
        ),
        "PerformanceScore": np.random.uniform(1, 5, size=n),
    }

    df = pd.DataFrame(data)

    # ----- Inject Missing Values -----
    total_cells = df.size
    num_missing = int(total_cells * missing_rate)

    for _ in range(num_missing):
        row = np.random.randint(0, n)
        col = np.random.randint(0, df.shape[1])
        df.iat[row, col] = np.nan

    # ----- Inject Outliers -----
    num_outliers = int(n * outlier_rate)

    numeric_cols = df.select_dtypes(include=[np.number]).columns

    for col in numeric_cols:
        indices = np.random.choice(n, num_outliers, replace=False)

        # Extreme high or low values
        df.loc[indices, col] = (
            df[col].mean()
            + np.random.choice([-1, 1]) * 6 * df[col].std()
        )

    # ----- Add Duplicates (optional realism) -----
    duplicate_rows = df.sample(frac=0.01, random_state=seed)
    df = pd.concat([df, duplicate_rows], ignore_index=True)

    return df


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--rows",
        type=int,
        default=1000,
        help="Number of dataset rows",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="sample_dataset.csv",
        help="Output CSV file",
    )

    args = parser.parse_args()

    df = generate_dataset(n=args.rows)

    df.to_csv(args.output, index=False)

    print("Dataset created")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("File:", args.output)


if __name__ == "__main__":
    main()
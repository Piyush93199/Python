import pandas as pd


def detect_outliers_iqr(df, column):

    if column not in df.columns:
        return pd.Series([False] * len(df))

    if not pd.api.types.is_numeric_dtype(
        df[column]
    ):
        return pd.Series([False] * len(df))

    q1 = df[column].quantile(0.25)

    q3 = df[column].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr

    upper = q3 + 1.5 * iqr

    mask = (
        (df[column] < lower)
        |
        (df[column] > upper)
    )

    return mask

def detect_outliers_zscore(
    df,
    column,
    threshold=3.0,
):

    if column not in df.columns:
        return pd.Series(
            [False] * len(df)
        )

    if not pd.api.types.is_numeric_dtype(
        df[column]
    ):
        return pd.Series(
            [False] * len(df)
        )

    mean = df[column].mean()

    std = df[column].std()

    if std == 0:
        return pd.Series(
            [False] * len(df)
        )

    z_scores = (
        df[column] - mean
    ) / std

    mask = (
        z_scores.abs() > threshold
    )

    return mask

def remove_outliers(
    df,
    mask,
):

    cleaned_df = df.loc[
        ~mask
    ].reset_index(
        drop=True
    )

    return cleaned_df
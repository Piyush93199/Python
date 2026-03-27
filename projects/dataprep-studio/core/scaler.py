import pandas as pd


def is_numeric_column(df, column):

    return pd.api.types.is_numeric_dtype(
        df[column]
    )


def min_max_scale(df, column):

    if not is_numeric_column(df, column):
        return df

    col_min = df[column].min()

    col_max = df[column].max()

    if col_max == col_min:
        return df

    df[column] = (
        df[column] - col_min
    ) / (col_max - col_min)

    return df


def standardize(df, column):

    if not is_numeric_column(df, column):
        return df

    mean = df[column].mean()

    std = df[column].std()

    if std == 0:
        return df

    df[column] = (
        df[column] - mean
    ) / std

    return df
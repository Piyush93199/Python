import pandas as pd


def is_numeric_column(df, column):

    return pd.api.types.is_numeric_dtype(
        df[column]
    )


def mean_impute(
    df,
    column,
):

    value = df[column].mean()

    series = df[column].dropna()

    if (series % 1 == 0).all():

        value = int(round(value))

    df[column] = df[column].fillna(value)

    return df


def median_impute(df, column):

    if not is_numeric_column(df, column):
        print("Median not allowed for non-numeric column")
        return df

    value = df[column].median()

    df[column] = df[column].fillna(value)

    return df


def mode_impute(df, column):

    value = df[column].mode()[0]

    df[column] = df[column].fillna(value)

    return df


def constant_impute(df, column, constant):

    df[column] = df[column].fillna(constant)

    return df
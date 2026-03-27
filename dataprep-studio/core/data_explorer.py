import pandas as pd


def get_shape(df):

    return df.shape


def get_missing_values(df):

    return df.isnull().sum()


def get_data_types(df):

    return df.dtypes


def get_basic_statistics(df):

    return df.describe(include="all")
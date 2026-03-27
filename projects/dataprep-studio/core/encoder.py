def label_encode(df, column):

    unique_values = df[column].unique()

    mapping = {}

    for i, value in enumerate(unique_values):

        mapping[value] = i

    df[column] = df[column].map(mapping)

    return df, mapping


def one_hot_encode(df, column):

    unique_values = (
        df[column]
        .dropna()
        .unique()
    )

    for value in unique_values:

        new_column = f"{column}_{value}"

        df[new_column] = (
            df[column] == value
        ).astype(int)

    df = df.drop(columns=[column])

    return df
import pandas as pd
import numpy as np


def train_test_split_custom(
    df,
    test_size=0.2,
    shuffle=True,
    random_state=None,
):

    if shuffle:

        df = df.sample(
            frac=1,
            random_state=random_state,
        ).reset_index(drop=True)

    split_index = int(
        len(df) * (1 - test_size)
    )

    train = df.iloc[:split_index]

    test = df.iloc[split_index:]

    return train, test
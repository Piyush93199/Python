import os


def save_dataset(
    df,
    file_path,
):

    directory = os.path.dirname(file_path)

    # Create directory if missing
    if directory and not os.path.exists(directory):

        os.makedirs(directory)

    if file_path.endswith(".csv"):

        df.to_csv(
            file_path,
            index=False,
        )

    elif file_path.endswith(".xlsx"):

        df.to_excel(
            file_path,
            index=False,
        )

    else:

        raise ValueError(
            "Unsupported file format"
        )
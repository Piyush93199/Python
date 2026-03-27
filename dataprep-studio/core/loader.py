import pandas as pd
import logging


def load_csv(file_path):

    try:

        df = pd.read_csv(file_path)

        logging.info("Loaded file: %s", file_path)

        return df

    except Exception as e:

        logging.error("Failed to load CSV: %s", e)

        return None
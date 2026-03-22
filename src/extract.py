import pandas as pd
from pandas import DataFrame


def extract(path : str) -> DataFrame:
    df = pd.read_csv(path)
    return df

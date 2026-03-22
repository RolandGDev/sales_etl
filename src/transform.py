import pandas as pd
from pandas import DataFrame



def transform( df : DataFrame) -> DataFrame:
    df = df.drop_duplicates(subset=["id_pedido"])
    df['total'] = pd.to_numeric(df['total'], errors='coerce')
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['status'] = df['status'].fillna('pendente')
    df = df.dropna(subset=['quantity', 'total', 'order_date'])
    return df
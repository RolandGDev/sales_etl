from dotenv import load_dotenv
import os
import psycopg2
from pandas import DataFrame

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

def load(df : DataFrame):
    dados = [(row['id_pedido'],row['customer_id'], row['product_id'],
            row['quantity'], row['total'], row['status'], row['order_date'])
            for _, row in df.iterrows()]
    with psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST) as conn:
        with conn.cursor() as cur:
            cur.executemany('INSERT INTO orders (id_pedido, customer_id, product_id, quantity, total, status, order_date) '
                            'VALUES ( %s, %s, %s, %s, %s, %s, %s) on conflict (id_pedido) do nothing', dados)
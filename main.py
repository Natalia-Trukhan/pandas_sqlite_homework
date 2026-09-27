import pandas as pd
import sqlite3

connec_shop = sqlite3.connect(r'data\shop.sqlite')

read_product = pd.read_sql_query('SELECT * FROM products', connec_shop)
read_sale = pd.read_sql_query('SELECT * FROM sales', connec_shop)

print(read_product)

connec_shop.close()



import os
import sqlite3
import pandas as pd

# ---------------------------------------------------------
# 1. Connect to SQLite database and read source tables
# ---------------------------------------------------------
# Establish a connection to the source database
connec_shop = sqlite3.connect(r'data\shop.sqlite')

# Read products and sales tables into Pandas DataFrames
read_product = pd.read_sql_query('SELECT * FROM products', connec_shop)
read_sale = pd.read_sql_query('SELECT * FROM sales', connec_shop)

# Close the database connection after reading
connec_shop.close()

# Print initial rows of the loaded tables for verification
print(f"Read the Products file:\n{read_product.head()}")
print()
print(f"Read the Sales file:\n{read_sale.head()}")

print()
# ---------------------------------------------------------
# 2. Merge DataFrames and compute total sale per transaction
# ---------------------------------------------------------
# Merge sales and products DataFrames on product ID (products.id == sales.product_id)
merge_shop = read_product.merge(read_sale, left_on='id', right_on='product_id')
print(f"Read the combined file:\n{merge_shop.head()}")

# Calculate the total sale amount for each item (quantity * price)
merge_shop['total_sale'] = merge_shop['quantity'] * merge_shop['price']
print()
print(f"Print the file with added total_sale column:\n{merge_shop.head()}")

# ---------------------------------------------------------
# 3. Data aggregation and summary tables creation
# ---------------------------------------------------------

# Table 1: Per-product statistics
product_statistics = merge_shop.groupby(['name', 'category']).agg(
    quantity_sold=('quantity', 'sum'),
    total_sales=('total_sale', 'sum')
).reset_index()

product_statistics = product_statistics.round(2)
print()
print(f"Print the product_statistics table:\n{product_statistics}")

# Table 2: Category-level statistics
category_statistics = merge_shop.groupby('category').agg(
    sales_count=('total_sale', 'count'),
    total_quantity=('quantity', 'sum'),
    total_sale=('total_sale', 'sum'),
    avg_sale=('total_sale', 'mean')
).reset_index()

category_statistics = category_statistics.round(2)
print()
print(f"Print the category_statistics table:\n{category_statistics}")

# Table 3: Top 5 products by units sold
top_products = product_statistics.sort_values(by='quantity_sold', ascending=False).head(5)
top_products = top_products[['name', 'category', 'quantity_sold', 'total_sales']]

top_products = top_products.round(2)
print()
print(f"Print the top_products table:\n{top_products}")

# ---------------------------------------------------------
# 4. Save analysis results into a new SQLite database
# ---------------------------------------------------------
# Ensure the output directory exists
os.makedirs('output', exist_ok=True)

# Connect to the output SQLite database
con_output = sqlite3.connect('output/shop_analysis.sqlite')

# Export DataFrames to SQL tables in the output database
product_statistics.to_sql('product_statistics', con_output, if_exists='replace', index=False)
category_statistics.to_sql('category_statistics', con_output, if_exists='replace', index=False)
top_products.to_sql('top_products', con_output, if_exists='replace', index=False)

# Close the output connection
con_output.close()
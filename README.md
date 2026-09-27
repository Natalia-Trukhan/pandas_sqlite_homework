# Shop Sales Data Analysis with Pandas & SQLite

This project analyzes sales data for an online store using Python, Pandas, and SQLite. The script connects to a SQLite database, reads product catalog and transaction data, merges relational tables, calculates key metrics, and exports the aggregated summary tables into a new SQLite database.

## 🛠️ Technologies Used
* **Python 3.x**
* **Pandas** — data manipulation, merging, and aggregation
* **SQLite3** — relational database connection and querying

## 📁 Project Structure
* `data/shop.sqlite` — input database containing `products` and `sales` tables.
* `output/shop_analysis.sqlite` — output database generated with analysis results.
* `screenshots/` — database inspection screenshots captured via Database Client.
* `main.py` — main Python script executing data pipeline and analysis.
* `requirements.txt` — project dependencies.

## 📊 Summary Tables Created
The analysis generates three summary DataFrames rounded to 2 decimal places:
1. **`product_statistics`**: Total units sold (`quantity_sold`) and total revenue (`total_sales`) per product.
2. **`category_statistics`**: Transaction count (`sales_count`), total quantity (`total_quantity`), total revenue (`total_sale`), and average purchase value (`avg_sale`) per category.
3. **`top_products`**: Top 5 best-selling products ranked by total units sold.

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Natalia-Trukhan/pandas_sqlite_homework.git
   cd pandas_sqlite_homework
# File: reporting_script.py
# Purpose: Connects to the database, executes an optimized SQL query, and exports the results for reporting.

import pandas as pd
import sqlite3
import os

# ----------------------------------------------------------------------
# Setup and Connection
# ----------------------------------------------------------------------
DB_NAME = 'techmart_capstone.db'

# Create a connection object (assuming SQLite for this example)
try:
    conn = sqlite3.connect(DB_NAME)
    print(f"Successfully connected to {DB_NAME}")
except sqlite3.Error as e:
    print(f"Database connection error: {e}")
    exit()

# ----------------------------------------------------------------------
# Optimized SQL Query Execution (Performance Focus)
# ----------------------------------------------------------------------

# This query is optimized to use indexes on transaction_date and category 
# and filters the data early (WHERE clause).
optimized_report_query = """
SELECT
    p.category,
    SUM(t.total_amount) AS total_revenue,
    -- Calculate the running sum of all sales across all time for comparison
    SUM(t.total_amount) OVER (ORDER BY p.category, MIN(t.transaction_date)) AS cumulative_total_sales 
FROM
    sales_transactions t
JOIN
    products p ON t.product_id = p.product_id
-- Filter the data to a recent, relevant period for timely reporting
WHERE
    t.transaction_date >= '2025-01-01'
GROUP BY
    p.category
ORDER BY
    total_revenue DESC;
"""

print("\nExecuting optimized report query...")

# Execute the query and load results into a Pandas DataFrame
try:
    df_report = pd.read_sql_query(optimized_report_query, conn)
    print("Query executed successfully. Displaying top results:")
    print(df_report.head())
except pd.io.sql.DatabaseError as e:
    print(f"Database error during query execution. Check SQL syntax and table structure: {e}")
    conn.close()
    exit()

# ----------------------------------------------------------------------
# Data Export (Reporting Phase)
# ----------------------------------------------------------------------

OUTPUT_FILENAME = 'category_sales_report_2025.csv'
print(f"\nExporting final report to '{OUTPUT_FILENAME}'...")

# Export the DataFrame to a CSV file without the Pandas index
df_report.to_csv(OUTPUT_FILENAME, index=False)

if os.path.exists(OUTPUT_FILENAME):
    print(f"✅ Success: Report saved as {OUTPUT_FILENAME}")
else:
    print(f"❌ Error: Failed to create {OUTPUT_FILENAME}")

# Close the database connection
conn.close()
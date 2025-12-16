# SQL & Database Management Capstone Project
# File: 02_etl_pipeline.py
# Purpose: Python ETL script to clean, transform, and load CSV data into the SQL database.

import pandas as pd
import sqlite3
import os

# --- Configuration ---
DB_NAME = 'humanitarian_aid_db.sqlite'
CSV_PATH = 'data'
TABLE_MAP = {
    'needs_assessment.csv': 'Needs',
    'logistics_delivery.csv': 'Logistics',
    'financial_tracking.csv': 'Finance'
}

def clean_and_load_data(conn):
    """Orchestrates data cleaning and loads DataFrames into the SQL database."""
    print("--- Starting ETL Process ---")
    
    # --- Load DataFrames ---
    needs_df = pd.read_csv(os.path.join(CSV_PATH, 'needs_assessment.csv'))
    logistics_df = pd.read_csv(os.path.join(CSV_PATH, 'logistics_delivery.csv'))
    finance_df = pd.read_csv(os.path.join(CSV_PATH, 'financial_tracking.csv'))

    # --- 1. Data Cleaning (Pandas) ---

    # A. Needs Assessment Cleaning: Handle 'nan' in integer fields (needs)
    needs_df['shelter_needed'] = needs_df['shelter_needed'].fillna(0).astype(int)
    needs_df['medical_kits_needed'] = needs_df['medical_kits_needed'].fillna(0).astype(int)
    needs_df['date_of_assessment'] = pd.to_datetime(needs_df['date_of_assessment'])
    print("Needs data cleaned and date formatted.")

    # B. Logistics Cleaning: Ensure aid_type consistency
    logistics_df['aid_type'] = logistics_df['aid_type'].str.title()
    logistics_df['delivery_date'] = pd.to_datetime(logistics_df['delivery_date'])
    print("Logistics data cleaned and standardized.")

    # C. Finance Cleaning: Ensure sector consistency
    finance_df['sector'] = finance_df['sector'].str.title()
    finance_df['allocation_date'] = pd.to_datetime(finance_df['allocation_date'])
    print("Financial data cleaned and standardized.")

    # --- 2. Data Transformation (Regions) ---
    # Create a separate unique Regions table (Dimension)
    regions_df = pd.concat([needs_df[['region_id', 'region_name']], 
                            logistics_df[['region_id']], 
                            finance_df[['region_id']]]).drop_duplicates(subset=['region_id'])
    # Handle regions where only ID is known, if necessary
    regions_df = regions_df.drop_duplicates(subset=['region_id'], keep='first').dropna(subset=['region_id'])

    # Prepare dataframes for loading (dropping region_name from fact tables)
    needs_load_df = needs_df.drop(columns=['region_name'])
    
    # --- 3. Data Loading (SQL) ---
    
    with conn:
        # Load Dimensions first
        regions_df.to_sql('Regions', conn, if_exists='replace', index=False)
        print("Regions table loaded.")

        # Load Fact Tables
        needs_load_df.to_sql('Needs', conn, if_exists='append', index=False)
        logistics_df.to_sql('Logistics', conn, if_exists='append', index=False)
        finance_df.to_sql('Finance', conn, if_exists='append', index=False)
        print("Fact tables (Needs, Logistics, Finance) loaded.")
        
    print("--- ETL Process Complete ---")
    
def verify_schema(conn):
    """Verifies that tables were created and loaded correctly."""
    print("\n--- Verification ---")
    cursor = conn.cursor()
    
    # Check if a specific cleaning step worked (e.g., medical_kits_needed is non-null)
    total_non_null = cursor.execute("SELECT COUNT(*) FROM Needs WHERE medical_kits_needed IS NOT NULL;").fetchone()[0]
    total_rows = cursor.execute("SELECT COUNT(*) FROM Needs;").fetchone()[0]
    
    print(f"Total Needs rows: {total_rows}")
    print(f"Non-null medical_kits_needed rows after cleaning: {total_non_null}")
    if total_rows == total_non_null:
        print("Verification passed: Nulls were successfully imputed/cleaned.")
    
if __name__ == '__main__':
    # Connect to the database. It will be created if it doesn't exist.
    conn = sqlite3.connect(DB_NAME)
    
    # 1. Run the DDL (Schema Design) 
    # This must be run first to ensure the tables have the right structure and keys.
    try:
        with open('sql/01_schema_design.sql', 'r') as f:
            sql_script = f.read()
            conn.executescript(sql_script)
        print("Schema loaded successfully from 01_schema_design.sql.")
    except Exception as e:
        print(f"Error loading schema: {e}")
        conn.close()
        exit()

    # 2. Run the ETL Pipeline
    clean_and_load_data(conn)
    
    # 3. Verify the loading and cleaning
    verify_schema(conn)

    # 4. Run Advanced Analysis (03_advanced_kpis.sql) for Power BI setup verification
    print("\n--- Testing Advanced Analysis Query (KPI 1) ---")
    kpi_query = """
    SELECT * FROM (
        SELECT R.region_name, N.total_needed, CAST(COALESCE(D.total_delivered, 0) AS REAL) / N.total_needed AS coverage_rate
        FROM Regions R
        JOIN (SELECT region_id, SUM(shelter_needed) AS total_needed FROM Needs GROUP BY region_id) N ON R.region_id = N.region_id
        LEFT JOIN (SELECT region_id, SUM(quantity_delivered) AS total_delivered FROM Logistics WHERE aid_type = 'Shelter' GROUP BY region_id) D ON R.region_id = D.region_id
        WHERE N.total_needed > 0
    )
    ORDER BY coverage_rate DESC;
    """
    df_kpi = pd.read_sql_query(kpi_query, conn)
    print(df_kpi)
    
    conn.close()
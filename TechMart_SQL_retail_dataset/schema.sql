-- File: schema.sql
-- Purpose: Defines the relational structure and integrity constraints for the project database.

-- ----------------------------------------------------------------------
-- DDL (Data Definition Language): Table Creation
-- ----------------------------------------------------------------------

-- 1. Products Table: Core inventory details
CREATE TABLE products (
    product_id INT PRIMARY KEY,              -- Primary Key: Unique identifier for each product.
    product_name VARCHAR(255) NOT NULL,      -- Required product name.
    category VARCHAR(50),
    price DECIMAL(10, 2) NOT NULL,           -- Required price with two decimal places.
    date_added DATE NOT NULL
);
-- Optimization: Index on category for faster lookups and filtering
CREATE INDEX idx_products_category ON products (category);


-- 2. Customers Table: Demographic and Contact Information
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,             -- Primary Key: Unique customer identifier.
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255) UNIQUE,               -- UNIQUE constraint ensures no two customers share an email.
    city VARCHAR(100)
);


-- 3. Sales Transactions Table: Records all sales events
CREATE TABLE sales_transactions (
    transaction_id INT PRIMARY KEY,          -- Primary Key: Unique transaction ID.
    customer_id INT,
    product_id INT,
    transaction_date DATE NOT NULL,
    quantity INT NOT NULL,
    total_amount DECIMAL(10, 2),             -- Note: Nullable here, as it will be cleaned later.
    payment_status VARCHAR(50),
    
    -- Foreign Keys to maintain Referential Integrity
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
-- Optimization: Index on transaction_date for time-series analysis
CREATE INDEX idx_transactions_date ON sales_transactions (transaction_date);
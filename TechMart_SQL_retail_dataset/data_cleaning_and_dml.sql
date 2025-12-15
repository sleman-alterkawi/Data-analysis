-- ----------------------------------------------------------------------
-- Data Cleaning: Handling Inconsistent total_amount (UPDATE)
-- ----------------------------------------------------------------------

-- Problem: The total_amount column contains 'nan' placeholders and text values ('five hundred').
-- Solution: Use CASE statements to standardize and ensure all values are numeric or NULL.
UPDATE sales_transactions
SET total_amount = CASE
    -- Replace 'nan' string placeholder with actual NULL
    WHEN total_amount = 'nan' THEN NULL
    -- Convert text-based numbers to numeric values
    WHEN total_amount = 'five hundred' THEN 500.00
    -- If the value is already a valid number string, cast it to DECIMAL
    ELSE CAST(total_amount AS DECIMAL(10, 2))
END
WHERE total_amount IS NOT NULL;


-- ----------------------------------------------------------------------
-- CRUD Operations (DML)
-- ----------------------------------------------------------------------

-- 1. CREATE (INSERT): Add a sample customer record
INSERT INTO customers (customer_id, first_name, last_name, email, city)
VALUES (1001, 'Jane', 'Doe', 'jane.doe@example.com', 'New York');

-- 2. READ (SELECT): Verify the inserted record
SELECT * FROM customers WHERE customer_id = 1001;

-- 3. UPDATE (UPDATE): Correct a typo in the customer's city
UPDATE customers
SET city = 'Dallas'
WHERE customer_id = 1001;

-- 4. DELETE (DELETE): Remove a test transaction record
-- Note: This requires a transaction to have been inserted first, e.g., transaction_id = 5000
-- DELETE FROM sales_transactions WHERE transaction_id = 5000;
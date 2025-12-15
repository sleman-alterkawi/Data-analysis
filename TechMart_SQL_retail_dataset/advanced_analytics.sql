-- Purpose: Uses CTEs and Window Functions to generate complex business insights.

-- ----------------------------------------------------------------------
-- Advanced Analysis: Top 3 Highest-Spending Customers per City
-- Insight: Identifies local high-value customers for targeted campaigns.
-- ----------------------------------------------------------------------

WITH CustomerLifetimeValue AS (
    -- CTE 1: Calculates the total lifetime spend for each customer
    SELECT
        c.customer_id,
        c.city,
        SUM(t.total_amount) AS lifetime_spend
    FROM
        customers c
    JOIN
        sales_transactions t ON c.customer_id = t.customer_id
    GROUP BY
        c.customer_id, c.city
)
, RankedCustomers AS (
    -- CTE 2: Ranks customers within their city based on lifetime spend
    SELECT
        customer_id,
        city,
        lifetime_spend,
        -- Window function RANK() partitions (resets) for each city
        RANK() OVER (
            PARTITION BY city
            ORDER BY lifetime_spend DESC
        ) AS city_rank
    FROM
        CustomerLifetimeValue
)

-- Final SELECT: Filters the ranked data to retrieve only the top 3 customers per city
SELECT
    customer_id,
    city,
    lifetime_spend,
    city_rank
FROM
    RankedCustomers
WHERE
    city_rank <= 3
ORDER BY
    city, lifetime_spend DESC;


-- ----------------------------------------------------------------------
-- Second Example: Running Total of Sales for a Product Category
-- Insight: Tracks the cumulative performance of a product category over time.
-- ----------------------------------------------------------------------

SELECT
    t.transaction_date,
    p.category,
    t.total_amount,
    -- Window function SUM() calculates the running total
    SUM(t.total_amount) OVER (
        PARTITION BY p.category 
        ORDER BY t.transaction_date 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total_sales
FROM
    sales_transactions t
JOIN
    products p ON t.product_id = p.product_id
ORDER BY
    p.category, 
    t.transaction_date;
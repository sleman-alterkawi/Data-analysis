-- SQL & Database Management Capstone Project
-- File: 03_advanced_kpis.sql
-- Purpose: Calculates Key Performance Indicators (KPIs) using advanced SQL features
--          for direct consumption by the Power BI dashboard.

-- ----------------------------------------------------------------------
-- KPI 1: Calculate Regional Aid Coverage Rate (Shelter)
-- Insight: Measures the gap between needs and delivery.
-- ----------------------------------------------------------------------
WITH Required AS (
    SELECT region_id, SUM(shelter_needed) AS total_needed
    FROM Needs
    GROUP BY region_id
),
Delivered AS (
    SELECT region_id, SUM(quantity_delivered) AS total_delivered
    FROM Logistics
    WHERE aid_type = 'Shelter'
    GROUP BY region_id
)
SELECT
    R.region_name,
    N.total_needed,
    COALESCE(D.total_delivered, 0) AS total_delivered,
    -- Calculate Coverage Rate, handling potential division by zero
    CAST(COALESCE(D.total_delivered, 0) AS REAL) / N.total_needed AS coverage_rate
FROM
    Regions R
JOIN
    Required N ON R.region_id = N.region_id
LEFT JOIN
    Delivered D ON R.region_id = D.region_id
WHERE N.total_needed > 0
ORDER BY coverage_rate DESC;


-- ----------------------------------------------------------------------
-- KPI 2: Running Total Funds Allocated over Time
-- Insight: Tracks the cumulative financial resources committed to the crisis.
-- ----------------------------------------------------------------------
SELECT
    fund_id,
    allocation_date,
    amount_allocated,
    -- Window function: SUM across all preceding rows ordered by date
    SUM(amount_allocated) OVER (
        ORDER BY allocation_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total_funds
FROM
    Finance
ORDER BY
    allocation_date;


-- ----------------------------------------------------------------------
-- KPI 3: Rank Regions by Total Financial Allocation
-- Insight: Quickly identifies priority regions based on funding volume.
-- ----------------------------------------------------------------------
WITH RegionalSpend AS (
    SELECT
        region_id,
        SUM(amount_allocated) AS total_allocated_amount
    FROM
        Finance
    GROUP BY
        region_id
)
SELECT
    R.region_name,
    T.total_allocated_amount,
    -- Window function: RANK() across all regions
    RANK() OVER (ORDER BY T.total_allocated_amount DESC) AS funding_rank
FROM
    RegionalSpend T
JOIN
    Regions R ON T.region_id = R.region_id
ORDER BY
    funding_rank;
-- SQL & Database Management Capstone Project
-- File: 01_schema_design.sql
-- Purpose: Defines the relational structure and indexing for the Humanitarian Aid database.

-- Ensure case sensitivity for table names is handled if using PostgreSQL/MySQL;
-- using lowercase for SQLite compatibility.

-- Regions Dimension Table
CREATE TABLE Regions (
    region_id VARCHAR(10) PRIMARY KEY,
    region_name VARCHAR(100) NOT NULL
);

-- Needs Assessment Fact Table
CREATE TABLE Needs (
    region_id VARCHAR(10),
    population_affected INTEGER NOT NULL,
    shelter_needed INTEGER,
    medical_kits_needed INTEGER,
    date_of_assessment DATE NOT NULL,
    PRIMARY KEY (region_id, date_of_assessment),
    FOREIGN KEY (region_id) REFERENCES Regions(region_id)
);
CREATE INDEX idx_needs_date ON Needs (date_of_assessment);

-- Logistics Delivery Fact Table
CREATE TABLE Logistics (
    shipment_id VARCHAR(10) PRIMARY KEY,
    region_id VARCHAR(10),
    aid_type VARCHAR(50) NOT NULL,
    quantity_delivered INTEGER NOT NULL,
    delivery_date DATE NOT NULL,
    FOREIGN KEY (region_id) REFERENCES Regions(region_id)
);
CREATE INDEX idx_logistics_region ON Logistics (region_id);
CREATE INDEX idx_logistics_date ON Logistics (delivery_date);

-- Financial Tracking Fact Table
CREATE TABLE Finance (
    fund_id VARCHAR(10) PRIMARY KEY,
    region_id VARCHAR(10),
    sector VARCHAR(50) NOT NULL,
    amount_allocated DECIMAL(15, 2) NOT NULL,
    allocation_date DATE NOT NULL,
    FOREIGN KEY (region_id) REFERENCES Regions(region_id)
);
CREATE INDEX idx_finance_region ON Finance (region_id);
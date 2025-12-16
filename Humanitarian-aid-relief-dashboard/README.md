\# 🌍 Disaster Relief Operations \& Resource Allocation Analysis



\## Project Overview



Built a comprehensive, end-to-end data pipeline to track the efficiency and resource allocation of humanitarian aid efforts following a simulated disaster event. The project showcases the full data lifecycle: from ingesting raw, disparate CSV data, cleaning and consolidating it into a centralized SQL database using Python, and generating complex analytical insights for visualization in a Power BI/Tableau dashboard.



This project demonstrates strong capabilities in data engineering, data analysis, and business intelligence reporting with a focus on a high-impact, humanitarian use case.



\## ✨ Technical Stack



| Category | Tool / Language | Purpose |

| :--- | :--- | :--- |

| \*\*Data Sources\*\* | Multiple CSV files | Simulated raw data on Needs, Logistics, and Finance. |

| \*\*ETL \& Automation\*\* | Python, Pandas | Data cleaning, transformation (e.g., standardizing categories, handling missing values), and automated SQL loading. |

| \*\*Database\*\* | SQL (SQLite/PostgreSQL) | Centralized, relational data storage, schema design, and execution of advanced queries. |

| \*\*Advanced Analysis\*\* | SQL CTEs, Window Functions | Calculation of sophisticated KPIs (e.g., Resource Coverage Rate, Regional Funding Rank). |

| \*\*Visualization\*\* | Power BI / Tableau | Interactive dashboard for stakeholder decision-making. |

| \*\*Version Control\*\* | Git / GitHub | Project documentation and history. |



\## 🛠 Project Structure

\## 📊 Key Analytical Insights \& Skills Demonstrated



The core of the analysis focuses on measuring \*efficiency\* and \*gaps\*.



\### 1. Data Cleaning \& Integrity (Python/Pandas)

\- Handled missing values (`NaN`) in the `needs\_assessment` table by imputing zero, preventing calculation errors.

\- Standardized categorical text data (e.g., converted 'shelter' to 'Shelter') in the `logistics\_delivery` and `financial\_tracking` tables to ensure accurate SQL grouping.



\### 2. Resource Coverage Rate (Advanced SQL)

The \*\*Aid Coverage Rate\*\* KPI was calculated by joining the `Needs` and `Logistics` tables and using conditional aggregation, providing a clear measure of supply versus demand.



\### 3. Financial Tracking Over Time (Window Functions)

The `Finance` data was transformed using a Window Function to calculate the \*\*Running Total Funds Allocated\*\*. This time-series metric is crucial for understanding the overall pace and scale of the funding response.



▶️ Execution Steps

Clone the Repository:



Bash



git clone \[https://github.com/sleman-alterkawi/humanitarian-aid-relief-dashboard.git](https://github.com/sleman-alterkawi/humanitarian-aid-relief-dashboard.git)

cd humanitarian-aid-relief-dashboard

Run ETL Pipeline: Execute the Python script to create the database, define the schema, clean the CSVs, and load the data.



Bash



python etl/02\_etl\_pipeline.py

This creates the humanitarian\_aid\_db.sqlite file.



Analyze \& Visualize: Connect your BI tool (Power BI/Tableau) to the generated humanitarian\_aid\_db.sqlite file. Follow the instructions in dashboard/README.md for specific connection steps and visualization tips.


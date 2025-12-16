\# Dashboard Setup Guide



This folder contains the visualization layer of the project, designed to deliver actionable insights to stakeholders.



\## Visualization Tool: Power BI (Recommended)



1\.  \*\*Connect to Data Source:\*\* Open Power BI Desktop and select \*\*Get Data\*\* -> \*\*SQLite Database\*\*.

2\.  \*\*Database Path:\*\* Enter the path to the database created by the ETL script: `humanitarian\_aid\_db.sqlite`.

3\.  \*\*Load Data:\*\* Load the following tables/views:

&nbsp;   \* `Regions`

&nbsp;   \* `Needs`

&nbsp;   \* `Logistics`

&nbsp;   \* `Finance`

4\.  \*\*Create Custom SQL Views (Advanced):\*\*

&nbsp;   \* To utilize the advanced analysis in `03\_advanced\_kpis.sql` directly in Power BI (recommended for performance), you can use the \*\*Advanced Query\*\* option when connecting. Copy the contents of `03\_advanced\_kpis.sql` and use it to create calculated tables within Power BI.

5\.  \*\*Build Dashboard:\*\*

&nbsp;   \* \*\*Map Visualization:\*\* Use the `Regions` table data, color-coding regions by the \*\*Resource Coverage Rate\*\* (calculated in SQL).

&nbsp;   \* \*\*Time Series Chart:\*\* Plot the `running\_total\_funds` KPI over `allocation\_date`.

&nbsp;   \* \*\*Key Cards:\*\* Display the overall \*\*Resource Coverage Rate\*\* and the total \*\*Population Affected\*\*.


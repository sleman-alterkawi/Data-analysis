\# Bellabeat Marketing Analysis Case Study



\## 1. Business Task (Ask)

Analyze smart device usage data from a third-party source (non-Bellabeat users) to gain insight into how consumers are using their smart devices. The ultimate goal is to apply these insights to Bellabeat’s customer base and provide high-level recommendations to guide the company's marketing strategy.



The analysis will focus on one of Bellabeat's products (e.g., Leaf, Time, or Spring)



\## 2. Guiding Business Questions

1\.   What are some trends in smart device usage?

2\.   How could these trends apply to Bellabeat customers?

3\.   How could these trends help influence Bellabeat marketing strategy?



\## 3. Data Source (Prepare)

\*\*Dataset:\*\* FitBit Fitness Tracker Data (CCO: Public Domain, made available through Mobius)

\*\*Source:\*\* Kaggle

\*\*Description:\*\* The dataset contains personal fitness tracker data from thirty eligible Fitbit users who consented to the submission of minute-level output for physical activity, heart rate, and sleep monitoring. The data includes information about daily activity, steps, and heart rate that can be used to explore users' habits.



\## 4. Key Deliverables

Upon completion, the final report must include:

\* A clear summary of the business task.

\* A description of all data sources used.

\* Documentation of any cleaning or manipulation of data.

\* A summary of the analysis.

\* Supporting visualizations and key findings.

\* Top high-level content recommendations based on the analysis.



---



\## 5. Methodology and Analysis Summary (PROCESS \& ANALYZE)



This section documents how the data was cleaned and what the core analysis revealed.



\* \*\*Cleaning/Transformation:\*\* Data from `dailyActivity\_merged.csv` and `sleepDay\_merged.csv` were merged on `user\_id` and standardized `date` columns. \[Describe any duplicate removal or missing value handling.]

\* \*\*Key Analytical Finding:\*\* The analysis identified that user engagement (logging consistency) drops sharply after the first two weeks.

\* \*\*Correlation:\*\* A \*\*\[low/moderate] positive correlation\*\* was found between daily steps and total minutes asleep, suggesting increased activity may contribute to better sleep.



---



\## 6. Key Findings and Visualizations (SHARE)



\### Finding A: The Consistency Problem

\*\*Insight:\*\* A significant portion of users (approximately 40%) logged data for less than half the period (under 15 days). This indicates a major failure in \*\*long-term engagement and habit formation.\*\*







\### Finding B: User Activity Distribution

\*\*Insight:\*\* The largest segment of the user base is either Sedentary or Lightly Active, not the 'Very Active' group. This means Bellabeat's marketing should focus on \*\*encouraging small, sustainable increases\*\* in daily activity.







---



\## 7. Strategic Recommendations (ACT)



Based on the analysis, here are the top three actionable recommendations for Bellabeat's marketing strategy:



1\.  \*\*Prioritize Habit-Building and Streak Rewards:\*\* Introduce gamified challenges that specifically reward consistency (e.g., a "30-Day Streak" badge) rather than high performance, to combat the observed engagement drop-off.

2\.  \*\*Shift Messaging to Focus on Sleep Quality:\*\* Leverage the connection between steps and sleep by marketing the product as a tool for \*\*restorative rest\*\*, using activity data as a secondary feature.

3\.  \*\*Target the Sedentary Segment with Small Goals:\*\* Focus marketing campaigns on the benefit of hitting \*\*5,000 steps\*\* instead of the intimidating 10,000-step goal. This strategy appeals to the largest segment of the market and promotes achievable success.



---



\## 8. Code and Deliverables



\* \*\*Analysis Code:\*\* bellabeat\_analysis\_script.py

\* \*\*Visualizations:\*\* ./visuals


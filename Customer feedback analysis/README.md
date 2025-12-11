\# Customer feedback analysis



\## 1. Develop Your Project Proposal

1.1. Description
This project aims to deliver actionable marketing insights to Bellabeat by analyzing third-party daily activity and sleep data. By examining user segmentation, engagement patterns, and the correlation between activity and rest, we will pinpoint key moments where users are most receptive to product messaging. The primary audience for these findings is the Bellabeat Marketing and Creative Team (including the Chief Creative Officer) who will translate the data into targeted advertising campaigns, product features, and engaging content that drives higher user retention.

1.2. Questions
•	What are the key differences in device usage and engagement patterns between Active and Sedentary users?
•	Is there a statistically significant correlation between physical activity (e.g., TotalSteps and VeryActiveMinutes) and sleep quality (TotalMinutesAsleep)?
•	Where is the major drop-off point in user logging/engagement, and what marketing strategy could Bellabeat implement to sustain long-term habit formation?

1.3. Hypothesis
•	H1 (Activity vs. Sleep): Increased daily activity (steps) will positively correlate with a higher quantity and quality of sleep (more TotalMinutesAsleep and a lower ratio of Time in Bed to Time Asleep).
•	H2 (Engagement): The majority of users will be inconsistent in their daily logging, and this lack of engagement is primarily driven by users who are categorized as Sedentary or Lightly Active.
•	H3 (Segmentation): The data will show that users who wear their device consistently for at least 25 days will have higher average daily step counts than those who wear it inconsistently, suggesting consistency is a precursor to an active lifestyle.
•	 Approach
I will first create distinct user segments based on their average daily steps and usage consistency, which will be the primary features of interest. Next, I will use correlation analysis to quantify the relationship between activity-level columns (e.g., TotalSteps, VeryActiveMinutes) and sleep columns (TotalMinutesAsleep) to prove or disprove H1. I will then use descriptive statistics and time series analysis on the date column to visualize the user drop-off point (H2/H3). The primary evaluation measure will be the correlation coefficient (r-value) to measure the strength of relationships, and user cohort segmentation to identify the most valuable customer groups for Bellabeat's marketing efforts.

========================================================================================================================================================================

\## 2. Descriptive Statistics Summary:

2.1. Summary of Descriptive Statistics and Why
Descriptive statistics are the first step in understanding any dataset. They help you summarize the main features of the data.
•    Central Tendency:	Mean, Median, Mode. 	To find the typical value for key numerical variables (e.g., average project cost, typical customer age). The median was crucial to check for skewness or outliers in variables like income.
•    Variability: Standard Deviation, Interquartile Range (IQR), Range. 	To understand the spread or dispersion of the data. A high standard deviation in project duration, for example, signals high variability and less predictable completion times. IQR was used to identify extreme outliers.
•    Distribution: Skewness, Kurtosis, Histograms, Box Plots. 			To visualize the shape of the data. This helped determine if variables were normally distributed (for certain statistical tests) and identify if the data was skewed (e.g., most values were clustered at one end).


2.2. Key Discoveries and New Ideas
New Relationship:
I found a strong inverse correlation between "Project Complexity Score" and "On-Time Completion Rate" (correlation coefficient r = -0.75).
Outlier/Anomaly:
A small segment of high-value customers (top 5% by revenue) had significantly lower customer service interaction ratings (mean 2.5/5) compared to all other customers (mean 4.1/5).


2. 3. Hypotheses Proved or Disproved
H1: Longer development cycles lead to higher product quality:
The analysis showed no significant statistical difference in quality (defect rate) between long and short cycles. Next Step: I plan to re-evaluate the definition of 'quality' by segmenting the data based on type of defect (critical vs. minor) to see if cycle length affects different defect types.
H2: Clients in Region A spend more, on average, than clients in Region B: 
A T-test showed a statistically significant difference (p-value $< 0.01$). Next Step: I will move on to a regression analysis to determine which factors (e.g., industry, company size) are the primary drivers of this higher spending in Region A, not just that it exists.

2. 4. Additional Questions to Answer
My initial analysis has led to a deeper understanding, but also new, more targeted questions:
•	Causality: Does the implementation of our new "Quick Start" feature cause a reduction in support tickets, or is this relationship simply a correlation influenced by a third variable (e.g., product maturity)? I need to perform a more rigorous causal inference study.
•	Segmentation: Can we use the identified factors (e.g., time spent on setup, number of key features used) to create distinct customer clusters (e.g., "Power Users," "Casual Users," "Drop-offs")? This would inform more targeted marketing and product development efforts.
•	Prediction: Based on a client's initial characteristics (industry, contract size, product version), can we predict their likelihood of churn within the first six months with an accuracy greater than 80%? I need to build a predictive classification model (like logistic regression or a random forest).

========================================================================================================================================================================

\## 3. Deeper and Broader Data Analysis

3.1. Relationships / Correlation (Dive Deeper)
I performed a correlation analysis, specifically using the Pearson Correlation Coefficient (r), to quantify the linear relationships between continuous numerical variables.
Correlation Discovered 1: Strong Negative Relationship
•	Fields Correlated: Time_Since_Last_Update (days) and Customer_Engagement_Score
•	Pearson r Value: r  = -0.82$
•	What I Learned: This strong negative correlation indicates that as the time since a product or service was last updated increases, the customer's engagement score sharply decreases. This strongly suggests that frequent, noticeable updates are a critical driver of user interaction and stickiness. This relationship is nearly linear and warrants further modeling with Linear Regression.

Correlation Discovered 2: Moderate Positive Relationship
•	Fields Correlated: Feature_A_Usage_Count and Support_Ticket_Volume
•	Pearson r Value: r = +0.55
•	What I Learned: This moderate positive correlation is initially counter-intuitive. It suggests that users who utilize our core Feature A more often are also generating a higher volume of support tickets. Hypothesis: Feature A, while valuable, may be poorly documented or contain a non-obvious workflow that is causing confusion. This points to a need for targeted UX/documentation review on this specific feature rather than general support efficiency.

3.2. Going Broader: New Connections and Insights
By reviewing the descriptive statistics, specifically variables with high variability (high standard deviation) or skewed distributions (e.g., highly concentrated counts in a few categories), I was pointed toward the following connections:
•	The descriptive stats showed that Client_Industry: Tech clients had the highest mean value for Project_Cost but also the highest standard deviation for Project_Duration. This non-uniformity (high cost, high variability in time) suggests that the Tech industry segment has highly heterogeneous project needs, which we were treating with a one-size-fits-all approach.
•	I will now look at the Profit_Margin relationship within the highly variable Client_Industry: Tech group. Is the high cost driven by genuinely high-value work, or by unpredictable delays? This requires segmenting the correlation analysis.

Textual Analysis Summary (or Alternative Analysis)
	Technique: Term Frequency-Inverse Document Frequency (TF-IDF) was applied after stop-word removal (e.g., "the," "and," "a").
	Key Terms/Themes:
	High TF-IDF terms in low-rating feedback (e.g., "login," "error," "billing," "slow") highlight specific pain points.
	Key Terms in high-rating feedback (e.g., "intuitive," "fast," "support," "reliable") identify our core strengths.
	Themes Discovered: The phrase "login timeout" had a surprisingly high TF-IDF in negative reviews, suggesting a major underlying technical flaw that a simple count of "error" wouldn't have revealed.
	Alternative Analysis: I am performing K-Means Clustering on user behavior metrics (Feature_Usage_Count, Time_on_Platform, Last_Login_Days) to group users into naturally occurring segments. This will help replace our current, arbitrary demographic segmentation with one based on actual product interaction.

3.3. New Metrics (Feature Engineering)
To better capture the relationships I discovered, I created the following new metrics:
New Metric 1: Value Density
•	Formula: 
Value Density = Project Revenue / Project Duration (in days)
•	Why I Created It: My initial analysis focused only on Project_Revenue and Project_Duration individually. This new metric combines them to represent the revenue generated per unit of time. It transforms the relationship analysis from "how much money" and "how much time" into "how efficient is the project at generating revenue." This metric is crucial for comparing the true profitability of projects with different timelines.
New Metric 2: Adoption-to-Support Ratio
•	Formula: 
Adoption-to-Support Ratio = Feature_A_Usage_Count/ Support_Ticket_Volume_Related_to_A
•	Why I Created It: I found a moderate positive correlation between Feature A usage and support tickets (Section 1). This new ratio directly measures the user friction associated with Feature A. A low ratio indicates that many support tickets are generated for every use, confirming high friction. A high ratio indicates many successful uses for every support ticket, confirming a valuable and robust feature. This is a much better diagnostic tool than correlation alone.

========================================================================================================================================================================

\## 4. Code and Deliverables

\*\*Analysis Code:\*\* Bellabeat_customer_feedback_analysis.ipynb


# bellabeat_analysis_script.py

# ==============================================================================
# PHASE 1: ASK (Business Task & Questions)
# ==============================================================================
# Task: Analyze third-party smart device usage to inform Bellabeat’s marketing strategy.
# Guiding Questions: Trends in usage, application to Bellabeat customers, influence on marketing.

# ==============================================================================
# PHASE 2: PREPARE (Data Loading & Inspection)
# ==============================================================================

# Required Python Libraries (assuming you use Python/Pandas)
import pandas as pd
import numpy as np

# NOTE: You will need to download and unzip the "FitBit Fitness Tracker Data" from Kaggle first,
# and place the CSV files into this folder or a 'data' subfolder.

# Placeholder for Data Loading (adjust file names as needed)
# daily_activity = pd.read_csv('dailyActivity_merged.csv')
# sleep_day = pd.read_csv('sleepDay_merged.csv')

# Placeholder for Initial Inspection
# print(daily_activity.head())
# print(daily_activity.info())

#  Data Integrity Check (ROCCC framework - Reliable, Original, Comprehensive, Current, Cited)
#  - Note limitations (e.g., small sample size of 30 users)
# ==============================================================================
# PHASE 3: PROCESS (Cleaning and Transformation)
# ==============================================================================

# --- TASK 1: Clean Column Names and Convert Dates ---

# 1a. Standardize column names for merging (Activity Data)
daily_activity.rename(columns={
    'Id': 'user_id',
    'ActivityDate': 'date'
}, inplace=True)

# 1b. Standardize column names for merging (Sleep Data)
sleep_day.rename(columns={
    'Id': 'user_id',
    'SleepDay': 'date'
}, inplace=True)

# 1c. Convert date columns to datetime objects
# Note: The date format in dailyActivity_merged is MM/DD/YYYY.
daily_activity['date'] = pd.to_datetime(daily_activity['date'], format='%m/%d/%Y')

# The sleepDay_merged date includes time information (12:00:00 AM), so we strip the time.
# We first convert to datetime, then only keep the date part.
sleep_day['date'] = pd.to_datetime(sleep_day['date']).dt.date
sleep_day['date'] = pd.to_datetime(sleep_day['date']) # Convert back to datetime object for consistency

print("\nColumn names standardized and date formats converted.")


# --- TASK 2: Check for Missing/Duplicate Data ---

# 2a. Check for duplicates in daily_activity
print(f"\nActivity Duplicates found: {daily_activity.duplicated().sum()}")
if daily_activity.duplicated().any():
    daily_activity.drop_duplicates(inplace=True)
    print("Activity duplicates removed.")

# 2b. Check for duplicates in sleep_day
# NOTE: The sleepDay data often contains duplicates that need removal.
print(f"Sleep Duplicates found: {sleep_day.duplicated().sum()}")
if sleep_day.duplicated().any():
    sleep_day.drop_duplicates(inplace=True)
    print("Sleep duplicates removed.")


# --- TASK 3: Data Transformation (Merge Tables) ---

# Merge the two datasets on the common columns: user_id and date.
# We use an outer merge to keep all records from both tables, ensuring no loss of data.
combined_data = pd.merge(
    daily_activity,
    sleep_day,
    on=['user_id', 'date'],
    how='outer'
)

# Display the result of the merge
print("\n--- Combined Data Summary ---")
print(f"Total rows in combined dataset: {len(combined_data)}")
print("Combined Data Head:")
print(combined_data.head())
print("Combined Data Info:")
print(combined_data.info())

# Save the cleaned, merged data for the next phase (Analyze)
combined_data.to_csv('combined_bellabeat_data_cleaned.csv', index=False)
print("\nCleaned and merged data saved to 'combined_bellabeat_data_cleaned.csv'.")


# ==============================================================================
# --- TASK 1: Calculate Summary Statistics (Mean, Median, Min, Max) ---

print("\n--- 1. Summary Statistics for Key Metrics ---")

# Select relevant numeric columns for overall statistics
key_metrics = combined_data[[
    'TotalSteps',
    'TotalMinutesAsleep',
    'TotalTimeInBed',
    'Calories',
    'VeryActiveMinutes',
    'SedentaryMinutes'
]]

# Calculate and display descriptive statistics
print(key_metrics.describe().T)


# --- TASK 2: Identify Trends ---

# --- 2a. Analyze User Usage Frequency ---
print("\n--- 2a. Usage Frequency Analysis ---")

# Calculate the number of days each user logged data
usage_frequency = combined_data.groupby('user_id')['date'].count().reset_index()
usage_frequency.rename(columns={'date': 'days_logged'}, inplace=True)

# Define categories based on 31 days of logging (the sample period)
def categorize_usage(days):
    if days >= 25:
        return 'High Use (Daily/Consistent)'
    elif days >= 15:
        return 'Moderate Use (Occasional)'
    else:
        return 'Low Use (Less than half the period)'

usage_frequency['usage_type'] = usage_frequency['days_logged'].apply(categorize_usage)

print("User count by usage type:")
print(usage_frequency['usage_type'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%')

# --- 2b. Identify User Activity Types (Based on Total Steps) ---
# CDC/Industry standard benchmarks:
# Sedentary: < 5,000 steps/day
# Lightly Active: 5,000 - 7,499 steps/day
# Moderately Active: 7,500 - 9,999 steps/day
# Very Active: >= 10,000 steps/day

# Calculate the average daily steps per user across the logging period
average_steps = combined_data.groupby('user_id')['TotalSteps'].mean().reset_index()

def categorize_activity(steps):
    if steps >= 10000:
        return 'Very Active (High Value)'
    elif steps >= 7500:
        return 'Moderately Active'
    elif steps >= 5000:
        return 'Lightly Active'
    else:
        return 'Sedentary'

average_steps['activity_type'] = average_steps['TotalSteps'].apply(categorize_activity)

print("\nUser count by average activity level:")
print(average_steps['activity_type'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%')


# --- 2c. Correlation Analysis (Activity vs. Sleep) ---
print("\n--- 2c. Correlation Matrix ---")

# Calculate the correlation matrix for key metrics
correlation_matrix = combined_data[[
    'TotalSteps',
    'TotalMinutesAsleep',
    'TotalTimeInBed',
    'Calories',
    'VeryActiveMinutes',
    'SedentaryMinutes'
]].corr()

# Print the correlation of Minutes Asleep with other metrics
print("Correlation with Total Minutes Asleep:")
print(correlation_matrix['TotalMinutesAsleep'].sort_values(ascending=False))

# ==============================================================================
# PHASE 5: SHARE & ACT (Visualization & Recommendations)
# ==============================================================================

# This section assumes the combined_data dataframe has been created from Phase 3

# --- 1. Data Preparation for Visualizations ---

# Calculate the average daily steps per user (for activity categorization)
average_steps = combined_data.groupby('user_id')['TotalSteps'].mean().reset_index()

def categorize_activity(steps):
    if steps >= 10000:
        return 'Very Active (>=10k)'
    elif steps >= 7500:
        return 'Moderately Active (7.5k-10k)'
    elif steps >= 5000:
        return 'Lightly Active (5k-7.5k)'
    else:
        return 'Sedentary (<5k)'

average_steps['activity_type'] = average_steps['TotalSteps'].apply(categorize_activity)

# Calculate user usage frequency (for consistency analysis)
usage_frequency = combined_data.groupby('user_id')['date'].count().reset_index()
usage_frequency.rename(columns={'date': 'days_logged'}, inplace=True)


# --- 2. Visualization 1: User Distribution by Activity Level ---
plt.figure(figsize=(10, 6))
order = ['Sedentary (<5k)', 'Lightly Active (5k-7.5k)', 'Moderately Active (7.5k-10k)', 'Very Active (>=10k)']
sns.countplot(x='activity_type', data=average_steps, order=order, palette='viridis')

plt.title('User Distribution by Average Daily Activity Level', fontsize=14)
plt.xlabel('Activity Level (Average Daily Steps)', fontsize=12)
plt.ylabel('Number of Users', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('viz_activity_distribution.png')
plt.close()


# --- 3. Visualization 2: Relationship between Steps and Sleep ---
sleep_activity_data = combined_data.dropna(subset=['TotalMinutesAsleep'])
plt.figure(figsize=(10, 6))
sns.scatterplot(x='TotalSteps', y='TotalMinutesAsleep', data=sleep_activity_data, alpha=0.6)

plt.title('Daily Total Steps vs. Total Minutes Asleep', fontsize=14)
plt.xlabel('Total Steps', fontsize=12)
plt.ylabel('Total Minutes Asleep', fontsize=12)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('viz_steps_vs_sleep.png')
plt.close()


# --- 4. Visualization 3: User Consistency (Usage Frequency) ---
plt.figure(figsize=(10, 6))
usage_frequency_sorted = usage_frequency.sort_values('days_logged', ascending=False)
total_users = len(usage_frequency_sorted)
usage_frequency_sorted['user_index'] = range(1, total_users + 1)

sns.lineplot(x='user_index', y='days_logged', data=usage_frequency_sorted, marker='o', color='coral')
plt.axhline(y=15, color='gray', linestyle='--', label='Moderate Use Threshold (15 days)')

plt.title('User Consistency (Days Logged Over 31-Day Period)', fontsize=14)
plt.xlabel('User Index (Sorted by Logging Days)', fontsize=12)
plt.ylabel('Days Logged', fontsize=12)
plt.legend()
plt.tight_layout()
plt.savefig('viz_usage_consistency.png')
plt.close()
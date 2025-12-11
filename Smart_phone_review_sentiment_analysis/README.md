\# Smart Phone Review Sentiment Analysis and Concept Drift Detection



\## 1. Project Overview

This project implements a complete pipeline for analyzing and classifying the sentiment of a large dataset of smartphone-related text reviews (likely tweets). The primary goal is to build highly accurate classification models (Multinomial Naive Bayes and XGBoost) to predict sentiment (Positive, Negative, or Neutral) and, critically, to assess the long-term robustness of these models by testing for Concept Drift across time-ordered data.

The full analysis is contained within the Jupyter Notebook: Smart_phone_review_sentiment_analysis.ipynb.
========================================================================================================================================================================

\## 2. Project Goal and Data

•   Goal: To accurately classify text reviews into sentiment categories and monitor model performance over time.

•  Data Source: The project reads two time-ordered datasets from Google Drive: train.csv (for initial model training) and test.csv (for concept drift evaluation).

•  Target Variable: Sentiment (derived from text polarity), mapped to: Negative (1), Neutral (0), Positive (2).

========================================================================================================================================================================

\## 3. Methodology: NLP and Machine Learning Pipeline

3.1. Text Preprocessing (The Cleaning Pipeline)

Raw text data requires extensive cleaning to be usable by machine learning models.

• 	Cleaning: data_processing: Removes mentions (@w+), hashtags (#), and non-alphabetic characters.
•  	Tokenization nltk.word_tokenizeBreaks text into individual word units (tokens)
• 	Stop-word Removal:	nltk.corpus.stopwords:	Removes common, uninformative words ("the", "is", "a") to focus on sentiment-bearing terms.
• 	StemmingPorterStemmerReduces words to their root form (e.g., "running" $\rightarrow$ "run") to reduce feature space and improve model generalization.
• 	Sentiment Scoring:	TextBlob Polarity: Calculates a continuous sentiment score (-1.0 to +1.0).
• 	Labeling: sentiment function: Maps the continuous polarity score to the discrete categories (Negative, Neutral, Positive).


3.2. Exploratory Data Analysis (EDA)
Sentiment Distribution: The notebook uses a Countplot and a Pie Chart to visualize the balance (or imbalance) of the three sentiment classes in the training data. This step is crucial for understanding potential bias in model training.

3.3. Feature Extraction and Model Training
Feature Extraction: The cleaned text (filtered_text) is converted into a numerical feature matrix using CountVectorizer (Bag of Words - BoW). This technique represents each review as a vector based on the frequency of words in a predefined vocabulary.

Model Training: The vectorized features are split into training (80%) and testing (20%) sets.

Model 1 (Baseline): MultinomialNB (Naive Bayes Classifier)

Model 2 (Advanced): XGBClassifier (Extreme Gradient Boosting)
========================================================================================================================================================================

\## 4. Key Results and Evaluation
Confusion Matrix: A heatmap visualization is generated for both models to show classification quality, detailing where misclassifications occur (e.g., how often Negative reviews are mistaken for Neutral).
Concept Drift Analysis
Concept Drift refers to a change in the relationship between the input data (reviews) and the target variable (sentiment) over time, often leading to reduced model accuracy.

Method: The model's accuracy is calculated in rolling 1,000-point batches across the combined, time-ordered train and test datasets.

Visualization: Line plots are generated for both models. A downward trend in accuracy over time in these plots indicates that the model is drifting and may need retraining on the newer data.

Interpretation: The magnitude and trend of the accuracy plots show the stability of the learned sentiment patterns.

========================================================================================================================================================================

\## 5. Code and Deliverables

\*\*Analysis Code:\*\* Smart_phone_review_sentiment_analysis
\* \*\*Analysis data:\*\* ./Data



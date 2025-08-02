Loan Approval Prediction System Using KNN and Streamlit:

1. Project Overview
The objective of this project was to build a predictive system that can classify loan applications as either approved or rejected based on applicant information. The core of the system involves machine learning techniques to learn from historical loan data and a user-friendly frontend built using Streamlit for easy interaction.

2. Dataset and Features
- The dataset used for this project contains various attributes related to the loan applicant and the loan itself. Key features included:
- Demographics: person_age, person_gender, person_education, person_income
- Employment & Financial Info: person_emp_exp, person_home_ownership, credit_score, loan_percent_income
- Loan Attributes: loan_amnt, loan_intent, loan_int_rate
- Credit History: cb_person_cred_hist_length, previous_loan_defaults_on_file
- Target Variable: loan_status (1 = approved, 0 = rejected)
- These features were a mix of categorical and numerical types, requiring appropriate preprocessing.

3. Data Preprocessing
- Missing Values: Handled missing or inconsistent entries, particularly in credit score and employment experience.
- Encoding: Applied label encoding and one-hot encoding for categorical variables.
- Feature Scaling: Normalized numerical features for algorithms sensitive to scale, such as KNN.
- Train-Test Split: Divided the dataset into training and testing sets (typically 80/20 split).

4. Model Building
- I experimented with two models to solve the classification problem:

a. Logistic Regression
A simple and interpretable baseline model.
- Gave reasonable results, but performance was slightly lower compared to KNN.

b. K-Nearest Neighbors (KNN)
- Tuned the number of neighbors using cross-validation.

Achieved higher accuracy and better overall metrics on the test data.
Selected KNN as the final model due to its superior performance.

5. Evaluation Metrics

Models were evaluated using:
- Accuracy
- Recall
- Confusion Matrix

- KNN outperformed logistic regression across these metrics, especially in handling class imbalance and predicting positive cases accurately.

6. Application Deployment Using Streamlit
- After finalizing the KNN model, I built a web application using Streamlit to allow users to interact with the model and predict loan approval outcomes in real time.

Features of the Streamlit App:
- User input fields for all features such as income, age, education, credit score, etc.
- Backend processing to apply the same preprocessing steps as during training.
- Real-time prediction output: “Loan Approved” or “Loan Rejected”.
- 
Simple, intuitive UI suitable for non-technical users.

7. Final Outcome

- The result was a functional and accurate loan prediction system that:
- Provides instant feedback to users based on the data they input.
- Demonstrates the application of KNN in a real-world use case.
- Can be extended further with more data or integrated into a larger financial system.

8. Future Enhancements

- Model Improvements: Experiment with ensemble models like Random Forest or XGBoost.
- Explainability: Add SHAP or LIME to explain model predictions.
- Database Integration: Store and retrieve predictions using a backend database.
- Authentication: Add login functionality to secure the application.


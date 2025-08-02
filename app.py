import streamlit as st  # type: ignore
import joblib
import numpy as np

# setup page
st.set_page_config(
    page_title="Loan Prediction App",          # Title shown in the browser tab
    page_icon="💸",                            # Emoji or path to an image icon
    layout="wide",                             # Options: "centered" or "wide"
    initial_sidebar_state="expanded",          # "auto", "expanded", "collapsed"
    menu_items= {                               # Optional custom help/about menu
        'Get Help': 'https://www.medindia.net/directories/hospitals/government-mental-hospital-thane-thane-maharashtra-26614.html',
        'Report a bug': 'https://example.com/bug',
        'About': 'Created by Aanchal Pandey — Data Science Student 🚀'
    }
)


# Load the trained model
model = joblib.load("loan_model.pkl")

# Streamlit page UI
st.title("Loan Prediction Application")
st.write("Please enter the details of the applicant:")

# Categorical mappings
model_gender = {'female': np.int64(0), 'male': np.int64(1)}
select_model_gender = st.selectbox("Model gender: ", list(model_gender.keys()))
person_gender = model_gender[select_model_gender]

model_education = {
    'Associate': np.int64(0), 'Bachelor': np.int64(1), 'Doctorate': np.int64(2),
    'High School': np.int64(3), 'Master': np.int64(4)
}
select_model_education = st.selectbox("Model education: ", list(model_education.keys()))
person_eduation = model_education[select_model_education]

model_ownership = {'MORTGAGE': np.int64(0), 'OTHER': np.int64(1), 'OWN': np.int64(2), 'RENT': np.int64(3)}
select_model_ownership = st.selectbox("Model home ownership: ", list(model_ownership.keys()))
person_home_ownership = model_ownership[select_model_ownership]

model_loan_intend = {
    'DEBTCONSOLIDATION': np.int64(0), 'EDUCATION': np.int64(1),
    'HOMEIMPROVEMENT': np.int64(2), 'MEDICAL': np.int64(3),
    'PERSONAL': np.int64(4), 'VENTURE': np.int64(5)
}
select_model_loan_intend = st.selectbox("Model loan intent: ", list(model_loan_intend.keys()))
loan_intent = model_loan_intend[select_model_loan_intend]

model_previous_loan_defaults_on_file = {'No': np.int64(0), 'Yes': np.int64(1)}
select_model_previous_loan_defaults_on_file = st.selectbox(
    "Model previous loan defaults on file: ", list(model_previous_loan_defaults_on_file.keys()))
previous_loan_defaults_on_file = model_previous_loan_defaults_on_file[select_model_previous_loan_defaults_on_file]

# Numerical inputs
person_age = st.number_input("Age of the applicant", min_value=18, max_value=100, step=1)
person_income = st.number_input("Annual income of the applicant", min_value=1000, max_value=1000000, step=1000)
person_emp_exp = st.number_input("Years of employment experience", min_value=0, max_value=50, step=1)
loan_amnt = st.number_input("Loan amount requested", min_value=1000, max_value=500000, step=1000)
loan_int_rate = st.number_input("Interest rate on the loan", min_value=0.0, max_value=100.0, step=0.1)
loan_percent_income = st.number_input("Percentage of income to be used for loan repayment", min_value=0.0, max_value=100.0, step=0.1)
cb_person_cred_hist_length = st.number_input("Credit history length in months", min_value=0, max_value=120, step=1)
credit_score = st.number_input("Credit score of the applicant", min_value=300, max_value=850, step=1)

# Predict button
if st.button("Predict Loan Approval"):
    input_data = np.array([[
        person_age,
        person_gender,
        person_eduation,
        person_income,
        person_emp_exp,
        person_home_ownership,
        loan_amnt,
        loan_intent,
        loan_int_rate,
        loan_percent_income,
        cb_person_cred_hist_length,
        credit_score,
        previous_loan_defaults_on_file
    ]])

    prediction = model.predict(input_data)[0]
    result = '✅ Approved' if prediction == 1 else '❌ Rejected'
    st.success(f"Loan Application Result: {result}")

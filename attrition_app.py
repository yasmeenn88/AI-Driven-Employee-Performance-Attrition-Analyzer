
import streamlit as st
import pandas as pd
import os
import joblib
from datetime import datetime


# Load model components

model = joblib.load("best_gradient_boosting_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoders = joblib.load("label_encoders.pkl")

# Survey config

CATEGORICAL_OPTIONS = {
    "Business_Travel": ['Travel Rarely', 'Travel Frequently', 'No Travel'],
    "Department": ['Cyber Security', 'Software Development', 'IT Services', 'Data Science', 'Network Administration'],
    "Education": ['Graduation', 'Degree', "Master's", 'PhD', 'Below College'],
    "Environment_Satisfaction": ['1', '2', '3', '4', '5'],
    "Gender": ['Male', 'Female'],
    "Job_Involvement": ['1', '2', '3', '4', '5'],
    "Job_Level": ['1', '2', '3', '4', '5', '6', '7', '8'],
    "Job_Role": ['IT', 'QA Analyst', 'Business Analyst', 'Manager', 'Consultant', 'Support', 'HR', 'Software Engineer', 'Technician', 'Director', 'Developer', 'Help Desk'],
    "Job_Satisfaction": ['1', '2', '3', '4', '5'],
    "Marital_Status": ['Married', 'Divorced', 'Single'],
    "Overtime": ['Yes', 'No'],
    "Work_life_balance": ['1', '2', '3', '4', '5']
}

NUMERIC_COLUMNS = [
    "Age",
    "Distance_From_Home",
    "Salary",
    "Number_of_Companies_Worked_previously",
    "Salary_Hike_in_percent",
    "Total_working_years_experience",
    "No_of_years_worked_at_current_company",
    "No_of_years_in_current_role",
    "Years_since_last_promotion"
]

# Exact order of features used during training
model_features = list(CATEGORICAL_OPTIONS.keys()) + NUMERIC_COLUMNS
CSV_FILE = "survey_responses.csv"


# App Interface

st.set_page_config("Attrition Prediction App", layout="wide")
st.sidebar.title("📋 Menu")
choice = st.sidebar.radio("Go to", ["🧑 Employee Survey", "👩‍💼 HR Dashboard"])


# Employee Survey
if choice == "🧑 Employee Survey":
    st.title(" Monthly Employee Survey Form")

    with st.form("survey_form"):
        name = st.text_input(" Your Full Name")
        survey_data = {"Name": name}

        # Categorical dropdowns
        for col, options in CATEGORICAL_OPTIONS.items():
            survey_data[col] = st.selectbox(col.replace("_", " "), options)

        # Numeric inputs
        for col in NUMERIC_COLUMNS:
            survey_data[col] = st.number_input(col.replace("_", " "), step=1)

        submitted = st.form_submit_button("Submit Survey ✅")
        if submitted:
            df = pd.DataFrame([survey_data])
            df["Submission_Date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if os.path.exists(CSV_FILE):
                df.to_csv(CSV_FILE, mode='a', header=False, index=False)
            else:
                df.to_csv(CSV_FILE, index=False)
            st.success(" Your response has been submitted successfully. ")

# HR Dashboard
else:
    st.title("👩‍💼 HR Dashboard – Attrition Risk Alerts")

    if not os.path.exists(CSV_FILE):
        st.warning("⚠️ No survey responses yet.")
    else:
        df = pd.read_csv(CSV_FILE)

        # Drop rows with missing critical fields
        df = df.dropna(subset=["Name"] + model_features)

        # Encode features
        features = df[model_features].copy()
        for col in CATEGORICAL_OPTIONS.keys():
            if col in label_encoders:
                features[col] = label_encoders[col].transform(features[col])

        X = scaler.transform(features.values)

        # Predict
        preds = model.predict(X)
        df["Predicted_Risk"] = preds

        # Alert Message
        def risk_alert(row):
            if row["Predicted_Risk"] == 1:
                return "🔴 High risk of leaving this month"
            return "✅ No risk detected"

        df["Alert_Message"] = df.apply(risk_alert, axis=1)

        st.subheader("🔔 Predicted Attrition Alerts")
        filter_high = st.checkbox("Show only high-risk employees 🔴", value=False)

        if filter_high:
            df = df[df["Predicted_Risk"] == 1]

        # Display table
        alert_df = df[["Name", "Predicted_Risk", "Alert_Message", "Submission_Date"]].copy()
        alert_df["Action"] = "🔍 View / Notify"

        def color_risk(val):
            return "color: red; font-weight: bold" if val == 1 else "color: green"

        st.dataframe(alert_df.style.applymap(color_risk, subset=["Predicted_Risk"]))

        st.markdown("📤 [Download All Responses as CSV](./survey_responses.csv)")








# ==========================================================
#  AI AGENT TEMPLATE (STUDENTS MUST CUSTOMIZE)
# ==========================================================

import streamlit as st
import pickle
import numpy as np

# ==========================================================
# STEP 1 — CHANGE AGENT NAME (MANDATORY)
# ==========================================================
# Replace with your name + problem
# Example: "Harshit Churn Predictor"

st.title("YOUR NAME - AI AGENT")
st.write("Enter customer details to get prediction")
# ==========================================================
# STEP 2 — LOAD MODEL (DO NOT CHANGE PATH)
# ==========================================================

try:
model = pickle.load(open("../models/model.pkl", "rb"))
except:
st.error("❌ Model not found. Please train and save model first.")
st.stop()

# ==========================================================
# STEP 3 — INPUT FEATURES (CUSTOMIZE BASED ON YOUR MODEL)
# ==========================================================
#  You MUST align these inputs with your feature engineering
# YOU CAN CHANGE THESE

age = st.number_input("Age", min_value=18, max_value=80, value=30)
monthly_spend = st.number_input("Monthly Spend", value=100.0)
num_transactions = st.number_input("Number of Transactions", value=10)
tenure = st.number_input("Tenure (months)", value=12)
last_login = st.number_input("Last Login Days", value=5)

# OPTIONAL — Add more features here

# Example:

# support_tickets = st.number_input("Support Tickets", value=1)

# ==========================================================

#  STEP 4 — PREDICTION BUTTON

# ==========================================================

if st.button("Predict"):


try:
    # ==================================================
    # STEP 5 — ALIGN INPUT FORMAT (VERY IMPORTANT)
    # ==================================================
    # Order must match training features

    input_data = np.array([[
        age,
        monthly_spend,
        num_transactions,
        tenure,
        last_login
    ]])

    # ==================================================
    # STEP 6 — MODEL PREDICTION
    # ==================================================
    prediction = model.predict(input_data)

    # ==================================================
    #  STEP 7 — OUTPUT (CUSTOMIZE BASED ON PROBLEM)
    # ==================================================

    # BASIC OUTPUT (YOU CAN IMPROVE)
    st.success(f"Prediction: {prediction[0]}")

    # ==================================================
    # BONUS (OPTIONAL — IMPROVE UX)
    # ==================================================
    
    # Classification Example
    if prediction[0] == 1:
        st.error("⚠️ High Risk / Negative Outcome")
    else:
        st.success("Positive Outcome")

    # 👉 Confidence Score (if model supports it)
    try:
        prob = model.predict_proba(input_data)
        st.info(f"Confidence: {round(max(prob[0])*100,2)}%")
    except:
        pass

except Exception as e:
    st.error("❌ Error in prediction. Check feature alignment.")


# ==========================================================
# FINAL INSTRUCTIONS FOR STUDENTS
# ==========================================================
# ==============================
# WHAT YOU MUST CHANGE
# ==============================
# 1. Agent Title → Add your name
# 2. Input Features → Match your dataset
# 3. Input Order → Must match training data
# 4. Output Logic → Based on your problem
# ==============================
# WHAT YOU CAN IMPROVE
# ==============================
# - Add more input fields
# - Improve UI (colors, layout)
# - Add explanation of prediction
# - Add business insights
# - Add charts or visuals
# ==============================
#  GOAL
# ==============================
# Build an AI Agent that is:
# ✔ Accurate
# ✔ User-friendly
# ✔ Visually appealing

print(" Customize your AI agent and make it unique!")

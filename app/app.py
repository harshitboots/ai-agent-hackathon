# ==========================================================
# 🧾 WHAT YOU MUST CHANGE (READ CAREFULLY)
# ==========================================================
# - Agent Title → Add your name + problem
# - Input Features → Match your dataset columns
# - Feature Order → MUST match training data EXACTLY
# - Output logic → Based on your problem (classification/regression)

# ==========================================================
# 💡 WHAT YOU CAN IMPROVE
# ==========================================================
# - Add more input fields
# - Improve UI design
# - Add explanation of prediction
# - Add charts or business insights

# ==========================================================
# 🎯 GOAL
# ==========================================================
# Build an AI Agent that is:
# ✔ Accurate  
# ✔ User-friendly  
# ✔ Visually appealing  

# ==========================================================
# 🤖 AI AGENT TEMPLATE (STUDENTS MUST CUSTOMIZE)
# ==========================================================

import streamlit as st
import pickle
import numpy as np
import os

# ==========================================================
# 🔥 STEP 1 — CHANGE AGENT NAME (MANDATORY)
# ==========================================================
# 👉 STUDENT TASK:
# Replace "YOUR NAME" with your name
# Replace "AI AGENT" with your problem
# Example:
# st.title("Harshit - Churn Prediction Agent")

st.set_page_config(page_title="AI Agent", layout="centered")

st.title("YOUR NAME - AI AGENT")  # 🔥 CHANGE THIS
st.write("Enter details below to get prediction")

# ==========================================================
# 📦 STEP 2 — LOAD MODEL (DO NOT CHANGE FILE NAME)
# ==========================================================
# ⚠️ IMPORTANT:
# Your trained model MUST be saved as:
# models/model.pkl

MODEL_PATH = "models/model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error("❌ Model not found. Please train your model first.")
    st.info("👉 Save your model as: models/model.pkl")
    st.stop()

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# ==========================================================
# 🧠 STEP 3 — INPUT FEATURES (CUSTOMIZE THIS SECTION)
# ==========================================================
# 🔥 VERY IMPORTANT:
# These inputs MUST match your training features EXACTLY
# ✔ Same columns
# ✔ Same order
# ✔ Same transformations

st.subheader("📊 Input Features")

# 👉 STUDENT TASK:
# Modify these inputs based on YOUR dataset

age = st.number_input("Age", min_value=18, max_value=80, value=30)  
# 🔧 CHANGE if your dataset has different feature

monthly_spend = st.number_input("Monthly Spend (£)", value=100.0)  
# 🔧 CHANGE name/value based on your dataset

num_transactions = st.number_input("Number of Transactions", value=10)  
# 🔧 MODIFY or REMOVE if not needed

tenure = st.number_input("Tenure (months)", value=12)  
# 🔧 MODIFY if your dataset uses different feature

last_login = st.number_input("Days Since Last Login", value=5)  
# 🔧 MODIFY if not relevant

# 👉 STUDENT: Add/remove features based on your dataset
# Example:
# support_tickets = st.number_input("Support Tickets", value=1)

# ==========================================================
# 🎯 STEP 4 — PREDICT BUTTON
# ==========================================================

if st.button("🔮 Predict"):

    try:
        # ==================================================
        # ⚠️ STEP 5 — FEATURE ORDER (VERY IMPORTANT)
        # ==================================================
        # 👉 STUDENT TASK:
        # The order here MUST match your training data EXACTLY
        # If wrong → predictions will be incorrect

        input_data = np.array([[ 
            age,
            monthly_spend,
            num_transactions,
            tenure,
            last_login
        ]])
        # 🔧 MODIFY this order if you changed features above

        # ==================================================
        # 🤖 STEP 6 — MODEL PREDICTION
        # ==================================================
        prediction = model.predict(input_data)

        # ==================================================
        # 📢 STEP 7 — OUTPUT (CUSTOMIZE BASED ON PROBLEM)
        # ==================================================
        # 👉 STUDENT TASK:
        # Modify output based on your problem type

        st.success(f"Prediction: {prediction[0]}")

        # ==================================================
        # 🎨 BONUS UX (OPTIONAL BUT RECOMMENDED)
        # ==================================================
        # 👉 STUDENT: Customize this logic

        if prediction[0] == 1:
            st.error("⚠️ High Risk / Negative Outcome")  
            # 🔧 Change meaning based on your problem
        else:
            st.success("✅ Positive Outcome")  
            # 🔧 Change meaning based on your problem

        # ==================================================
        # 📊 CONFIDENCE SCORE (IF AVAILABLE)
        # ==================================================
        try:
            prob = model.predict_proba(input_data)
            confidence = round(max(prob[0]) * 100, 2)
            st.info(f"Confidence: {confidence}%")
        except:
            st.warning("⚠️ Confidence not available for this model")

    except Exception as e:
        st.error("❌ Prediction failed. Check feature alignment.")
        st.text(str(e))
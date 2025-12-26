#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load model and encoders
# -----------------------------
model = joblib.load("career_model.pkl")
ord_encoder = joblib.load("ordinal_encoder.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Career Recommendation System", layout="centered")

st.title("🎯 Career Recommendation System")
st.write("Enter your details to get a recommended career path")

# -----------------------------
# User Inputs
# -----------------------------
education = st.selectbox(
    "Education Level",
    ["High School", "Intermediate", "Bachelor's", "Master's", "PhD"]
)

specialization = st.selectbox(
    "Specialization",
    ["Computer Science", "Information Technology", "Electronics", "Mechanical", "Civil", "Business", "Other"]
)

skills = st.selectbox(
    "Primary Skill",
    ["Python", "SQL", "Machine Learning", "Data Analysis", "Web Development", "Cloud", "Other"]
)

certifications = st.selectbox(
    "Certifications",
    ["None", "Beginner", "Intermediate", "Advanced"]
)

# -----------------------------
# Prediction Button
# -----------------------------
if st.button("🔍 Predict Career"):
    
    # Create input dataframe (ORDER MUST MATCH TRAINING)
    input_df = pd.DataFrame(
        [[education, specialization, skills, certifications]],
        columns=["Education Level", "Specialization", "Skills", "Certifications"]
    )

    # Encode inputs
    input_encoded = ord_encoder.transform(input_df)

    # Predict
    prediction_encoded = model.predict(input_encoded)

    # Decode output
    prediction = label_encoder.inverse_transform(prediction_encoded)

    # Show result
    st.success(f"✅ Recommended Career: **{prediction[0]}**")


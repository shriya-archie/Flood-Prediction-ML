import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. Load the "frozen" models
# If you haven't made these files yet, the app will error out!
try:
    lin_model = joblib.load('linear_model.pkl')
    log_model = joblib.load('logistic_model.pkl')
    rf_model = joblib.load('random_forest_model.pkl')
except:
    st.error("Model files (.pkl) not found! Please export them from your notebooks first.")

st.title("🌊 The Flood Predictor: Model Comparison")
st.markdown("Comparing my **77% Accuracy** Logistic model vs my **86% Accuracy** Random Forest.")

# 2. Setup Input Sliders (Let's use your top features)
st.sidebar.header("Adjust Environmental Factors")
monsoon = st.sidebar.slider("Monsoon Intensity", 0.0, 1.0, 0.5)
river = st.sidebar.slider("River Management", 0.0, 1.0, 0.5)
drainage = st.sidebar.slider("Drainage Systems", 0.0, 1.0, 0.5)
climate = st.sidebar.slider("Climate Change Impact", 0.0, 1.0, 0.5)

# Create a dummy array for all 21 features (assuming others are 0.5)
# Note: The model expects exactly 21 inputs if you trained it on 21
input_data = np.array([[monsoon, river, drainage, climate] + [0.5]*17])

# 3. Comparisons
st.header("🔍 Side-by-Side Predictions")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Linear")
    # Linear predicts a raw number
    lin_pred = lin_model.predict(input_data)[0]
    st.metric("Raw Probability", f"{lin_pred:.4f}")
    st.caption("Predicts precise decimals.")

with col2:
    st.subheader("Logistic")
    # Logistic predicts 0 or 1
    log_pred = log_model.predict(input_data)[0]
    result = "FLOOD" if log_pred == 1 else "SAFE"
    st.metric("Classification", result)
    st.caption("Uses a 'Straight Line' boundary.")

with col3:
    st.subheader("Random Forest")
    # Random Forest is your best model
    rf_pred = rf_model.predict(input_data)[0]
    rf_result = "FLOOD" if rf_pred == 1 else "SAFE"
    st.metric("Classification", rf_result)
    st.success("Uses 100 Non-Linear Trees.")

st.divider()
st.write("### Why is Random Forest different?")
st.write("While Linear and Logistic models were 'fooled' by noisy data, the Random Forest (86% accuracy) looks at the complex interactions between these sliders.")
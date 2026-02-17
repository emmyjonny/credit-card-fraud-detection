import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("Credit Card Fraud Detection System")

st.write("Upload a transaction dataset to detect fraudulent transactions.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    
    st.write("Dataset Preview:")
    st.dataframe(data.head())
    
    # Example prediction (replace with your trained model)
    st.write("Fraud Detection Results:")
    
    data['Fraud Prediction'] = np.random.choice([0,1], size=len(data))
    
    st.dataframe(data)
    
    fraud_count = data['Fraud Prediction'].sum()
    
    st.write(f"Detected {fraud_count} fraudulent transactions")

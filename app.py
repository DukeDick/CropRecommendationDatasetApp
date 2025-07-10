import streamlit as st
import numpy as np
import pickle

# Load trained Random Forest model
model = pickle.load(open('RandomForest.pkl', 'rb'))

# App Title
st.set_page_config(page_title="Smart Crop Recommendation", layout="centered")
st.title("Smart Crop Recommendation System🌱")
st.markdown("### Fill in the following field values to predict the most suitable crop.")

# Center the input form using columns
col1, col2, col3 = st.columns([1, 2, 1])  # Center column is twice as wide

with col2:
    N = st.number_input("Nitrogen", min_value=0.0, step=1.0)
    P = st.number_input("Phosphorus", min_value=0.0, step=1.0)
    K = st.number_input("Potassium", min_value=0.0, step=1.0)
    temp = st.number_input("Temperature (°C)", step=0.1)
    humidity = st.number_input("Humidity (%)", step=0.1)
    ph = st.number_input("Soil pH", step=0.1)
    rainfall = st.number_input("Rainfall (mm)", step=0.1)

    if st.button("Predict"):
        try:
            input_data = np.array([[N, P, K, temp, humidity, ph, rainfall]])
            prediction = model.predict(input_data)[0]
            st.success(f"🌱 {prediction} is the best crop to be cultivated right there.")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

import streamlit as st
import pandas as pd
import joblib

# 1. Model Load karo (Joblib use karke)
# Agar model 'models/' folder mein hai toh path sahi dena
model = joblib.load('smartphone_model.pkl')

# 2. Page Configuration
st.set_page_config(page_title="SmartPrice Predictor", page_icon="📱")

st.title("📱 Smartphone Price Predictor")
st.markdown("Enter phone specifications to estimate the **Final Price**.")

# 3. User Inputs
# Humne wahi columns liye hain jo Training ke waqt use kiye the
st.sidebar.header("Phone Specifications")

brand = st.sidebar.selectbox("Brand", ['Apple', 'Samsung', 'Xiaomi', 'Realme', 'Motorola', 'OPPO', 'POCO', 'Other'])
model_series = st.sidebar.text_input("Model Series (e.g., iPhone 14, Galaxy S23)", "Others")
ram = st.sidebar.slider("RAM (GB)", 2, 64, 8)
storage = st.sidebar.slider("Storage (GB)", 16, 1024, 128)
color = st.sidebar.selectbox("Color", ['Black', 'White', 'Blue', 'Gray', 'Silver', 'Yellow'])
free_sim = st.sidebar.radio("Sim Free?", ['Yes', 'No'])

# 4. Prediction Button
if st.sidebar.button("Predict Price 🚀"):
    # Data ko DataFrame mein convert karo (Pipeline ko DF chahiye hota hai)
    input_data = pd.DataFrame({
        'Brand': [brand],
        'Model': [model_series],
        'RAM': [ram],
        'Storage': [storage],
        'Color': [color],
        'Free': [free_sim]
    })

    # Prediction
    try:
        prediction = model.predict(input_data)[0]
        
        # Result Display
        st.subheader("Price Prediction")
        st.metric(label="Estimated Price", value=f"€{prediction:.2f}")
        
        st.balloons() # Thodi celebration!
    except Exception as e:
        st.error(f"Error: {e}. Make sure input columns match the training data.")

# 5. Footer
st.markdown("---")
st.caption("Model trained using Random Forest Regressor | Precision based on dataset trends.")
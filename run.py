import streamlit as st
import tensorflow as tf
import pandas as pd
import joblib

# Load model
model = tf.keras.models.load_model("insurance_model.keras")

# Load scaler
scaler = joblib.load("scaler.pkl")


st.title("Insurance Cost Prediction")
st.write("Enter Customer Details")

age = st.number_input("Age", min_value=18, max_value=100, value=30)
sex = st.selectbox("Gender", ["Female", "Male"])
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
children = st.number_input("Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", ["No", "Yes"])
region = st.selectbox(
    "Region",
    ["northeast", "northwest", "southeast", "southwest"]
)

if st.button("Predict"):
    data = {
        "age": [age],
        "bmi": [bmi],
        "children": [children],
        "sex_female": [1 if sex == "Female" else 0],
        "sex_male": [1 if sex == "Male" else 0],
        "smoker_no": [1 if smoker == "No" else 0],
        "smoker_yes": [1 if smoker == "Yes" else 0],
        "region_northeast": [1 if region == "northeast" else 0],
        "region_northwest": [1 if region == "northwest" else 0],
        "region_southeast": [1 if region == "southeast" else 0],
        "region_southwest": [1 if region == "southwest" else 0],
    }

    df = pd.DataFrame(data)

    if hasattr(scaler, "transform"):
        scaled = scaler.transform(df)
        prediction = model.predict(scaled, verbose=0)
        st.success(f"Predicted Insurance Charge: ${prediction[0][0]:,.2f}")
    else:
        st.error(
            f"Error: 'scalers.pkl' contains a {type(scaler).__name__}, "
            "not a fitted scaler object."
        )
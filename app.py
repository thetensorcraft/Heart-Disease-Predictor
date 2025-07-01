import streamlit as st
import pandas as pd
import joblib

# load files
model = joblib.load("heart_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

# UI
st.set_page_config(page_title="Heart Disease Predictor", page_icon="💓")
st.markdown(
    "<h1 style='text-align: center; color: #FF4B4B;'>💓 Heart Disease Prediction</h1>",
    unsafe_allow_html = True
)

# inputs
age = st.slider("Age", 18, 100, 40)
sex = st.selectbox("Sex", ["M", "F"])
cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
chol = st.slider("Cholestrol (mg/dl)", 80, 400, 150)
fbs	= st.selectbox("Fasting Blood Sugar 120mg/dl", [0, 1])
restecg = st.selectbox("Resting Electrographic", [0, 1, 2])
thalach = st.slider("Maximum heart rate achieved", 70, 230, 150)
exang = st.selectbox("Exercise Induced Anigna", [0, 1])
oldpeak	= st.slider("Depression Induced", 0, 7, 5)
slope = st.selectbox("Slope of peak exercise", [0, 1, 2])
ca = st.selectbox("Number of major blood vessels", [0, 1, 2, 3])
thal = st.selectbox("Defect", [1, 2, 3])

# prediction
input_dict = {
    "age": age,
    "sex": 1 if sex == "M" else 0,
    "cp": cp,
    "trestbps": trestbps,
    "chol": chol,
    "fbs": fbs,
    "restecg": restecg,
    "thalach": thalach,
    "exang": exang,
    "oldpeak": oldpeak,
    "slope": slope,
    "ca": ca,
    "thal": thal
}

# input to model
input_df = pd.DataFrame([input_dict], columns = columns)
input_scaled = scaler.transform(input_df)

# prediction
if st.button("Predict"):
    prediction = model.predict(input_scaled)[0]
    if prediction == 1:
        st.markdown(
            f"<div style='background-color:#ffcccc; padding:20px; border-radius:10px;'>"
            f"<h2 style='color:#b30000;'>🔴 High Risk of Heart Disease</h2>",
            unsafe_allow_html = True
        )
    else:
        st.markdown(
            f"<div style='background-color:#ccffcc; padding:20px; border-radius:10px;'>"
            f"<h2 style='color:#006600;'>🟢 Low Risk of Heart Disease</h2>",
            unsafe_allow_html = True
        )

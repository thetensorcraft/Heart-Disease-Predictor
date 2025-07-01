# 💓 Heart Disease Predictor

A Machine Learning-powered web app built with **Streamlit** that predicts the risk of heart disease using patient medical data.

![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-orange?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 🧠 Features

- Predicts heart disease risk as **Low** or **High**
- Clean and interactive **Streamlit UI**
- Uses a trained **Naive Bayes classifier**
- Scaled with **StandardScaler** for better accuracy

---

## 🩺 Input Parameters

| Feature       | Description                        |
|---------------|------------------------------------|
| age           | Age of the person                  |
| sex           | 1 = Male, 0 = Female               |
| cp            | Chest pain type (0–3)              |
| trestbps      | Resting blood pressure             |
| chol          | Cholesterol level                  |
| fbs           | Fasting blood sugar > 120 mg/dl    |
| restecg       | Resting ECG results                |
| thalach       | Maximum heart rate achieved        |
| exang         | Exercise-induced angina            |
| oldpeak       | ST depression                      |
| slope         | Slope of the ST segment            |
| ca            | Number of major vessels (0–3)      |
| thal          | Thalassemia condition (0–3)        |

---

## 📦 Installation

```bash
git clone https://github.com/your-username/heart-disease-predictor.git
cd heart-disease-predictor
pip install -r requirements.txt
streamlit run app.py

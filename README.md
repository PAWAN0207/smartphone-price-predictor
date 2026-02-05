# 📱 Smartphone Value-for-Money Predictor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Model-F7931E?style=for-the-badge&logo=scikitlearn)
![Machine Learning](https://img.shields.io/badge/ML-Random%20Forest-green?style=for-the-badge)

An intelligent Machine Learning web application that predicts a smartphone's **Final Price** based on its specifications (RAM, Storage, Brand, etc.). This tool helps users determine if a smartphone is "Value-for-Money" or overpriced based on historical market data.

## 🚀 Live Demo
🔗 **[Check out the Live App here](https://YOUR-APP-LINK.streamlit.app/)** *(Note: Replace the link above with your actual Streamlit URL after deployment)*

## ✨ Key Features
- **Smart Prediction:** Powered by a **Random Forest Regressor** for high-accuracy price estimations.
- **End-to-End Pipeline:** Utilizes Scikit-Learn `Pipelines` to automate Data Cleaning, Scaling, and Encoding.
- **Realistic Pricing:** Implements **Log-Transformation** techniques to handle price outliers and provide realistic estimates for budget devices.
- **Interactive UI:** A clean, responsive dashboard built with Streamlit.

## 🛠️ Tech Stack
- **Languages:** Python
- **Data Analysis:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn (Random Forest, Preprocessing Pipelines)
- **Deployment:** GitHub, Streamlit Cloud

## 📂 Project Structure
```text
├── app.py                     # Streamlit web application script
├── smartphone_model.pkl        # Pre-trained ML Pipeline (Joblib)
├── requirements.txt            # Project dependencies
├── notebooks/                  # Jupyter notebooks for Exploratory Data Analysis (EDA)
│   └── Model_Training.ipynb
├── .gitignore                  # Files to be ignored by Git (e.g., venv/)
└── README.md                   # Project Documentation
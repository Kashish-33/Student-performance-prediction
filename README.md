  ## # Student Performance Prediction

An end-to-end machine learning project that predicts a student's math
score based on demographic and academic features. The trained model is
served via a Streamlit web application .

## Problem Statement

Predict a student's math score (out of 100) using features such as
gender, race/ethnicity, parental level of education, lunch type, test
preparation course completion, reading score, and writing score.

## Dataset

- Source: Students Performance in Exams (Kaggle)
- Size: 1000 records, 8 features
- Target Variable: Math Score (continuous — regression problem)

## Models Evaluated

| Model                  | Test R² Score |
|------------------------|---------------|
| Ridge Regression       | 0.8806        |
| Linear Regression      | 0.8803        |
| Random Forest          | 0.8551        |
| CatBoost Regressor     | 0.8516        |
| AdaBoost Regressor     | 0.8428        |
| XGBoost Regressor      | 0.8278        |
| Lasso                  | 0.8253        |
| K-Neighbors Regressor  | 0.7838        |
| Decision Tree          | 0.7100        |

## Tech Stack

- Language: Python
- ML Libraries: Scikit-learn, CatBoost, XGBoost
- Web Framework: Streamlit
- Others: Pandas, NumPy, Matplotlib, Seaborn



## How to Run Locally

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Run the app:
   streamlit run streamlit_app.py
4. Open http://localhost:8504 in your browser

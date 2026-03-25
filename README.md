  ## # Student Performance Prediction

An end-to-end machine learning project that predicts a student's math
score based on demographic and academic features. The trained model is
served via a Flask web application deployed on AWS Elastic Beanstalk.

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
- Web Framework: Flask
- Deployment: AWS Elastic Beanstalk
- Others: Pandas, NumPy, Matplotlib, Seaborn

## Project Structure

├── artifacts/              # Saved model and preprocessor (.pkl)
├── catboost_info/          # CatBoost training logs
├── data/
│   ├── 1. EDA STUDENT.ipynb
│   └── 2. MODEL TRAINING.ipynb
├── src/                    # Modular pipeline code
├── templates/              # HTML templates (Flask)
├── application.py          # Flask app entry point
├── requirements.txt
├── setup.py
└── .ebextensions/          # AWS Elastic Beanstalk config

## How to Run Locally

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Run the app:
   python application.py
4. Open http://localhost:5000 in your browser

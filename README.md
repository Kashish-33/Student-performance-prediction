#  Student Performance Prediction


A machine learning web application that predicts student exam scores based on demographic and academic background factors. Built as an end-to-end ML project covering data ingestion, preprocessing, model training, evaluation, and deployment.

---

##  Live Demo

 **[Try it here](https://student-performance-prediction-jckgbdv53yhtyjf9ksxhqe.streamlit.app)**

---

##  Problem Statement

Predict a student's **math score** based on features like gender, race/ethnicity, parental education level, lunch type, test preparation course, and scores in reading and writing.

---

##  ML Pipeline

```
Raw Data → Data Ingestion → Preprocessing → Model Training → Evaluation → Prediction
```

- **Data Ingestion** — Loads and splits data into train/test sets
- **Data Transformation** — Handles numerical scaling and categorical encoding via `ColumnTransformer`
- **Model Training** — Trains and evaluates multiple regression models, saves the best one

---

##  Models Benchmarked

| Model | R² Score |
|---|---|
| **Ridge Regression**  | **0.88** |
| Linear Regression | 0.87 |
| Lasso | 0.82 |
| ElasticNet | 0.81 |
| Random Forest | 0.85 |
| Gradient Boosting | 0.87 |
| XGBoost | 0.86 |
| CatBoost | 0.87 |
| AdaBoost | 0.84 |

> **Best Model:** Ridge Regression with R² = 0.88

---

##  Project Structure

```
student-ml-project/
├── src/                        # Core ML source code
├── notebook/
│   ├── data/
│   │   └── stud.csv            # Raw dataset
│   ├── 1. EDA STUDENT.ipynb    # Exploratory Data Analysis
│   └── 2. MODEL TRAINING.ipynb # Model training & evaluation
├── artifacts/                  # Saved model & preprocessor (auto-generated)
├── catboost_info/              # CatBoost training metadata
├── logs/                       # Training logs (auto-generated)
├── streamlit_app.py            # Streamlit frontend
├── setup.py
├── requirements.txt
└── runtime.txt                 # Python version for Streamlit Cloud
```

---

##  Features Used

| Feature | Type |
|---|---|
| Gender | Categorical |
| Race/Ethnicity | Categorical |
| Parental Level of Education | Categorical |
| Lunch Type | Categorical |
| Test Preparation Course | Categorical |
| Reading Score | Numerical |
| Writing Score | Numerical |

**Target:** Math Score (continuous)

---

##  Run Locally

```bash
# Clone the repo
git clone https://github.com/Kashish-33/student-performance-prediction.git
cd student-performance-prediction

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows


# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
```

---

##  Tech Stack

- **Language:** Python 3.8+
- **ML:** Scikit-Learn, XGBoost, CatBoost
- **Frontend:** Streamlit
- **Deployment:** Streamlit Cloud
- **Logging & Exception Handling:** Custom modules

---


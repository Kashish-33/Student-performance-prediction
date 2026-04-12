import streamlit as st
import sys
import os

# So that src/ is importable
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# ─────────────────────────────────────────────
# Page config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# ─────────────────────────────────────────────
# Custom CSS — clean academic light theme
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #f5f3ee;
    color: #1a1a1a;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2.5rem; max-width: 700px; }

/* ── Header ── */
.header-wrap {
    text-align: center;
    margin-bottom: 2rem;
    padding: 2rem 1.5rem 1.5rem;
    background: #ffffff;
    border-radius: 16px;
    border: 1px solid #e8e4dc;
    box-shadow: 0 2px 12px rgba(0,0,0,0.05);
}
.header-title {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 700;
    color: #1a1a1a;
    line-height: 1.2;
}
.header-sub {
    font-size: 0.82rem;
    color: #888;
    margin-top: 0.4rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}
.accent { color: #5c6bc0; }

/* ── Section label ── */
.section-label {
    font-size: 0.72rem;
    font-weight: 500;
    color: #888;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin: 1.4rem 0 0.6rem;
}

/* ── Selectbox & inputs ── */
div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    border: 1px solid #ddd8ce !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    color: #1a1a1a !important;
}
div[data-baseweb="select"] > div:focus-within {
    border-color: #5c6bc0 !important;
    box-shadow: 0 0 0 3px rgba(92,107,192,0.12) !important;
}
/* Selected value text */
div[data-baseweb="select"] span {
    color: #1a1a1a !important;
}
/* Dropdown menu options */
ul[data-baseweb="menu"] {
    background-color: #ffffff !important;
}
ul[data-baseweb="menu"] li {
    color: #1a1a1a !important;
    background-color: #ffffff !important;
}
ul[data-baseweb="menu"] li:hover {
    background-color: #eef0fb !important;
}
/* Dropdown popover */
div[data-baseweb="popover"] > div {
    background-color: #ffffff !important;
}
[role="listbox"] { background-color: #ffffff !important; }
[role="option"] { background-color: #ffffff !important; color: #1a1a1a !important; }
[role="option"]:hover, [aria-selected="true"] {
    background-color: #eef0fb !important;
    color: #5c6bc0 !important;
}
/* Number input */
input[type="number"] {
    background-color: #ffffff !important;
    border: 1px solid #ddd8ce !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    color: #1a1a1a !important;
}
/* All input text */
input {
    color: #1a1a1a !important;
}
label[data-testid="stWidgetLabel"] p {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.82rem;
    font-weight: 500;
    color: #444 !important;
}
/* Override Streamlit dark mode globally */
.stApp {
    background-color: #f5f3ee !important;
}
p, span, div {
    color: #1a1a1a;
}

/* ── Button ── */
.stButton > button {
    background: #5c6bc0 !important;
    color: #ffffff !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.95rem !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.7rem 2rem !important;
    width: 100%;
    transition: background 0.2s ease, transform 0.1s ease;
}
.stButton > button:hover {
    background: #3f51b5 !important;
    transform: translateY(-1px);
}

/* ── Result card ── */
.result-card {
    background: #ffffff;
    border: 1px solid #c5cae9;
    border-left: 5px solid #5c6bc0;
    border-radius: 12px;
    padding: 1.6rem 1.8rem;
    margin-top: 1.5rem;
    text-align: center;
    animation: fadeIn 0.4s ease;
}
.result-score {
    font-family: 'Playfair Display', serif;
    font-size: 3.5rem;
    font-weight: 700;
    color: #5c6bc0;
    line-height: 1;
}
.result-label {
    font-size: 0.8rem;
    color: #888;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-top: 0.4rem;
}
.result-grade {
    display: inline-block;
    margin-top: 0.8rem;
    padding: 0.3rem 1rem;
    border-radius: 20px;
    font-size: 0.82rem;
    font-weight: 500;
}

/* ── Form card ── */
.form-card {
    background: #ffffff;
    border: 1px solid #e8e4dc;
    border-radius: 16px;
    padding: 1.8rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.04);
    margin-bottom: 1rem;
}

/* ── Divider ── */
.divider { border: none; border-top: 1px solid #e8e4dc; margin: 1.5rem 0; }

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Header
# ─────────────────────────────────────────────
st.markdown("""
<div class="header-wrap">
    <div class="header-title">🎓 Student <span class="accent">Performance</span> Predictor</div>
    <div class="header-sub">Predict Maths Score · ML Powered · Ridge Regression</div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Form
# ─────────────────────────────────────────────
st.markdown('<div class="section-label">Student Details</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["male", "female"],
                          format_func=lambda x: x.capitalize())

    race_ethnicity = st.selectbox("Race / Ethnicity",
                                  ["group A", "group B", "group C", "group D", "group E"],
                                  format_func=lambda x: x.title())

    parental_education = st.selectbox("Parental Level of Education", [
        "associate's degree", "bachelor's degree", "high school",
        "master's degree", "some college", "some high school"
    ], format_func=lambda x: x.title())

with col2:
    lunch = st.selectbox("Lunch Type",
                         ["standard", "free/reduced"],
                         format_func=lambda x: x.title())

    test_prep = st.selectbox("Test Preparation Course",
                             ["none", "completed"],
                             format_func=lambda x: x.title())

st.markdown('<div class="section-label">Academic Scores</div>', unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    reading_score = st.number_input("Reading Score (out of 100)", min_value=0, max_value=100, value=70)
with col4:
    writing_score = st.number_input("Writing Score (out of 100)", min_value=0, max_value=100, value=70)

st.markdown("<br>", unsafe_allow_html=True)

col_l, col_m, col_r = st.columns([1, 2, 1])
with col_m:
    predict_btn = st.button("PREDICT MATHS SCORE")

# ─────────────────────────────────────────────
# Prediction
# ─────────────────────────────────────────────
st.markdown('<hr class="divider">', unsafe_allow_html=True)

if predict_btn:
    try:
        data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_education,
            lunch=lunch,
            test_preparation_course=test_prep,
            reading_score=float(reading_score),
            writing_score=float(writing_score)
        )
        pred_df = data.get_data_as_data_frame()
        pipeline = PredictPipeline()
        result = pipeline.predict(pred_df)[0]
        score = round(result, 1)

        # Grade logic
        if score >= 90:
            grade, grade_color, grade_bg = "A+", "#2e7d32", "#e8f5e9"
        elif score >= 80:
            grade, grade_color, grade_bg = "A", "#388e3c", "#e8f5e9"
        elif score >= 70:
            grade, grade_color, grade_bg = "B", "#f57c00", "#fff3e0"
        elif score >= 60:
            grade, grade_color, grade_bg = "C", "#f9a825", "#fffde7"
        else:
            grade, grade_color, grade_bg = "D", "#c62828", "#ffebee"

        st.markdown(f"""
        <div class="result-card">
            <div class="result-score">{score}</div>
            <div class="result-label">Predicted Maths Score out of 100</div>
            <span class="result-grade" style="background:{grade_bg}; color:{grade_color};">
                Grade {grade}
            </span>
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Prediction failed: {e}")
else:
    st.markdown("""
    <div style="text-align:center; padding: 2rem; color: #bbb; font-size: 0.85rem;
                border: 1px dashed #ddd; border-radius: 12px;">
        ↑ Fill in the details above and hit Predict
    </div>
    """, unsafe_allow_html=True)
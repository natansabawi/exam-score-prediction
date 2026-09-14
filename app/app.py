import streamlit as st
import pandas as pd
import joblib
import os
import sys

st.set_page_config(
    page_title="Ethiopian Giftedness & Talent Center",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
from data.questions import QUESTION_BANK

ASSETS_DIR = os.path.join(BASE_DIR, "assets")
LOGO_PATH = os.path.join(ASSETS_DIR, "logo.png")
HERO_PATH = os.path.join(ASSETS_DIR, "hero.png")

MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "exam_score_prediction_pipeline.joblib")
if not os.path.exists(MODEL_PATH):
    MODEL_PATH = os.path.join(BASE_DIR, "models", "exam_score_prediction_pipeline.joblib")
if not os.path.exists(MODEL_PATH):
    MODEL_PATH = "exam_score_prediction_pipeline.joblib"

# High-Contrast & High-Energy Styling Engine
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;800;900&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">

<style>
    /* Global Canvas Styling */
    html, body, [data-testid="stAppViewContainer"], .main {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        background: radial-gradient(circle at 10% 20%, #090d16 0%, #030712 100%) !important;
        color: #f8fafc !important;
    }

    [data-testid="stHeader"] {
        background: transparent !important;
    }

    /* Force all text elements, labels, and radio options to be visible */
    p, span, label, div, [data-testid="stMarkdownContainer"] p {
        color: #f1f5f9 !important;
    }

    /* Radio button options fix: high contrast visible text */
    [data-testid="stRadio"] label span {
        color: #f8fafc !important;
        font-size: 1.02rem !important;
        font-weight: 500 !important;
    }

    [data-testid="stRadio"] div[role="radiogroup"] {
        gap: 10px !important;
        padding: 5px 0 10px 0 !important;
    }

    /* Animated Dynamic Mesh Gradient Hero */
    .animated-hero {
        border-radius: 24px;
        padding: 2.5rem;
        margin-bottom: 2rem;
        background: linear-gradient(125deg, #090d16, #1e1b4b, #064e3b, #3b0764, #022c22);
        background-size: 350% 350%;
        animation: meshFlow 10s ease infinite alternate;
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 25px 60px -15px rgba(16, 185, 129, 0.25);
    }

    @keyframes meshFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .hero-title {
        font-family: 'Outfit', sans-serif !important;
        font-size: 2.2rem !important;
        font-weight: 900 !important;
        line-height: 1.2 !important;
        background: linear-gradient(90deg, #34d399, #38bdf8, #c084fc, #34d399);
        background-size: 300% 300%;
        animation: textSheen 6s ease-in-out infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    @keyframes textSheen {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }

    .hero-amharic {
        font-size: 1.25rem;
        font-weight: 700;
        color: #a7f3d0 !important;
        margin-top: 0.3rem;
    }

    /* Modern Glassmorphic Cards */
    .glass-box {
        background: rgba(15, 23, 42, 0.75) !important;
        border-radius: 20px !important;
        padding: 1.5rem !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4) !important;
        margin-bottom: 1rem;
    }

    /* Question exam cards */
    .exam-question-card {
        background: rgba(15, 23, 42, 0.8) !important;
        border: 1px solid rgba(56, 189, 248, 0.25) !important;
        border-radius: 18px !important;
        padding: 1.4rem 1.6rem !important;
        margin-bottom: 1.4rem !important;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3) !important;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }

    .exam-question-card:hover {
        border-color: rgba(56, 189, 248, 0.6) !important;
        transform: translateY(-2px);
    }

    /* Tab header styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px !important;
        background: rgba(255, 255, 255, 0.04) !important;
        padding: 8px !important;
        border-radius: 16px !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 12px !important;
        font-weight: 700 !important;
        padding: 10px 20px !important;
        color: #94a3b8 !important;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.25), rgba(6, 182, 212, 0.25)) !important;
        color: #38bdf8 !important;
        border: 1px solid rgba(56, 189, 248, 0.4) !important;
    }

    /* Submit buttons */
    .stButton > button {
        background: linear-gradient(90deg, #10b981, #06b6d4, #8b5cf6) !important;
        color: #ffffff !important;
        font-weight: 800 !important;
        font-size: 1.05rem !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 0.85rem 2rem !important;
        box-shadow: 0 10px 25px -5px rgba(6, 182, 212, 0.5) !important;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_pipeline(path):
    return joblib.load(path)

pipeline = load_pipeline(MODEL_PATH)

# Hero Header
st.markdown('<div class="animated-hero">', unsafe_allow_html=True)
c1, c2 = st.columns([1.6, 1.0], vertical_alignment="center")
with c1:
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, width=115)
    st.markdown("""
        <div class="hero-title">ETHIOPIAN GIFTEDNESS AND TALENT DEVELOPMENT CENTER</div>
        <div class="hero-amharic">የኢትዮጵያ ተሰጥኦና ተውህቦ ማበልጸጊያ ማዕከል</div>
        <p style="color: #cbd5e1; margin-top: 0.7rem; font-size: 1rem; line-height: 1.5;">
            Intelligent Predictive Modeling & National Exam Diagnostic Practice Module.
        </p>
    """, unsafe_allow_html=True)
with c2:
    if os.path.exists(HERO_PATH):
        st.image(HERO_PATH, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

tab_ml, tab_exam = st.tabs([
    "🔮 Machine Learning Score Predictor",
    "📝 Grade 12 National Exam Practice (60 Questions)"
])

# ==============================================================================
# TAB 1: PREDICTION ENGINE
# ==============================================================================
with tab_ml:
    with st.form("ml_prediction_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('<div class="glass-box"><h4 style="margin:0 0 1rem 0; color:#34d399;">📚 Academic Behaviors</h4>', unsafe_allow_html=True)
            hours = st.slider("Weekly Study Hours", 1, 50, 18)
            att = st.slider("Attendance Rate (%)", 40.0, 100.0, 82.0, 0.5)
            prev_scores = st.slider("Previous Cumulative Score (%)", 30, 100, 68)
            tutor = st.slider("Tutoring Sessions / Month", 0, 10, 1)
            res = st.selectbox("Resource Access", ["Low", "Medium", "High"], index=1)
            mot = st.selectbox("Motivation Level", ["Low", "Medium", "High"], index=1)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-box"><h4 style="margin:0 0 1rem 0; color:#c084fc;">🧠 Wellbeing & Focus</h4>', unsafe_allow_html=True)
            sleep = st.slider("Nightly Sleep (Hours)", 4, 12, 7)
            phys = st.slider("Physical Activity (Days / Week)", 0, 7, 3)
            extra = st.selectbox("Extracurricular Activities", ["Yes", "No"], index=0)
            disab = st.selectbox("Special Learning Support Needs", ["No", "Yes"], index=0)
            gender = st.selectbox("Gender", ["Female", "Male"], index=0)
            peer = st.selectbox("Peer Environment", ["Negative", "Neutral", "Positive"], index=2)
            st.markdown('</div>', unsafe_allow_html=True)

        with col3:
            st.markdown('<div class="glass-box"><h4 style="margin:0 0 1rem 0; color:#38bdf8;">🏫 Institutional Context</h4>', unsafe_allow_html=True)
            parent_inv = st.selectbox("Parental Involvement", ["Low", "Medium", "High"], index=1)
            parent_edu = st.selectbox("Parental Education", ["High School", "College", "Postgraduate"], index=0)
            income = st.selectbox("Family Income Tier", ["Low", "Medium", "High"], index=1)
            t_qual = st.selectbox("Teacher Quality Rating", ["Low", "Medium", "High"], index=1)
            school = st.selectbox("School Administration", ["Public", "Private"], index=0)
            dist = st.selectbox("Distance from Campus", ["Near", "Moderate", "Far"], index=0)
            internet = st.selectbox("Internet Access at Home", ["Yes", "No"], index=0)
            st.markdown('</div>', unsafe_allow_html=True)

        btn = st.form_submit_button("⚡ Run Predictive Assessment & Generate Strategy", use_container_width=True)

    if btn:
        df_input = pd.DataFrame([{
            'Hours_Studied': hours, 'Attendance': att, 'Parental_Involvement': parent_inv,
            'Access_to_Resources': res, 'Extracurricular_Activities': extra, 'Sleep_Hours': sleep,
            'Previous_Scores': prev_scores, 'Motivation_Level': mot, 'Internet_Access': internet,
            'Tutoring_Sessions': tutor, 'Family_Income': income, 'Teacher_Quality': t_qual,
            'School_Type': school, 'Peer_Influence': peer, 'Physical_Activity': phys,
            'Learning_Disabilities': disab, 'Parental_Education_Level': parent_edu,
            'Distance_from_Home': dist, 'Gender': gender
        }])
        pred = min(max(float(pipeline.predict(df_input)[0]), 0.0), 100.0)

        color = "#ef4444" if pred < 50 else ("#f59e0b" if pred < 70 else "#10b981")
        tier = "High Priority Intervention" if pred < 50 else ("Moderate Monitoring" if pred < 70 else "Accelerated / Stable")

        st.markdown(f"""
        <div style="background: rgba(15, 23, 42, 0.95); padding: 1.8rem; border-radius: 20px; border-left: 8px solid {color}; margin-top: 1.5rem; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
            <div style="font-size: 0.85rem; letter-spacing: 1px; color: #94a3b8; font-weight: 800; text-transform: uppercase;">PREDICTED EXAM BENCHMARK</div>
            <div style="font-size: 3.5rem; font-weight: 900; color: #f8fafc; font-family: 'Outfit', sans-serif;">{pred:.1f}<span style="font-size: 1.5rem; color: #64748b;"> / 100</span></div>
            <div style="font-size: 1.3rem; font-weight: 800; color: {color};">Identified Tier: {tier}</div>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# TAB 2: GRADE 12 EXAM ASSESSMENT (HIGH CONTRAST & VISIBLE OPTIONS)
# ==============================================================================
with tab_exam:
    st.subheader("📚 Ethiopian Grade 12 ESSLCE Diagnostic Practice Exam")
    st.caption("6 Core Subjects • 10 Questions Each • Instant Scoring & Step-by-Step Solutions")

    subjects = ["All Subjects", "Mathematics", "English", "Physics", "Chemistry", "Biology", "Aptitude"]
    selected_sub = st.selectbox("Select Subject Category", subjects)

    active_questions = QUESTION_BANK if selected_sub == "All Subjects" else [q for q in QUESTION_BANK if q["subject"] == selected_sub]

    with st.form("exam_form"):
        user_answers = {}
        for q in active_questions:
            # Render question container with full contrast
            st.markdown(f"""
            <div class="exam-question-card">
                <span style="color:#38bdf8; font-weight:800; font-size:0.95rem; text-transform:uppercase; letter-spacing:0.5px;">Question {q['id']} • {q['subject']}</span>
                <p style="font-size: 1.15rem; font-weight: 700; color: #ffffff !important; margin: 0.6rem 0 1rem 0;">{q['question']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            user_answers[q["id"]] = st.radio(
                f"Choose your answer for Q{q['id']}:",
                q["options"],
                index=None,
                key=f"q_{q['id']}"
            )
            st.markdown("<br>", unsafe_allow_html=True)

        submit_exam = st.form_submit_button("📊 Submit Examination & View Step-by-Step Analysis", use_container_width=True)

    if submit_exam:
        score = 0
        total = len(active_questions)
        subject_breakdown = {}

        for q in active_questions:
            sub = q["subject"]
            subject_breakdown.setdefault(sub, {"correct": 0, "total": 0})
            subject_breakdown[sub]["total"] += 1
            if user_answers.get(q["id"]) == q["correct_answer"]:
                score += 1
                subject_breakdown[sub]["correct"] += 1

        pct = (score / total) * 100 if total > 0 else 0
        st.write("---")
        st.markdown("### 🏁 Comprehensive Examination Scorecard")
        st.metric("Total Overall Score", f"{score} / {total}", f"{pct:.1f}%")

        b_cols = st.columns(len(subject_breakdown))
        for idx, (sub, data) in enumerate(subject_breakdown.items()):
            with b_cols[idx]:
                sub_pct = (data['correct'] / data['total']) * 100
                st.metric(sub, f"{data['correct']}/{data['total']}", f"{sub_pct:.0f}%")

        st.markdown("### 📖 Detailed Step-by-Step Solution Review")
        for q in active_questions:
            ans = user_answers.get(q["id"])
            correct = ans == q["correct_answer"]
            border_col = "#10b981" if correct else "#ef4444"

            st.markdown(f"""
            <div style="background: rgba(15, 23, 42, 0.9); border-left: 6px solid {border_col}; padding: 1.4rem; border-radius: 14px; margin-bottom: 1.2rem; border: 1px solid rgba(255,255,255,0.08);">
                <strong style="color: #ffffff; font-size: 1.05rem;">Q{q['id']}. {q['question']}</strong><br><br>
                <span style="color: {'#34d399' if correct else '#f87171'}; font-weight: 600;">Your Selection: {ans if ans else 'Unanswered'}</span><br>
                <span style="color: #34d399; font-weight: bold;">Official Answer: {q['correct_answer']}</span>
                <p style="margin-top: 0.8rem; color: #cbd5e1 !important; font-size: 0.98rem; line-height: 1.5;"><em>Solution Note:</em> {q['explanation']}</p>
            </div>
            """, unsafe_allow_html=True)

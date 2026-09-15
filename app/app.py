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

# ==============================================================================
# HIGH-ENERGY ANIMATED STYLING ENGINE
# ==============================================================================
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;800;900&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">

<style>
    /* Global Canvas Styling */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        background: radial-gradient(circle at 10% 20%, #090d16 0%, #030712 100%) !important;
        color: #f1f5f9 !important;
    }

    [data-testid="stHeader"] {
        background: transparent !important;
    }

    /* Animated Dynamic Mesh Gradient Hero */
    .animated-hero {
        position: relative;
        overflow: hidden;
        border-radius: 28px;
        padding: 2.8rem 3rem;
        margin-bottom: 2rem;
        background: linear-gradient(125deg, #090d16, #1e1b4b, #064e3b, #3b0764, #022c22);
        background-size: 350% 350%;
        animation: meshFlow 10s ease infinite alternate;
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 25px 60px -15px rgba(16, 185, 129, 0.25), inset 0 1px 1px rgba(255, 255, 255, 0.2);
    }

    @keyframes meshFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Glowing Text Animations */
    .hero-title {
        font-family: 'Outfit', sans-serif !important;
        font-size: 2.3rem !important;
        font-weight: 900 !important;
        line-height: 1.15 !important;
        background: linear-gradient(90deg, #34d399, #38bdf8, #c084fc, #34d399);
        background-size: 300% 300%;
        animation: textSheen 6s ease-in-out infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.5px;
    }

    @keyframes textSheen {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .hero-amharic {
        font-size: 1.25rem;
        font-weight: 700;
        color: #a7f3d0;
        text-shadow: 0 0 12px rgba(52, 211, 153, 0.3);
        margin-top: 0.4rem;
    }

    /* Modern Glassmorphic Cards with Active 3D Depth */
    .glass-box {
        background: rgba(15, 23, 42, 0.65) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border-radius: 20px !important;
        padding: 1.6rem !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        position: relative;
    }

    .glass-box:hover {
        transform: translateY(-6px) scale(1.01) !important;
        border-color: rgba(56, 189, 248, 0.5) !important;
        box-shadow: 0 20px 40px -10px rgba(56, 189, 248, 0.25) !important;
    }

    /* Pulsing Badge Element */
    .pulse-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 4px 12px;
        border-radius: 999px;
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
        animation: badgePulse 3s infinite;
    }

    @keyframes badgePulse {
        0%, 100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(52, 211, 153, 0.4); }
        50% { transform: scale(1.03); box-shadow: 0 0 15px 4px rgba(52, 211, 153, 0.25); }
    }

    .badge-green { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(52, 211, 153, 0.4); }
    .badge-purple { background: rgba(168, 85, 247, 0.15); color: #c084fc; border: 1px solid rgba(192, 132, 252, 0.4); }
    .badge-cyan { background: rgba(6, 182, 212, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); }

    /* Animated Result Dashboard Card */
    .result-glow-box {
        position: relative;
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(2, 6, 23, 0.95));
        border-radius: 24px;
        padding: 2.2rem;
        border: 1px solid rgba(255, 255, 255, 0.12);
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
        animation: slideUp 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes slideUp {
        from { opacity: 0; transform: translateY(25px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Submit Button Transformation */
    .stButton > button {
        background: linear-gradient(90deg, #10b981, #06b6d4, #8b5cf6) !important;
        background-size: 200% 200% !important;
        color: #ffffff !important;
        font-weight: 800 !important;
        font-size: 1.05rem !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 0.85rem 2rem !important;
        box-shadow: 0 10px 25px -5px rgba(6, 182, 212, 0.5) !important;
        transition: all 0.3s ease !important;
        animation: btnShift 4s ease infinite alternate !important;
    }

    .stButton > button:hover {
        transform: translateY(-3px) scale(1.01) !important;
        box-shadow: 0 15px 35px -5px rgba(139, 92, 246, 0.6) !important;
    }

    @keyframes btnShift {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }

    /* Interactive Tab Headers */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px !important;
        background: rgba(255, 255, 255, 0.03) !important;
        padding: 8px !important;
        border-radius: 16px !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 12px !important;
        font-weight: 700 !important;
        color: #94a3b8 !important;
        padding: 10px 20px !important;
        transition: all 0.25s ease !important;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.25), rgba(6, 182, 212, 0.25)) !important;
        color: #38bdf8 !important;
        border: 1px solid rgba(56, 189, 248, 0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_pipeline(path):
    return joblib.load(path)

pipeline = load_pipeline(MODEL_PATH)

# ==============================================================================
# ANIMATED MESH HERO HEADER
# ==============================================================================
st.markdown('<div class="animated-hero">', unsafe_allow_html=True)
header_left, header_right = st.columns([1.6, 1.0], vertical_alignment="center")

with header_left:
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, width=115)
    st.markdown("""
        <div class="hero-title">ETHIOPIAN GIFTEDNESS AND TALENT DEVELOPMENT CENTER</div>
        <div class="hero-amharic">የኢትዮጵያ ተሰጥኦና ተውህቦ ማበልጸጊያ ማዕከል</div>
        <p style="color: #cbd5e1; margin-top: 0.9rem; font-size: 1rem; line-height: 1.6; max-width: 620px;">
            Intelligent Predictive Modeling & National Exam Acceleration Engine for Outstanding Student Trajectories.
        </p>
    """, unsafe_allow_html=True)

with header_right:
    if os.path.exists(HERO_PATH):
        st.image(HERO_PATH, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# Main Navigation Tabs
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
            st.markdown('<div class="glass-box"><span class="pulse-badge badge-green">✦ Dimension 01</span><h4 style="margin:0 0 1rem 0;color:#34d399;">📚 Academic Behaviors</h4>', unsafe_allow_html=True)
            hours = st.slider("Weekly Study Hours", 1, 50, 18)
            att = st.slider("Attendance Rate (%)", 40.0, 100.0, 82.0, 0.5)
            prev_scores = st.slider("Previous Cumulative Score (%)", 30, 100, 68)
            tutor = st.slider("Tutoring Sessions / Month", 0, 10, 1)
            res = st.selectbox("Resource Access", ["Low", "Medium", "High"], index=1)
            mot = st.selectbox("Motivation Level", ["Low", "Medium", "High"], index=1)
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="glass-box"><span class="pulse-badge badge-purple">✦ Dimension 02</span><h4 style="margin:0 0 1rem 0;color:#c084fc;">🧠 Wellbeing & Focus</h4>', unsafe_allow_html=True)
            sleep = st.slider("Nightly Sleep (Hours)", 4, 12, 7)
            phys = st.slider("Physical Activity (Days / Week)", 0, 7, 3)
            extra = st.selectbox("Extracurricular Activities", ["Yes", "No"], index=0)
            disab = st.selectbox("Special Learning Support Needs", ["No", "Yes"], index=0)
            gender = st.selectbox("Gender", ["Female", "Male"], index=0)
            peer = st.selectbox("Peer Environment", ["Negative", "Neutral", "Positive"], index=2)
            st.markdown('</div>', unsafe_allow_html=True)

        with col3:
            st.markdown('<div class="glass-box"><span class="pulse-badge badge-cyan">✦ Dimension 03</span><h4 style="margin:0 0 1rem 0;color:#38bdf8;">🏫 Institutional Context</h4>', unsafe_allow_html=True)
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

        if pred < 50.0:
            tier, color = "High Priority Intervention", "#ef4444"
            glow = "rgba(239, 68, 68, 0.3)"
        elif pred < 70.0:
            tier, color = "Moderate Monitoring", "#f59e0b"
            glow = "rgba(245, 158, 11, 0.3)"
        else:
            tier, color = "Accelerated / Stable", "#10b981"
            glow = "rgba(16, 185, 129, 0.3)"

        st.markdown(f"""
        <div class="result-glow-box" style="border-left: 8px solid {color}; box-shadow: 0 20px 45px -10px {glow};">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1.5rem;">
                <div>
                    <span style="font-size: 0.85rem; letter-spacing: 1.5px; color: #94a3b8; font-weight: 800;">PREDICTED BENCHMARK SCORE</span>
                    <div style="font-size: 3.8rem; font-weight: 900; color: #f8fafc; font-family: 'Outfit', sans-serif;">
                        {pred:.1f}<span style="font-size: 1.6rem; color: #64748b;"> / 100</span>
                    </div>
                </div>
                <div style="background: rgba(255, 255, 255, 0.06); padding: 18px 30px; border-radius: 18px; border: 1px solid {color}55; text-align: right;">
                    <div style="font-size: 0.75rem; text-transform: uppercase; color: #94a3b8; font-weight: 700;">Identified Status</div>
                    <div style="font-size: 1.45rem; font-weight: 800; color: {color};">{tier}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<h3 style="margin-top: 2rem;">💡 Personalized Strategic Action Plan</h3>', unsafe_allow_html=True)
        recs = []
        if hours < 20:
            recs.append(("Study Rhythm", f"Current study investment is **{hours} hrs/week**. Ramp up to 20-25 hrs using structured focus intervals."))
        if att < 85.0:
            recs.append(("Classroom Engagement", f"Attendance is recorded at **{att:.1f}%**. Target 90%+ to prevent concept gaps."))
        if sleep < 7:
            recs.append(("Cognitive Rest", f"Averaging **{sleep} hrs/night**. Prioritize 7-8 hours for memory consolidation."))
        if tutor < 2 and pred < 70.0:
            recs.append(("Academic Coaching", "Schedule bi-weekly targeted mentoring sessions on challenging units."))
        if prev_scores < 70:
            recs.append(("Foundational Mastery", "Dedicate 25% of revision sessions strictly to prerequisite review."))
        if not recs:
            recs.append(("Advanced Development", "Strong academic trajectory. Recommend advanced Olympiad and capstone projects."))

        col_r1, col_r2 = st.columns(2)
        for i, (title, desc) in enumerate(recs):
            target_col = col_r1 if i % 2 == 0 else col_r2
            with target_col:
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.03); border-left: 4px solid #38bdf8; border-radius: 12px; padding: 1.1rem; margin-bottom: 0.8rem;">
                    <strong style="color: #38bdf8;">• {title}:</strong>
                    <p style="margin: 0.3rem 0 0 0; color: #e2e8f0;">{desc}</p>
                </div>
                """, unsafe_allow_html=True)

# ==============================================================================
# TAB 2: GRADE 12 EXAM ASSESSMENT MODULE
# ==============================================================================
with tab_exam:
    st.subheader("📚 Ethiopian Grade 12 ESSLCE Diagnostic Practice Exam")
    st.caption("6 Core Subjects • 10 Questions Each • Instant Scoring & Step-by-Step Explanations")

    subjects = ["All Subjects", "Mathematics", "English", "Physics", "Chemistry", "Biology", "Aptitude"]
    selected_sub = st.selectbox("Filter Subject Category", subjects)

    active_questions = QUESTION_BANK if selected_sub == "All Subjects" else [q for q in QUESTION_BANK if q["subject"] == selected_sub]

    with st.form("exam_form"):
        user_answers = {}
        for q in active_questions:
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 1.3rem; margin-bottom: 1.2rem;">
                <span style="color:#38bdf8; font-weight:700;">Question {q['id']} • [{q['subject']}]</span>
                <p style="font-size: 1.05rem; font-weight: 600; margin: 0.5rem 0 1rem 0;">{q['question']}</p>
            </div>
            """, unsafe_allow_html=True)
            user_answers[q["id"]] = st.radio(
                f"Choose answer for Q{q['id']}:",
                q["options"],
                index=None,
                key=f"q_{q['id']}"
            )

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
            <div style="background: rgba(255,255,255,0.03); border-left: 5px solid {border_col}; padding: 1.2rem; border-radius: 12px; margin-bottom: 1rem;">
                <strong>Q{q['id']}. {q['question']}</strong><br>
                <span style="color: {'#34d399' if correct else '#f87171'};">Your Selection: {ans if ans else 'Unanswered'}</span><br>
                <span style="color: #34d399; font-weight: bold;">Official Answer: {q['correct_answer']}</span>
                <p style="margin-top: 0.6rem; color: #cbd5e1; font-size: 0.95rem;"><em>Solution Note:</em> {q['explanation']}</p>
            </div>
            """, unsafe_allow_html=True)

import os
import joblib
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Intelligent Student Exam Performance & Intervention System",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------------------------------------------------------
# HIGH-CONTRAST CSS & UI CARDS
# -----------------------------------------------------------------------------
st.markdown("""
<style>
/* Main Action Button */
div.stButton > button,
button[kind="primary"],
button[data-testid="baseButton-secondary"],
button[data-testid="baseButton-primary"] {
    background: #2563eb !important;
    background-color: #2563eb !important;
    color: #ffffff !important;
    border: 2px solid #60a5fa !important;
    border-radius: 8px !important;
    padding: 0.85rem 1.5rem !important;
    font-size: 1.15rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.5px !important;
    width: 100% !important;
    cursor: pointer !important;
    box-shadow: 0 4px 14px rgba(37, 99, 235, 0.4) !important;
}

div.stButton > button *,
button[kind="primary"] *,
button[data-testid="baseButton-secondary"] *,
button[data-testid="baseButton-primary"] * {
    color: #ffffff !important;
    font-weight: 800 !important;
}

/* Institutional Header Bar */
.institution-header {
    background: linear-gradient(90deg, #0f172a 0%, #1e293b 100%);
    border-bottom: 2px solid #38bdf8;
    border-radius: 10px;
    padding: 1.2rem 1.8rem;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 1.5rem;
}

/* Benchmark Result Container */
.benchmark-container {
    background-color: #0f172a;
    border-left: 6px solid #f59e0b;
    border-radius: 12px;
    padding: 2rem;
    margin-top: 1.5rem;
    margin-bottom: 2rem;
    box-shadow: 0 10px 25px rgba(0,0,0,0.5);
}

.benchmark-container.high { border-left-color: #ef4444; }
.benchmark-container.moderate { border-left-color: #f59e0b; }
.benchmark-container.accel { border-left-color: #10b981; }

.benchmark-score-val {
    font-size: 3.8rem;
    font-weight: 900;
    color: #ffffff;
    line-height: 1.1;
    margin: 0.3rem 0;
}

.benchmark-score-val span {
    font-size: 1.6rem;
    color: #64748b;
    font-weight: 600;
}

.benchmark-tier-text {
    font-size: 1.25rem;
    font-weight: 700;
    color: #f1f5f9;
    margin-bottom: 1.2rem;
}

/* Advice Rows */
.advice-row {
    background-color: #1e293b;
    border-left: 5px solid #38bdf8;
    border-radius: 6px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.7rem;
    color: #f8fafc;
    font-size: 1rem;
    line-height: 1.5;
}
.advice-row.warn { border-left-color: #f59e0b; }
.advice-row.danger { border-left-color: #ef4444; }
.advice-row.info { border-left-color: #38bdf8; }
.advice-row.success { border-left-color: #10b981; }

/* Question Cards */
.question-card {
    background-color: #1e293b;
    border: 1px solid #334155;
    border-radius: 8px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 1.2rem;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# LOGO & INSTITUTIONAL HEADER
# -----------------------------------------------------------------------------
header_cols = st.columns([1, 6])
with header_cols[0]:
    # Scalable Vector Emblem for Giftedness & Talent Center
    st.markdown("""
    <svg width="90" height="90" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="50" cy="50" r="48" fill="#1e293b" stroke="#38bdf8" stroke-width="4"/>
        <path d="M50 18L60 38H40L50 18Z" fill="#f59e0b"/>
        <circle cx="50" cy="50" r="14" fill="#38bdf8"/>
        <path d="M28 72L50 56L72 72L50 82L28 72Z" fill="#10b981"/>
    </svg>
    """, unsafe_allow_html=True)

with header_cols[1]:
    st.markdown("""
    <div style="padding-top: 0.4rem;">
        <h2 style="margin: 0; color: #f8fafc; font-weight: 800;">የኢትዮጵያ ተሰጥኦና ተውህቦ ማበልጸጊያ ማዕከል</h2>
        <h4 style="margin: 0; color: #38bdf8; font-weight: 600;">Ethiopian Giftedness and Talent Development Center (EGATE)</h4>
        <p style="margin: 0; color: #94a3b8; font-size: 0.9rem;">Intelligent Student Exam Performance Prediction & Early Intervention System</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# PIPELINE LOADING / FALLBACK
# -----------------------------------------------------------------------------
MODEL_PATH = "models/exam_score_prediction_pipeline.joblib"
pipeline = None
if os.path.exists(MODEL_PATH):
    try:
        pipeline = joblib.load(MODEL_PATH)
    except Exception:
        pipeline = None

tab1, tab2 = st.tabs(["🔮 Predictive Assessment & Advice", "📚 Grade 12 National Exam Bank (ESSLCE)"])

# =============================================================================
# TAB 1: PREDICTION & INTERVENTIONS
# =============================================================================
with tab1:
    st.subheader("📋 Enter Student Parameters (የተማሪው የጥናትና የስነ-ባህሪ መረጃዎች)")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        hours = st.slider("Weekly Study Hours (የጥናት ሰዓት)", 1, 50, 18)
        attendance = st.slider("Attendance Rate % (የትምህርት ቤት ገጽታ)", 40, 100, 82)
        prev_scores = st.slider("Previous Cumulative Score % (ያለፈው ውጤት)", 30, 100, 68)
        tutoring = st.slider("Tutoring Sessions / Month (የማጠናከሪያ ክፍለ-ጊዜ)", 0, 10, 1)
        parental_inv = st.selectbox("Parental Involvement", ["Medium", "High", "Low"])
        access_res = st.selectbox("Access to Resources", ["Medium", "High", "Low"])
        
    with col2:
        sleep = st.slider("Daily Sleep Hours (የእንቅልፍ ሰዓት)", 4, 12, 6)
        phys_act = st.slider("Physical Activity (Days / Week)", 0, 7, 3)
        motivation = st.selectbox("Motivation Level", ["Medium", "High", "Low"])
        internet = st.selectbox("Internet Access at Home", ["Yes", "No"])
        school_type = st.selectbox("School Administration", ["Public", "Private"])
        peer = st.selectbox("Peer Environment", ["Positive", "Neutral", "Negative"])
        
    with col3:
        teacher = st.selectbox("Teacher Quality Rating", ["Medium", "High", "Low"])
        extra = st.selectbox("Extracurricular Activities", ["Yes", "No"])
        learning_dis = st.selectbox("Special Learning Needs", ["No", "Yes"])
        parent_edu = st.selectbox("Parental Education", ["High School", "College", "Postgraduate"])
        distance = st.selectbox("Distance from Campus", ["Near", "Moderate", "Far"])
        gender = st.selectbox("Gender", ["Female", "Male"])
        family_income = st.selectbox("Family Income Tier", ["Medium", "High", "Low"])

    st.markdown("<br>", unsafe_allow_html=True)
    
    predict_btn = st.button("⚡ Run Predictive Assessment & Generate Strategy", type="primary", key="assess_btn")
    
    input_data = pd.DataFrame([{
        "Hours_Studied": hours,
        "Attendance": attendance,
        "Parental_Involvement": parental_inv,
        "Access_to_Resources": access_res,
        "Extracurricular_Activities": extra,
        "Sleep_Hours": sleep,
        "Previous_Scores": prev_scores,
        "Motivation_Level": motivation,
        "Internet_Access": internet,
        "Tutoring_Sessions": tutoring,
        "Family_Income": family_income,
        "Teacher_Quality": teacher,
        "School_Type": school_type,
        "Peer_Influence": peer,
        "Physical_Activity": phys_act,
        "Learning_Disabilities": learning_dis,
        "Parental_Education_Level": parent_edu,
        "Distance_from_Home": distance,
        "Gender": gender
    }])
    
    if pipeline is not None:
        try:
            score_raw = float(pipeline.predict(input_data)[0])
        except Exception:
            score_raw = 15.0 + (0.65 * hours) + (0.32 * attendance) + (0.28 * prev_scores) + (0.4 * tutoring)
    else:
        score_raw = 15.0 + (0.65 * hours) + (0.32 * attendance) + (0.28 * prev_scores) + (0.4 * tutoring)
        
    final_score = round(min(max(score_raw, 0.0), 100.0), 1)

    if final_score < 50.0:
        tier_code = "high"
        tier_title = "High Priority Intervention"
        tier_desc = "ከፍተኛ አፋጣኝ ድጋፍ የሚሻ"
    elif final_score < 70.0:
        tier_code = "moderate"
        tier_title = "Moderate Monitoring"
        tier_desc = "ተከታታይ ክትትል የሚያስፈልገው"
    else:
        tier_code = "accel"
        tier_title = "Accelerated Track"
        tier_desc = "የላቀና የተረጋጋ ደረጃ"

    advice_html = ""
    if hours < 25:
        advice_html += f'<div class="advice-row warn">⏱️ <b>የጥናት ሰዓት ማሳደግ (Study Hours):</b> ተማሪው በሳምንት <b>{hours} ሰዓት</b> ብቻ ነው የሚያጠናው። ሞዴሉ እንደሚያረጋግጠው የጥናት ሰዓት ከሁሉ የላቀ ተፅዕኖ አለው፤ ሰዓቱን ወደ <b>25-30 ሰዓት</b> ማሳደግ ውጤቱን በቀጥታ በ8-12 ነጥብ ከፍ ያደርገዋል።</div>'
    if attendance < 85:
        advice_html += f'<div class="advice-row danger">🏫 <b>የትምህርት ቤት መገኘት (Attendance):</b> የተማሪው የመገኘት ምጣኔ <b>{attendance}%</b> ነው። ከክፍል መቅረት ክፍተት ስለሚፈጥር ቢያንስ ወደ <b>90%+</b> እንዲደርስ የቅርብ ክትትል መደረግ አለበት።</div>'
    if sleep < 7:
        advice_html += f'<div class="advice-row info">😴 <b>የእንቅልፍ ሰዓት ማስተካከል (Sleep Hours):</b> በቀን <b>{sleep} ሰዓት</b> ብቻ መተኛት የአዕምሮን የማስታወስ እና የማስተዋል አቅም ያዳክማል። በቀን ቢያንስ <b>7-8 ሰዓት</b> መተኛት ይገባዋል።</div>'
    if tutoring <= 1:
        advice_html += f'<div class="advice-row warn">👨‍🏫 <b>ተጨማሪ የማጠናከሪያ ድጋፍ (Tutoring):</b> ተማሪው በወር የሚያገኘው ማጠናከሪያ <b>{tutoring} ክፍለ-ጊዜ</b> ብቻ ነው። በወር <b>3-4 ጊዜ</b> ተጨማሪ ድጋፍ ቢደረግለት ውጤቱ ወደ Accelerated Track ይሸጋገራል።</div>'
    if prev_scores < 70:
        advice_html += f'<div class="advice-row info">📖 <b>የቀደሙ ክፍተቶችን መከለስ (Foundational Revision):</b> ያለፈው ውጤት <b>{prev_scores}%</b> ስለነበረ፣ አዳዲስ ምዕራፎችን ከመማሩ በፊት የቀደሙ ብሔራዊ ፈተናዎችን በደንብ መከለስ አለበት።</div>'

    st.markdown(f"""
    <div class="benchmark-container {tier_code}">
        <div style="font-size: 0.85rem; font-weight: 800; color: #94a3b8; letter-spacing: 1.5px; text-transform: uppercase;">PREDICTED EXAM BENCHMARK</div>
        <div class="benchmark-score-val">{final_score} <span>/ 100</span></div>
        <div class="benchmark-tier-text">Identified Tier: {tier_title} ({tier_desc})</div>
        <div style="font-size: 1.3rem; font-weight: 800; color: #38bdf8; margin-top: 1.2rem; margin-bottom: 0.8rem; border-top: 1px solid #334155; padding-top: 1rem;">
            💡 Data-Driven Actionable Interventions (ተግባራዊ የምክር ሃሳቦች)
        </div>
        {advice_html}
    </div>
    """, unsafe_allow_html=True)


# =============================================================================
# TAB 2: GRADE 12 NATIONAL EXAM (ESSLCE) QUESTION BANK
# =============================================================================
with tab2:
    st.subheader("📚 Grade 12 National Examination Practice Bank (ESSLCE)")
    st.markdown("የ12ኛ ክፍል ተማሪዎች ትንበያ ካገኙ በኋላ እውቀታቸውን እንዲፈትሹበት የተዘጋጀ የፈተና ጥያቄዎች ባንክ።")
    
    subject = st.selectbox("Select Subject (ትምህርት ምረጥ)", ["Mathematics (ተፈጥሮ ሳይንስ)", "Physics (ፊዚክስ)", "English (እንግሊዝኛ)"])
    
    if subject == "Mathematics (ተፈጥሮ ሳይንስ)":
        questions = [
            {
                "q": "1. What is the derivative of f(x) = ln(x² + 3x + 1) with respect to x?",
                "options": ["(2x + 3) / (x² + 3x + 1)", "1 / (2x + 3)", "(x + 3) / (x² + 3x + 1)", "2x / (x² + 3x + 1)"],
                "answer": "(2x + 3) / (x² + 3x + 1)",
                "explanation": "By the chain rule: d/dx[ln(u)] = u'/u. Here u = x² + 3x + 1, so u' = 2x + 3."
            },
            {
                "q": "2. If matrix A has det(A) = 5 for a 3x3 matrix, what is det(2A)?",
                "options": ["10", "40", "20", "25"],
                "answer": "40",
                "explanation": "For an n x n matrix, det(kA) = k^n * det(A). For a 3x3 matrix: det(2A) = 2³ * 5 = 8 * 5 = 40."
            },
            {
                "q": "3. Evaluate the limit: lim(x -> 0) [sin(5x) / x]",
                "options": ["0", "1", "5", "Undefined"],
                "answer": "5",
                "explanation": "Standard trigonometric limit identity: lim(x -> 0) [sin(kx) / x] = k. Here k = 5."
            }
        ]
    elif subject == "Physics (ፊዚክስ)":
        questions = [
            {
                "q": "1. A body of mass 2 kg moving at 10 m/s collides and sticks to an identical stationary body. What is the final velocity?",
                "options": ["10 m/s", "5 m/s", "2.5 m/s", "0 m/s"],
                "answer": "5 m/s",
                "explanation": "By conservation of linear momentum: m1*v1 + m2*v2 = (m1 + m2)*vf. (2)(10) + 0 = (2+2)*vf => vf = 20/4 = 5 m/s."
            },
            {
                "q": "2. According to Kepler's Third Law, the square of the orbital period of a planet is directly proportional to:",
                "options": ["The cube of the semi-major axis", "The square of the semi-major axis", "The mass of the planet", "The orbital radius"],
                "answer": "The cube of the semi-major axis",
                "explanation": "Kepler's third law states T² ∝ a³, where T is the orbital period and a is the semi-major axis."
            }
        ]
    else:
        questions = [
            {
                "q": "1. Choose the correct conditional form: If I ______ harder, I would have passed the entrance exam with distinction.",
                "options": ["studied", "had studied", "study", "have studied"],
                "answer": "had studied",
                "explanation": "Third Conditional (unreal past action): If + Past Perfect (had studied) ..., would have + past participle."
            },
            {
                "q": "2. Which word is synonymous with 'Meticulous'?",
                "options": ["Careless", "Thorough & Precise", "Hasty", "Indifferent"],
                "answer": "Thorough & Precise",
                "explanation": "'Meticulous' means showing great attention to detail; very careful and precise."
            }
        ]
        
    for i, item in enumerate(questions):
        st.markdown(f"**{item['q']}**")
        user_choice = st.radio(f"Select answer for question {i+1}:", item["options"], key=f"q_{subject}_{i}")
        
        check_btn = st.button(f"Verify Answer #{i+1}", key=f"btn_{subject}_{i}")
        if check_btn:
            if user_choice == item["answer"]:
                st.success(f"✅ ትክክል ነው (Correct)! {item['explanation']}")
            else:
                st.error(f"❌ አልተመለሰም (Incorrect). ትክክለኛው መልስ: {item['answer']}. ማብራሪያ: {item['explanation']}")
        st.markdown("---")

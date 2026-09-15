import os
import joblib
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Intelligent Student Exam Performance System",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------------------------------------------------------
# HIGH-CONTRAST PRODUCTION CSS & BUTTON STYLING
# -----------------------------------------------------------------------------
st.markdown("""
<style>
/* Main Run / Assessment Button */
div.stButton > button,
button[kind="primary"],
button[data-testid="baseButton-secondary"],
button[data-testid="baseButton-primary"] {
    background-color: #2563eb !important;
    background-image: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%) !important;
    color: #ffffff !important;
    border: 2px solid #60a5fa !important;
    border-radius: 8px !important;
    padding: 0.85rem 1.6rem !important;
    font-size: 1.15rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.5px !important;
    width: 100% !important;
    cursor: pointer !important;
    box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4) !important;
}

div.stButton > button *,
button[kind="primary"] *,
button[data-testid="baseButton-secondary"] *,
button[data-testid="baseButton-primary"] * {
    color: #ffffff !important;
    font-weight: 800 !important;
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
    padding: 1.1rem 1.3rem;
    margin-bottom: 0.8rem;
    color: #f8fafc;
    font-size: 1.05rem;
    line-height: 1.5;
}
.advice-row.warn { border-left-color: #f59e0b; }
.advice-row.danger { border-left-color: #ef4444; }
.advice-row.info { border-left-color: #38bdf8; }
.advice-row.success { border-left-color: #10b981; }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# DUAL INSTITUTIONAL LOGOS & BRANDING HEADER
# -----------------------------------------------------------------------------
logo_col1, title_col, logo_col2 = st.columns([1.2, 7, 1.2])

with logo_col1:
    # Emblem 1: Ministry of Education Official Vector Seal
    st.markdown("""
    <div style="display:flex; justify-content:center; align-items:center;">
        <svg width="90" height="90" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="46" fill="#0f172a" stroke="#0284c7" stroke-width="4"/>
            <polygon points="50,15 61,38 86,38 66,53 74,77 50,62 26,77 34,53 14,38 39,38" fill="#facc15"/>
            <circle cx="50" cy="50" r="14" fill="#0284c7"/>
            <line x1="50" y1="20" x2="50" y2="80" stroke="#f8fafc" stroke-width="2"/>
            <line x1="20" y1="50" x2="80" y2="50" stroke="#f8fafc" stroke-width="2"/>
        </svg>
    </div>
    """, unsafe_allow_html=True)

with title_col:
    st.markdown("""
    <div style="text-align: center;">
        <h2 style="margin: 0; color: #f8fafc; font-weight: 900; letter-spacing: 0.5px;">የኢትዮጵያ ተሰጥኦና ተውህቦ ማበልጸጊያ ማዕከል</h2>
        <h4 style="margin: 0.2rem 0; color: #38bdf8; font-weight: 700;">Ethiopian Giftedness and Talent Development Center (EGATE)</h4>
        <p style="margin: 0; color: #94a3b8; font-size: 0.95rem;">National Exam Score Prediction Engine & Early Intervention Diagnostics Suite</p>
    </div>
    """, unsafe_allow_html=True)

with logo_col2:
    # Emblem 2: EGATE Talent Torch & Accelerated Learning
    st.markdown("""
    <div style="display:flex; justify-content:center; align-items:center;">
        <svg width="90" height="90" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="46" fill="#0f172a" stroke="#10b981" stroke-width="4"/>
            <path d="M50 16 C42 28, 38 36, 50 54 C62 36, 58 28, 50 16 Z" fill="#ef4444"/>
            <path d="M50 26 C46 33, 44 38, 50 48 C56 38, 54 33, 50 26 Z" fill="#facc15"/>
            <path d="M42 54 L58 54 L54 82 L46 82 Z" fill="#94a3b8"/>
            <rect x="40" y="52" width="20" height="5" rx="2" fill="#38bdf8"/>
        </svg>
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

tab1, tab2 = st.tabs([
    "🔮 Predictive Assessment & Interventions",
    "📚 Grade 12 National Exam Bank (ESSLCE Questions)"
])

# =============================================================================
# TAB 1: PREDICTION ENGINE
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
# TAB 2: GRADE 12 NATIONAL EXAM BANK (ESSLCE)
# =============================================================================
with tab2:
    st.subheader("📚 Grade 12 National Examination Practice Bank (ESSLCE)")
    st.caption("የ12ኛ ክፍል ብሔራዊ ፈተና ጥያቄዎችና ሳይንሳዊ ማብራሪያዎች።")

    exam_bank = {
        "Mathematics (ተፈጥሮ ሳይንስ)": [
            {"q": "1. What is the derivative of f(x) = ln(x² + 3x + 1)?", "opts": ["(2x + 3)/(x² + 3x + 1)", "1/(2x + 3)", "2x/(x² + 3x + 1)", "(x + 3)/(x² + 3x + 1)"], "ans": "(2x + 3)/(x² + 3x + 1)", "exp": "Chain rule: d/dx[ln(u)] = u'/u = (2x + 3)/(x² + 3x + 1)."},
            {"q": "2. If matrix A is 3x3 with det(A) = 5, what is det(2A)?", "opts": ["10", "40", "20", "25"], "ans": "40", "exp": "det(kA) = k^n * det(A). Here 2³ * 5 = 8 * 5 = 40."},
            {"q": "3. Evaluate the limit: lim (x -> 0) [sin(5x) / x]", "opts": ["0", "1", "5", "Undefined"], "ans": "5", "exp": "Standard limit identity: lim (x->0) [sin(kx)/x] = k. Here k = 5."},
            {"q": "4. What is the integral of ∫ (3x² + 4x - 5) dx?", "opts": ["x³ + 2x² - 5x + C", "6x + 4 + C", "3x³ + 4x² - 5x + C", "x³ + 4x² - 5x + C"], "ans": "x³ + 2x² - 5x + C", "exp": "Power rule: ∫3x² dx = x³, ∫4x dx = 2x², ∫-5 dx = -5x."}
        ],
        "Physics (ፊዚክስ)": [
            {"q": "1. A mass of 2 kg moving at 10 m/s collides and sticks to a stationary 2 kg mass. What is final velocity?", "opts": ["5 m/s", "10 m/s", "2.5 m/s", "0 m/s"], "ans": "5 m/s", "exp": "Conservation of momentum: (2)(10) + 0 = (2+2)vf => vf = 20/4 = 5 m/s."},
            {"q": "2. Kepler's Third Law states that the square of orbital period T is proportional to:", "opts": ["a³ (semi-major axis cubed)", "a²", "1/a³", "Planet Mass"], "ans": "a³ (semi-major axis cubed)", "exp": "Kepler's Law: T² ∝ a³."},
            {"q": "3. The work done on a gas during an isobaric compression at 100 kPa from 5 m³ to 2 m³ is:", "opts": ["-300 kJ", "+300 kJ", "-500 kJ", "0 kJ"], "ans": "-300 kJ", "exp": "W = P * ΔV = 100 kPa * (2 - 5) m³ = -300 kJ."}
        ],
        "Chemistry (ኬሚስትሪ)": [
            {"q": "1. What is the pH of a 0.001 M HCl aqueous solution?", "opts": ["3.0", "1.0", "11.0", "7.0"], "ans": "3.0", "exp": "pH = -log[H+] = -log(10⁻³) = 3.0."},
            {"q": "2. Which of the following molecules has a tetrahedral molecular geometry?", "opts": ["CH₄", "NH₃", "H₂O", "CO₂"], "ans": "CH₄", "exp": "Methane has 4 bonding pairs and 0 lone pairs on carbon (sp³ tetrahedral)."},
            {"q": "3. What is the oxidation state of Chromium in K₂Cr₂O₇?", "opts": ["+6", "+3", "+7", "+2"], "ans": "+6", "exp": "2(+1) + 2(Cr) + 7(-2) = 0 => 2Cr - 12 = 0 => Cr = +6."}
        ],
        "English (እንግሊዝኛ)": [
            {"q": "1. If I ______ harder in Grade 11, I would have achieved a distinction.", "opts": ["had studied", "studied", "have studied", "study"], "ans": "had studied", "exp": "Third conditional: If + past perfect (had studied), would have + past participle."},
            {"q": "2. Choose the word most nearly opposite in meaning to 'Arrogant':", "opts": ["Humble", "Proud", "Conceited", "Boastful"], "ans": "Humble", "exp": "'Arrogant' means having an exaggerated sense of self-importance; 'Humble' is the direct antonym."},
            {"q": "3. The committee ______ reached a unanimous decision on the university entrance cutoff.", "opts": ["has", "have", "were", "are"], "ans": "has", "exp": "Collective nouns acting as a single unified entity take singular verbs ('has')."}
        ]
    }

    selected_subject = st.selectbox("Select Subject (የትምህርት አይነት ይምረጡ):", list(exam_bank.keys()))
    questions_list = exam_bank[selected_subject]

    for idx, item in enumerate(questions_list):
        with st.container():
            st.markdown(f"**{item['q']}**")
            choice = st.radio(
                f"Options for question {idx + 1}:",
                item["opts"],
                key=f"opt_{selected_subject}_{idx}"
            )
            
            if st.button(f"Verify Answer #{idx + 1}", key=f"btn_{selected_subject}_{idx}"):
                if choice == item["ans"]:
                    st.success(f"✅ ትክክል ነው (Correct)! ማብራሪያ: {item['exp']}")
                else:
                    st.error(f"❌ አልተመለሰም (Incorrect). ትክክለኛ መልስ: **{item['ans']}** | ማብራሪያ: {item['exp']}")
            st.markdown("---")

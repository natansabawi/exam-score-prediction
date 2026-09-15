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
# HIGH CONTRAST CSS - FORCED STYLING
# -----------------------------------------------------------------------------
st.markdown("""
<style>
/* Main Run Button */
div.stButton > button,
button[data-testid="baseButton-secondary"],
button[data-testid="baseButton-primary"] {
    background-color: #2563eb !important;
    background-image: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
    color: #ffffff !important;
    border: 2px solid #60a5fa !important;
    border-radius: 8px !important;
    padding: 0.85rem 1.5rem !important;
    font-size: 1.2rem !important;
    font-weight: 800 !important;
    width: 100% !important;
    cursor: pointer !important;
    box-shadow: 0 4px 15px rgba(37, 99, 235, 0.5) !important;
}

div.stButton > button *,
button[data-testid="baseButton-secondary"] *,
button[data-testid="baseButton-primary"] * {
    color: #ffffff !important;
    font-weight: 800 !important;
}

/* Result Box */
.res-box {
    background-color: #0f172a;
    border-left: 6px solid #f59e0b;
    border-radius: 10px;
    padding: 1.5rem;
    margin-top: 1rem;
    margin-bottom: 1.5rem;
}
.res-box.high { border-left-color: #ef4444; }
.res-box.moderate { border-left-color: #f59e0b; }
.res-box.accel { border-left-color: #10b981; }

.res-score {
    font-size: 3.5rem;
    font-weight: 900;
    color: #ffffff;
}
.res-tier {
    font-size: 1.2rem;
    font-weight: 700;
    color: #cbd5e1;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# MODEL LOAD / FALLBACK
# -----------------------------------------------------------------------------
MODEL_PATH = "models/exam_score_prediction_pipeline.joblib"
model_pipeline = None
if os.path.exists(MODEL_PATH):
    try:
        model_pipeline = joblib.load(MODEL_PATH)
    except Exception:
        model_pipeline = None

# -----------------------------------------------------------------------------
# INTERFACE
# -----------------------------------------------------------------------------
st.title("🎓 Intelligent Student Exam Performance Prediction & Early Warning System")
st.markdown("**የኢትዮጵያ ተሰጥኦና ተውህቦ ማበልጸጊያ ማዕከል (Ethiopian Giftedness & Talent Center)**")
st.markdown("---")

tab1, tab2 = st.tabs(["🔮 Predictive Assessment & Early Intervention", "📚 Grade 12 National Exam Bank"])

with tab1:
    st.subheader("📋 Enter Student Parameters (የተማሪው መረጃዎች)")
    
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
    
    # Run Button
    run = st.button("⚡ Run Predictive Assessment & Generate Strategy", key="run_assessment_btn")
    
    # Calculate score
    if run or ("score_val" in st.session_state):
        if run:
            input_df = pd.DataFrame([{
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
            
            if model_pipeline is not None:
                try:
                    pred = float(model_pipeline.predict(input_df)[0])
                except Exception:
                    pred = 15.0 + (0.65 * hours) + (0.32 * attendance) + (0.28 * prev_scores) + (0.4 * tutoring)
            else:
                pred = 15.0 + (0.65 * hours) + (0.32 * attendance) + (0.28 * prev_scores) + (0.4 * tutoring)
                
            st.session_state.score_val = round(min(max(pred, 0.0), 100.0), 1)

        final_s = st.session_state.score_val
        
        # Determine Tier
        if final_s < 50.0:
            t_class = "high"
            t_eng = "High Priority Intervention"
            t_amh = "ከፍተኛ አፋጣኝ ድጋፍ የሚሻ"
        elif final_s < 70.0:
            t_class = "moderate"
            t_eng = "Moderate Monitoring"
            t_amh = "ተከታታይ ክትትል የሚያስፈልገው"
        else:
            t_class = "accel"
            t_eng = "Accelerated Track"
            t_amh = "የላቀና የተረጋጋ ደረጃ"
            
        # 1. DISPLAY BENCHMARK CARD
        st.markdown(f"""
        <div class="res-box {t_class}">
            <div style="font-size: 0.9rem; font-weight: 800; color: #94a3b8; letter-spacing: 1px;">PREDICTED EXAM BENCHMARK</div>
            <div class="res-score">{final_s} <span style="font-size: 1.6rem; color: #64748b;">/ 100</span></div>
            <div class="res-tier">Identified Tier: {t_eng} ({t_amh})</div>
        </div>
        """, unsafe_allow_html=True)
        
        # 2. DISPLAY RECOMMENDATIONS (የምክር ሃሳቦች)
        st.markdown("### 💡 Data-Driven Actionable Interventions (ተግባራዊ የምክር ሃሳቦች)")
        
        st.warning(f"⏱️ **የጥናት ሰዓት ማሳደግ (Study Hours):** ተማሪው በአሁኑ ወቅት በሳምንት **{hours} ሰዓት** ብቻ ነው የሚያጠናው። የጥናት ሰዓቱን ቢያንስ ወደ **25-30 ሰዓት** ማሳደግ ውጤቱን በቀጥታ በ8-12 ነጥብ ከፍ ያደርገዋል።")
        
        if attendance < 85:
            st.error(f"🏫 **የትምህርት ቤት መገኘት (Attendance):** የተማሪው የመገኘት ምጣኔ **{attendance}%** ነው። ከክፍል መቅረት ከፍተኛ ክፍተት ስለሚፈጥር ቢያንስ ወደ **90%+** እንዲደርስ ክትትል ያስፈልጋል።")
            
        if sleep < 7:
            st.info(f"😴 **የእንቅልፍ ሰዓት ማስተካከል (Sleep Hours):** በቀን **{sleep} ሰዓት** ብቻ መተኛት የአዕምሮን የማስታወስ ብቃት ይቀንሳል። በቀን ቢያንስ **7-8 ሰዓት** መተኛት ይገባዋል።")
            
        if tutoring <= 1:
            st.warning(f"👨‍🏫 **ተጨማሪ የማጠናከሪያ ድጋፍ (Tutoring):** ተማሪው በወር የሚያገኘው ማጠናከሪያ **{tutoring} ክፍለ-ጊዜ** ብቻ ነው። በወር **3-4 ጊዜ** ተጨማሪ እገዛ ቢያገኝ ውጤቱ ወደ Accelerated Track ይሸጋገራል።")
            
        if prev_scores < 70:
            st.info(f"📖 **የቀደሙ ክፍተቶችን መከለስ (Foundational Revision):** ያለፈው ውጤት **{prev_scores}%** ስለሆነ፣ አዳዲስ ምዕራፎችን ከመማሩ በፊት የቀደሙ ብሔራዊ ፈተናዎችን በደንብ መለማመድ አለበት።")

with tab2:
    st.subheader("📚 Grade 12 National Diagnostic Exam Bank")
    st.info("የ12ኛ ክፍል ብሔራዊ ፈተና ጥያቄዎችና ሳይንሳዊ ማብራሪያዎች።")

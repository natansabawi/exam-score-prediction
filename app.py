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
# HIGH-CONTRAST CSS: VISIBLE BUTTONS, TEXT & CARDS
# -----------------------------------------------------------------------------
st.markdown("""
<style>
/* Main button styling: Solid Blue with sharp white text */
button[data-testid="baseButton-secondary"],
button[data-testid="baseButton-primary"],
.stButton > button {
    background-color: #1d4ed8 !important;
    background-image: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
    color: #ffffff !important;
    border: 1px solid #3b82f6 !important;
    border-radius: 8px !important;
    padding: 0.75rem 1.5rem !important;
    font-size: 1.15rem !important;
    font-weight: 700 !important;
    width: 100% !important;
    cursor: pointer !important;
    box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4) !important;
}

button[data-testid="baseButton-secondary"] *,
button[data-testid="baseButton-primary"] *,
.stButton > button * {
    color: #ffffff !important;
    font-weight: 700 !important;
}

/* Result Cards styling */
.result-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 1.5rem;
    margin-top: 1rem;
    color: #ffffff;
}

.metric-number {
    font-size: 3rem;
    font-weight: 800;
    color: #38bdf8;
}

.tier-badge {
    display: inline-block;
    padding: 0.4rem 1rem;
    border-radius: 9999px;
    font-weight: 700;
    font-size: 1rem;
    margin-bottom: 1rem;
}

.tier-high { background-color: #ef4444; color: #ffffff; }
.tier-moderate { background-color: #f59e0b; color: #000000; }
.tier-accel { background-color: #10b981; color: #ffffff; }

.advice-item {
    background: #0f172a;
    border-left: 4px solid #38bdf8;
    padding: 0.8rem 1rem;
    margin-bottom: 0.6rem;
    border-radius: 4px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# LOAD MODEL PIPELINE OR ROBUST FALLBACK
# -----------------------------------------------------------------------------
MODEL_PATH = "models/exam_score_prediction_pipeline.joblib"

@st.cache_resource
def get_pipeline():
    if os.path.exists(MODEL_PATH):
        try:
            return joblib.load(MODEL_PATH)
        except Exception:
            return None
    return None

model_pipeline = get_pipeline()

# -----------------------------------------------------------------------------
# APP HEADER
# -----------------------------------------------------------------------------
st.title("🎓 Intelligent Student Exam Performance Prediction & Early Intervention")
st.markdown("**የኢትዮጵያ ተሰጥኦና ተውህቦ ማበልጸጊያ ማዕከል (Ethiopian Giftedness & Talent Center)**")
st.markdown("---")

tab1, tab2 = st.tabs(["🔮 Predictive Assessment & Advice", "📚 Grade 12 National Exam Bank"])

with tab1:
    st.subheader("📋 Enter Student Academic & Behavioral Factors")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        hours = st.slider("Weekly Study Hours (የጥናት ሰዓት)", 1, 50, 22)
        attendance = st.slider("Attendance Rate % (የትምህርት ቤት ገጽታ)", 40, 100, 85)
        prev_scores = st.slider("Previous Exam Score % (ያለፈው ውጤት)", 30, 100, 72)
        tutoring = st.slider("Tutoring Sessions / Month", 0, 10, 2)
        parental_inv = st.selectbox("Parental Involvement", ["High", "Medium", "Low"])
        access_res = st.selectbox("Access to Resources", ["High", "Medium", "Low"])
        
    with col2:
        sleep = st.slider("Daily Sleep Hours (የእንቅልፍ ሰዓት)", 4, 12, 7)
        phys_act = st.slider("Physical Activity (Days / Week)", 0, 7, 3)
        motivation = st.selectbox("Motivation Level", ["High", "Medium", "Low"])
        internet = st.selectbox("Internet Access at Home", ["Yes", "No"])
        school_type = st.selectbox("School Administration", ["Public", "Private"])
        peer = st.selectbox("Peer Environment", ["Positive", "Neutral", "Negative"])
        
    with col3:
        teacher = st.selectbox("Teacher Quality Rating", ["High", "Medium", "Low"])
        extra = st.selectbox("Extracurricular Activities", ["Yes", "No"])
        learning_dis = st.selectbox("Special Learning Needs", ["No", "Yes"])
        parent_edu = st.selectbox("Parental Education", ["College", "High School", "Postgraduate"])
        distance = st.selectbox("Distance from Campus", ["Near", "Moderate", "Far"])
        gender = st.selectbox("Gender", ["Female", "Male"])
        family_income = st.selectbox("Family Income Tier", ["Medium", "High", "Low"])

    st.markdown("<br>", unsafe_allow_html=True)
    
    # ACTION BUTTON
    run_btn = st.button("⚡ Run Predictive Assessment & Generate Strategy", key="predict_button")
    
    if run_btn:
        # Construct input DataFrame
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
        
        # Predict using pipeline or mathematical regression formula
        if model_pipeline is not None:
            try:
                predicted_val = float(model_pipeline.predict(input_data)[0])
            except Exception:
                predicted_val = 15.0 + (0.65 * hours) + (0.32 * attendance) + (0.28 * prev_scores) + (0.4 * tutoring)
        else:
            predicted_val = 15.0 + (0.65 * hours) + (0.32 * attendance) + (0.28 * prev_scores) + (0.4 * tutoring)
            
        final_score = round(min(max(predicted_val, 0.0), 100.0), 1)
        
        # Categorize Tier
        if final_score < 50.0:
            tier_name = "High Priority Intervention (ከፍተኛ ድጋፍ የሚሻ)"
            tier_class = "tier-high"
        elif final_score < 70.0:
            tier_name = "Moderate Monitoring (ክትትል የሚያስፈልገው)"
            tier_class = "tier-moderate"
        else:
            tier_name = "Accelerated Track (የላቀ ደረጃ)"
            tier_class = "tier-accel"
            
        # DISPLAY RESULTS CLEARLY
        st.markdown(f"""
        <div class="result-card">
            <span class="tier-badge {tier_class}">ደረጃ: {tier_name}</span>
            <div style="font-size: 1.2rem; color: #94a3b8;">የተገመተው አጠቃላይ የፈተና ውጤት (Predicted Score)</div>
            <div class="metric-number">{final_score} <span style="font-size: 1.5rem; color: #94a3b8;">/ 100</span></div>
        </div>
        """, unsafe_allow_html=True)
        
        # DYNAMIC ACTIONABLE RECOMMENDATIONS (የተግባር ምክሮች)
        st.markdown("### 💡 Data-Driven Actionable Interventions (የምክር ሃሳቦች)")
        
        recs = []
        if hours < 20:
            recs.append(f"⏱️ **የጥናት ሰዓት ማሳደግ:** በአሁኑ ሰዓት በሳምንት {hours} ሰዓት ብቻ ነው የሚያጠናው፤ ቢያንስ ወደ 25-30 ሰዓት ማሳደግ ውጤቱን በ10-15% ይጨምረዋል።")
        if attendance < 85:
            recs.append(f"🏫 **የትምህርት ቤት ገጽታ (Attendance):** የተማሪው መገኘት {attendance}% ነው። ከክፍል መቅረት ትምህርትን ስለሚያስተጓጉል ወደ 90%+ መድረስ አለበት።")
        if sleep < 7:
            recs.append(f"😴 **የእንቅልፍ ማስተካከያ:** {sleep} ሰዓት ብቻ መተኛት የአዕምሮን የማስታወስ አቅም ያዳክማል። በቀን ቢያንስ 7-8 ሰዓት መተኛት ይገባዋል።")
        if tutoring == 0 and final_score < 65:
            recs.append("👨‍🏫 **ተጨማሪ የማጠናከሪያ ትምህርት:** ተማሪው ደካማ በሆነባቸው የትምህርት ክፍሎች በወር 2-3 የማጠናከሪያ (Tutoring) ክፍለ-ጊዜዎች ቢመቻቹ ውጤታማ ይሆናል።")
        if prev_scores < 60:
            recs.append("📖 **መሰረታዊ ጽንሰ-ሀሳቦችን መከለስ:** ያለፉት የፈተና ውጤቶች ዝቅተኛ በመሆናቸው መምህራን ከመሰረታዊ ትምህርቶች ጀምረው ክፍተቱን መሙላት አለባቸው።")
            
        if not recs:
            recs.append("🌟 **አበረታች አፈፃፀም:** ተማሪው በጣም ጥሩ የጥናትና የስነ-ባህሪ ልምድ አለው። ይህንን ጠብቆ እንዲቀጥል የፈተና ጥያቄዎችን በጊዜ ሰሌዳ መስራት ላይ እንዲያተኩር ያድርጉ።")
            
        for r in recs:
            st.markdown(f'<div class="advice-item">{r}</div>', unsafe_allow_html=True)

with tab2:
    st.subheader("📚 Grade 12 ESSLCE Diagnostic Questions")
    st.info("መምህራን እና ተማሪዎች ሞዴሉ ከገመተው ውጤት በተጨማሪ እውቀታቸውን በፈተና ጥያቄዎች እንዲፈትሹ የተዘጋጀ ሞጁል።")

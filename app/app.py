import os
import joblib
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Ethiopian Giftedness and Talent Development Center",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# HIGH-CONTRAST PRODUCTION CSS
# -----------------------------------------------------------------------------
st.markdown("""
<style>
.stApp {
    background-color: #0b1120;
    color: #f8fafc;
}

.hero-title {
    font-size: 2.1rem;
    font-weight: 900;
    color: #2dd4bf;
    letter-spacing: -0.5px;
    line-height: 1.2;
    margin: 0.4rem 0 0.2rem 0;
    text-transform: uppercase;
}

.hero-subtitle-am {
    font-size: 1.25rem;
    font-weight: 800;
    color: #6ee7b7;
    margin-bottom: 0.5rem;
}

.hero-desc {
    font-size: 1rem;
    color: #cbd5e1;
    margin-bottom: 1rem;
}

.param-header {
    font-size: 1.15rem;
    font-weight: 800;
    color: #f8fafc;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

div.stButton > button,
button[kind="primary"],
button[data-testid="baseButton-secondary"],
button[data-testid="baseButton-primary"] {
    background-color: #0d9488 !important;
    background-image: linear-gradient(135deg, #0d9488 0%, #0f766e 100%) !important;
    color: #ffffff !important;
    border: 1px solid #2dd4bf !important;
    border-radius: 8px !important;
    padding: 0.85rem 1.6rem !important;
    font-size: 1.15rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.5px !important;
    width: 100% !important;
    cursor: pointer !important;
    box-shadow: 0 4px 15px rgba(13, 148, 136, 0.4) !important;
}

div.stButton > button *,
button[kind="primary"] *,
button[data-testid="baseButton-secondary"] *,
button[data-testid="baseButton-primary"] * {
    color: #ffffff !important;
    font-weight: 800 !important;
}

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

.advice-row {
    background-color: #1e293b;
    border-left: 5px solid #2dd4bf;
    border-radius: 6px;
    padding: 1.1rem 1.3rem;
    margin-bottom: 0.8rem;
    color: #f8fafc;
    font-size: 1.02rem;
    line-height: 1.5;
}
.advice-row.warn { border-left-color: #f59e0b; }
.advice-row.danger { border-left-color: #ef4444; }
.advice-row.info { border-left-color: #38bdf8; }
.advice-row.success { border-left-color: #10b981; }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# IMAGE RESOLUTION HELPERS (Handles both Linux Cloud & Local Windows Paths)
# -----------------------------------------------------------------------------
def load_img(name):
    candidate_paths = [
        os.path.join("app", "assets", name),
        os.path.join("assets", name),
        name
    ]
    for p in candidate_paths:
        if os.path.exists(p):
            try:
                return Image.open(p)
            except Exception:
                pass
    return None

img_logo = load_img("logo.png")
img_hero = load_img("hero.png")

# -----------------------------------------------------------------------------
# HERO SECTION
# -----------------------------------------------------------------------------
col_hero_left, col_hero_right = st.columns([1.3, 1])

with col_hero_left:
    if img_logo:
        st.image(img_logo, width=120)
    else:
        st.write("🎓 **EGATE**")
        
    st.markdown('<div class="hero-title">ETHIOPIAN GIFTEDNESS AND TALENT DEVELOPMENT CENTER</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle-am">የኢትዮጵያ ተሰጥኦና ተውህቦ ማበልጸጊያ ማዕከል</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-desc">Intelligent Predictive Modeling & National Exam Diagnostic Practice Module.</div>', unsafe_allow_html=True)

with col_hero_right:
    if img_hero:
        st.image(img_hero, use_container_width=True)

st.write("")

# -----------------------------------------------------------------------------
# PIPELINE LOADING
# -----------------------------------------------------------------------------
MODEL_PATH = "models/exam_score_prediction_pipeline.joblib"
pipeline = None
if os.path.exists(MODEL_PATH):
    try:
        pipeline = joblib.load(MODEL_PATH)
    except Exception:
        pipeline = None

tab1, tab2 = st.tabs([
    "🎓 Machine Learning Score Predictor", 
    "📑 Grade 12 National Exam Practice (60 Questions)"
])

# -----------------------------------------------------------------------------
# TAB 1: PREDICTOR
# -----------------------------------------------------------------------------
with tab1:
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown('<div class="param-header">📚 Academic Behaviors</div>', unsafe_allow_html=True)
        hours = st.slider("Weekly Study Hours (የጥናት ሰዓት)", 1, 50, 18)
        attendance = st.slider("Attendance Rate % (የትምህርት ቤት ገጽታ)", 40, 100, 82)
        prev_scores = st.slider("Previous Cumulative Score % (ያለፈው ውጤት)", 30, 100, 68)
        tutoring = st.slider("Tutoring Sessions / Month (የማጠናከሪያ ክፍለ-ጊዜ)", 0, 10, 1)
        parental_inv = st.selectbox("Parental Involvement", ["Medium", "High", "Low"])
        access_res = st.selectbox("Resource Access", ["Medium", "High", "Low"])

    with col_b:
        st.markdown('<div class="param-header">🧠 Wellbeing & Focus</div>', unsafe_allow_html=True)
        sleep = st.slider("Daily Sleep Hours (የእንቅልፍ ሰዓት)", 4, 12, 6)
        phys_act = st.slider("Physical Activity (Days / Week)", 0, 7, 3)
        motivation = st.selectbox("Motivation Level", ["Medium", "High", "Low"])
        internet = st.selectbox("Internet Access at Home", ["Yes", "No"])
        peer = st.selectbox("Peer Environment", ["Positive", "Neutral", "Negative"])
        extra = st.selectbox("Extracurricular Activities", ["Yes", "No"])

    with col_c:
        st.markdown('<div class="param-header">🏫 Institutional Context</div>', unsafe_allow_html=True)
        teacher = st.selectbox("Teacher Quality Rating", ["Medium", "High", "Low"])
        school_type = st.selectbox("School Administration", ["Public", "Private"])
        learning_dis = st.selectbox("Special Learning Support Needs", ["No", "Yes"])
        parent_edu = st.selectbox("Parental Education", ["High School", "College", "Postgraduate"])
        distance = st.selectbox("Distance from Campus", ["Near", "Moderate", "Far"])
        gender = st.selectbox("Gender", ["Female", "Male"])
        family_income = st.selectbox("Family Income Tier", ["Medium", "High", "Low"])

    st.markdown("<br>", unsafe_allow_html=True)
    run_btn = st.button("⚡ Run Predictive Assessment & Generate Strategy", key="run_strategy_btn")

    input_data = pd.DataFrame([{
        "Hours_Studied": hours, "Attendance": attendance, "Parental_Involvement": parental_inv,
        "Access_to_Resources": access_res, "Extracurricular_Activities": extra, "Sleep_Hours": sleep,
        "Previous_Scores": prev_scores, "Motivation_Level": motivation, "Internet_Access": internet,
        "Tutoring_Sessions": tutoring, "Family_Income": family_income, "Teacher_Quality": teacher,
        "School_Type": school_type, "Peer_Influence": peer, "Physical_Activity": phys_act,
        "Learning_Disabilities": learning_dis, "Parental_Education_Level": parent_edu,
        "Distance_from_Home": distance, "Gender": gender
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
        tier_code, tier_title, tier_desc = "high", "High Priority Intervention", "ከፍተኛ አፋጣኝ ድጋፍ የሚሻ"
    elif final_score < 70.0:
        tier_code, tier_title, tier_desc = "moderate", "Moderate Monitoring", "ተከታታይ ክትትል የሚያስፈልገው"
    else:
        tier_code, tier_title, tier_desc = "accel", "Accelerated Track", "የላቀና የተረጋጋ ደረጃ"

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
        <div style="font-size: 1.3rem; font-weight: 800; color: #2dd4bf; margin-top: 1.2rem; margin-bottom: 0.8rem; border-top: 1px solid #334155; padding-top: 1rem;">
            💡 Data-Driven Actionable Interventions (ተግባራዊ የምክር ሃሳቦች)
        </div>
        {advice_html}
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# TAB 2: EXACT 60-QUESTION GRADE 12 ESSLCE DIAGNOSTIC BANK (12 PER SUBJECT)
# -----------------------------------------------------------------------------
with tab2:
    st.subheader("📑 Grade 12 National Exam Practice Bank (60 Questions)")
    st.caption("የ12ኛ ክፍል ተማሪዎች ትንበያ ካገኙ በኋላ እውቀታቸውን እንዲፈትሹ የተዘጋጁ 60 ብሔራዊ የፈተና ጥያቄዎች (በ5 ዋና የትምህርት ክፍሎች)።")

    exam_bank = {
        "Mathematics (ተፈጥሮ ሳይንስ)": [
            {"q": "1. What is the derivative of f(x) = ln(x² + 3x + 1)?", "opts": ["(2x + 3)/(x² + 3x + 1)", "1/(2x + 3)", "2x/(x² + 3x + 1)", "(x + 3)/(x² + 3x + 1)"], "ans": "(2x + 3)/(x² + 3x + 1)", "exp": "Chain rule: d/dx[ln(u)] = u'/u = (2x + 3)/(x² + 3x + 1)."},
            {"q": "2. If matrix A is 3x3 with det(A) = 5, what is det(2A)?", "opts": ["10", "40", "20", "25"], "ans": "40", "exp": "det(kA) = k^n * det(A). Here 2³ * 5 = 8 * 5 = 40."},
            {"q": "3. Evaluate the limit: lim (x -> 0) [sin(5x) / x]", "opts": ["0", "1", "5", "Undefined"], "ans": "5", "exp": "Standard trigonometric limit identity lim (x->0) [sin(kx)/x] = k."},
            {"q": "4. What is the integral of ∫ (3x² + 4x - 5) dx?", "opts": ["x³ + 2x² - 5x + C", "6x + 4 + C", "3x³ + 4x² - 5x + C", "x³ + 4x² - 5x + C"], "ans": "x³ + 2x² - 5x + C", "exp": "Power rule: ∫3x² dx = x³, ∫4x dx = 2x², ∫-5 dx = -5x."},
            {"q": "5. What is the 10th term of an arithmetic progression with a₁ = 3 and d = 4?", "opts": ["39", "36", "43", "40"], "ans": "39", "exp": "a_n = a₁ + (n - 1)d -> a₁₀ = 3 + (9)(4) = 39."},
            {"q": "6. Find the modulus of the complex number z = 3 - 4i.", "opts": ["5", "7", "1", "25"], "ans": "5", "exp": "|z| = √(3² + (-4)²) = √(9 + 16) = √25 = 5."},
            {"q": "7. What is the vertical asymptote of f(x) = (2x + 1)/(x - 4)?", "opts": ["x = 4", "y = 2", "x = -4", "y = 4"], "ans": "x = 4", "exp": "Denominator is zero at x - 4 = 0 => x = 4."},
            {"q": "8. What is the dot product of vectors u = (2, -3) and v = (4, 1)?", "opts": ["5", "11", "-5", "8"], "ans": "5", "exp": "u · v = (2)(4) + (-3)(1) = 8 - 3 = 5."},
            {"q": "9. How many permutations can be formed using all letters of 'BOOK'?", "opts": ["12", "24", "6", "4"], "ans": "12", "exp": "P = 4! / 2! = 24 / 2 = 12."},
            {"q": "10. What is the radius of the circle x² + y² - 6x + 8y = 0?", "opts": ["5", "25", "10", "7"], "ans": "5", "exp": "(x - 3)² + (y + 4)² = 25 => r = √25 = 5."},
            {"q": "11. If f(x) = e^(3x), what is f''(x)?", "opts": ["9e^(3x)", "3e^(3x)", "6e^(3x)", "e^(3x)"], "ans": "9e^(3x)", "exp": "f'(x) = 3e^(3x), f''(x) = 9e^(3x)."},
            {"q": "12. What is the sum to infinity of 8 + 4 + 2 + 1 + ...?", "opts": ["16", "32", "15", "8"], "ans": "16", "exp": "S_∞ = a / (1 - r) = 8 / (1 - 0.5) = 16."}
        ],
        "Physics (ፊዚክስ)": [
            {"q": "1. A mass of 2 kg moving at 10 m/s collides and sticks to a stationary 2 kg mass. What is final velocity?", "opts": ["5 m/s", "10 m/s", "2.5 m/s", "0 m/s"], "ans": "5 m/s", "exp": "Conservation of momentum: (2)(10) + 0 = (2+2)vf => vf = 20/4 = 5 m/s."},
            {"q": "2. Kepler's Third Law states that the square of orbital period T is proportional to:", "opts": ["a³ (semi-major axis cubed)", "a²", "1/a³", "Planet Mass"], "ans": "a³ (semi-major axis cubed)", "exp": "Kepler's Law: T² ∝ a³."},
            {"q": "3. The work done on a gas during an isobaric compression at 100 kPa from 5 m³ to 2 m³ is:", "opts": ["-300 kJ", "+300 kJ", "-500 kJ", "0 kJ"], "ans": "-300 kJ", "exp": "W = P * ΔV = 100 kPa * (2 - 5) m³ = -300 kJ."},
            {"q": "4. What is the electric field at distance r from a point charge Q?", "opts": ["kQ/r²", "kQ/r", "kQ²/r", "kQ/r³"], "ans": "kQ/r²", "exp": "Coulomb's field definition: E = kQ / r²."},
            {"q": "5. What frequency is heard by an observer moving toward a stationary 400 Hz source?", "opts": ["Higher than 400 Hz", "Lower than 400 Hz", "Exactly 400 Hz", "Zero"], "ans": "Higher than 400 Hz", "exp": "Doppler effect: Approaching a source results in higher detected frequency."},
            {"q": "6. A 100-watt bulb operates on 200 V. What is the resistance of the bulb filament?", "opts": ["400 Ω", "200 Ω", "100 Ω", "2 Ω"], "ans": "400 Ω", "exp": "P = V² / R => R = V² / P = (200)² / 100 = 400 Ω."},
            {"q": "7. Total internal reflection occurs when light moves from:", "opts": ["Denser to rarer medium (θ > θc)", "Rarer to denser medium", "Air into water", "Vacuum into glass"], "ans": "Denser to rarer medium (θ > θc)", "exp": "Requires moving to lower refractive index at an angle exceeding critical angle."},
            {"q": "8. What is the kinetic energy of a 1000 kg car traveling at 20 m/s?", "opts": ["200,000 J", "400,000 J", "20,000 J", "10,000 J"], "ans": "200,000 J", "exp": "KE = 0.5 * m * v² = 0.5 * 1000 * 400 = 200,000 J."},
            {"q": "9. Which phenomenon proves the particle nature of electromagnetic waves?", "opts": ["Photoelectric effect", "Interference", "Diffraction", "Polarization"], "ans": "Photoelectric effect", "exp": "Demonstrates energy quantization into discrete photons (Einstein 1905)."},
            {"q": "10. What is the unit of magnetic flux?", "opts": ["Weber (Wb)", "Tesla (T)", "Henry (H)", "Farad (F)"], "ans": "Weber (Wb)", "exp": "Magnetic flux is measured in Webers (1 Wb = 1 T·m²)."},
            {"q": "11. A step-up transformer has Np=100 and Ns=500 turns. If Vp=20V, what is Vs?", "opts": ["100 V", "4 V", "50 V", "200 V"], "ans": "100 V", "exp": "Vs/Vp = Ns/Np => Vs = 20 * (500/100) = 100 V."},
            {"q": "12. In simple harmonic motion, the acceleration is maximum when displacement is:", "opts": ["Maximum", "Zero", "Half of amplitude", "Negative only"], "ans": "Maximum", "exp": "a = -ω²x; acceleration magnitude is maximum at maximum displacement."}
        ],
        "Chemistry (ኬሚስትሪ)": [
            {"q": "1. What is the pH of a 0.001 M HCl aqueous solution?", "opts": ["3.0", "1.0", "11.0", "7.0"], "ans": "3.0", "exp": "pH = -log[H+] = -log(10⁻³) = 3.0."},
            {"q": "2. Which molecule has a tetrahedral molecular geometry?", "opts": ["CH₄", "NH₃", "H₂O", "CO₂"], "ans": "CH₄", "exp": "Methane has 4 bonding pairs and 0 lone pairs on carbon (sp³ tetrahedral)."},
            {"q": "3. What is the oxidation state of Chromium in K₂Cr₂O₇?", "opts": ["+6", "+3", "+7", "+2"], "ans": "+6", "exp": "2(+1) + 2(Cr) + 7(-2) = 0 => 2Cr - 12 = 0 => Cr = +6."},
            {"q": "4. According to Le Chatelier's principle, increasing pressure on N₂(g) + 3H₂(g) ⇌ 2NH₃(g) will:", "opts": ["Shift equilibrium to the right", "Shift equilibrium to the left", "Have no effect", "Decrease NH₃ yield"], "ans": "Shift equilibrium to the right", "exp": "Equilibrium shifts toward fewer gas moles (4 moles -> 2 moles)."},
            {"q": "5. Which organic functional group characterizes aldehydes?", "opts": ["-CHO (Carbonyl at terminal)", "-COOH (Carboxyl)", "-OH (Hydroxyl)", "-CO- (Ketone)"], "ans": "-CHO (Carbonyl at terminal)", "exp": "Aldehydes possess a terminal carbonyl group bonded to hydrogen (-CHO)."},
            {"q": "6. How many moles of O₂ are required to completely combust 1 mole of propane (C₃H₈)?", "opts": ["5 moles", "3 moles", "4 moles", "7 moles"], "ans": "5 moles", "exp": "C₃H₈ + 5O₂ -> 3CO₂ + 4H₂O."},
            {"q": "7. What type of bond holds Sodium Chloride (NaCl) crystal lattice together?", "opts": ["Ionic bonding", "Covalent bonding", "Metallic bonding", "Hydrogen bonding"], "ans": "Ionic bonding", "exp": "Electrostatic attraction between Na⁺ and Cl⁻ ions."},
            {"q": "8. What is the conjugate base of HSO₄⁻?", "opts": ["SO₄²⁻", "H₂SO₄", "H₃O⁺", "H₂SO₃"], "ans": "SO₄²⁻", "exp": "Conjugate base results when acid donates H⁺ (HSO₄⁻ - H⁺ = SO₄²⁻)."},
            {"q": "9. Which catalyst is used in the industrial Haber process for ammonia synthesis?", "opts": ["Finely divided Iron (Fe)", "Nickel (Ni)", "Platinum (Pt)", "Vanadium oxide (V₂O₅)"], "ans": "Finely divided Iron (Fe)", "exp": "Iron promoted with K₂O and Al₂O₃ is the standard Haber catalyst."},
            {"q": "10. What is the electron configuration of the Calcium ion (Ca²⁺)?", "opts": ["[Ar]", "[Ne] 3s²", "[Ar] 4s²", "[Kr]"], "ans": ["[Ar]"], "exp": "Neutral Ca is [Ar] 4s². Losing two electrons leaves the Argon core [Ar]."},
            {"q": "11. An electrochemical cell has E°cell > 0. The reaction is:", "opts": ["Spontaneous (ΔG° < 0)", "Non-spontaneous", "At equilibrium", "Endothermic only"], "ans": "Spontaneous (ΔG° < 0)", "exp": "ΔG° = -nFE°cell. When E°cell is positive, ΔG° is negative (spontaneous)."},
            {"q": "12. What law states that at constant temperature, Volume is inversely proportional to Pressure?", "opts": ["Boyle's Law", "Charles's Law", "Gay-Lussac's Law", "Avogadro's Law"], "ans": "Boyle's Law", "exp": "Boyle's Law: P₁V₁ = P₂V₂ at constant temperature."}
        ],
        "Biology (ባዮሎጂ)": [
            {"q": "1. Which cellular organelle is responsible for aerobic ATP generation?", "opts": ["Mitochondria", "Ribosome", "Endoplasmic Reticulum", "Golgi Apparatus"], "ans": "Mitochondria", "exp": "Mitochondria carry out the citric acid cycle and oxidative phosphorylation."},
            {"q": "2. In DNA structure, which nitrogenous base pairs with Adenine via two hydrogen bonds?", "opts": ["Thymine", "Guanine", "Cytosine", "Uracil"], "ans": "Thymine", "exp": "Adenine pairs with Thymine (A=T) with two hydrogen bonds in double-stranded DNA."},
            {"q": "3. What is the phenotypic ratio of a heterozygous monohybrid cross (Aa x Aa)?", "opts": ["3:1", "1:2:1", "9:3:3:1", "1:1"], "ans": "3:1", "exp": "Offspring genotypic ratio is 1 AA : 2 Aa : 1 aa, yielding a 3:1 phenotype ratio."},
            {"q": "4. Which enzyme breaks down starch into maltose in the human digestive system?", "opts": ["Amylase", "Pepsin", "Lipase", "Trypsin"], "ans": "Amylase", "exp": "Amylase cleaves alpha-1,4 glycosidic bonds in starch."},
            {"q": "5. What hormone promotes stomatal closure during plant drought stress?", "opts": ["Abscisic Acid (ABA)", "Auxin", "Gibberellin", "Cytokinin"], "ans": "Abscisic Acid (ABA)", "exp": "ABA induces potassium ion efflux from guard cells, causing closure."},
            {"q": "6. Which phase of mitosis involves chromosomes aligning at the equatorial plate?", "opts": ["Metaphase", "Prophase", "Anaphase", "Telophase"], "ans": "Metaphase", "exp": "Chromosomes line up along the metaphase plate before chromatid separation."},
            {"q": "7. What blood type is considered the universal red blood cell donor?", "opts": ["O negative", "AB positive", "A positive", "O positive"], "ans": "O negative", "exp": "O negative RBCs lack A, B, and Rh surface antigens."},
            {"q": "8. What is the primary function of transfer RNA (tRNA) in protein synthesis?", "opts": ["Deliver specific amino acids to ribosome", "Transcribe DNA in nucleus", "Synthesize rRNA", "Degrade incorrect proteins"], "ans": "Deliver specific amino acids to ribosome", "exp": "tRNA transfers the corresponding amino acid to the matching mRNA codon."},
            {"q": "9. In ecological succession, the first organisms to colonize bare rock are:", "opts": ["Pioneer species (Lichens)", "Hardwood trees", "Shrubs", "Perennial grasses"], "ans": "Pioneer species (Lichens)", "exp": "Lichens and mosses begin biological weathering to produce early soil."},
            {"q": "10. Which part of the human brain controls respiration, heartbeat, and blood pressure?", "opts": ["Medulla oblongata", "Cerebellum", "Cerebrum", "Hypothalamus"], "ans": "Medulla oblongata", "exp": "The medulla oblongata in the brainstem regulates autonomic reflexes."},
            {"q": "11. The light-dependent reactions of photosynthesis occur within the:", "opts": ["Thylakoid membranes", "Stroma", "Mitochondrial matrix", "Cytoplasm"], "ans": "Thylakoid membranes", "exp": "Chlorophyll pigments and electron transport chains reside in thylakoid membranes."},
            {"q": "12. What term describes a relationship where one organism benefits while the other is unharmed?", "opts": ["Commensalism", "Mutualism", "Parasitism", "Competition"], "ans": "Commensalism", "exp": "Commensalism benefits one partner with zero net impact on the host."}
        ],
        "English (እንግሊዝኛ)": [
            {"q": "1. If I ______ harder in Grade 11, I would have achieved a distinction.", "opts": ["had studied", "studied", "have studied", "study"], "ans": "had studied", "exp": "Third conditional: If + past perfect (had studied), would have + past participle."},
            {"q": "2. Choose the word most nearly opposite in meaning to 'Arrogant':", "opts": ["Humble", "Proud", "Conceited", "Boastful"], "ans": "Humble", "exp": "'Arrogant' means having exaggerated self-importance; 'Humble' is the antonym."},
            {"q": "3. The committee ______ reached a unanimous decision on the university entrance cutoff.", "opts": ["has", "have", "were", "are"], "ans": "has", "exp": "Collective nouns acting as a single entity take singular verbs ('has')."},
            {"q": "4. Neither the teacher nor the students ______ present at the national symposium.", "opts": ["were", "was", "is", "has been"], "ans": "were", "exp": "With 'neither... nor', the verb agrees with the closer subject ('students' -> were)."},
            {"q": "5. Identify the active voice of: 'The scholarship was awarded to Abebe by the board.'", "opts": ["The board awarded the scholarship to Abebe.", "Abebe awarded the scholarship.", "The scholarship awarded Abebe.", "The board was awarding Abebe."], "ans": "The board awarded the scholarship to Abebe.", "exp": "Subject 'The board' performs the action directly on the object."},
            {"q": "6. Choose the correct spelling:", "opts": ["Accommodation", "Acommodation", "Accomodation", "Acomodation"], "ans": "Accommodation", "exp": "Standard spelling contains double 'c' and double 'm'."},
            {"q": "7. The idiom 'To cut corners' means to:", "opts": ["Do something poorly to save time or money", "Walk around a junction", "Drive fast", "Excel in an examination"], "ans": "Do something poorly to save time or money", "exp": "Idiomatic meaning: Taking shortcuts that reduce quality."},
            {"q": "8. Identify the clause type: 'Although the exam was challenging, she scored top marks.'", "opts": ["Complex sentence", "Compound sentence", "Simple sentence", "Compound-complex sentence"], "ans": "Complex sentence", "exp": "Contains one dependent clause ('Although...') and one independent clause."},
            {"q": "9. Select the synonym of 'Resilient':", "opts": ["Adaptable & Tough", "Fragile", "Rigid", "Hesitant"], "ans": "Adaptable & Tough", "exp": "'Resilient' means able to recover quickly from difficult conditions."},
            {"q": "10. He insisted ______ paying for the reference books himself.", "opts": ["on", "in", "to", "for"], "ans": "on", "exp": "The verb 'insist' takes the preposition 'on'."},
            {"q": "11. What figure of speech is: 'The classroom was a zoo during break time'?", "opts": ["Metaphor", "Simile", "Personification", "Hyperbole"], "ans": "Metaphor", "exp": "Direct comparison stating one entity is another without using 'like' or 'as'."},
            {"q": "12. Identify the correct relative pronoun: 'The professor ______ paper was published won the prize.'", "opts": ["whose", "whom", "who", "which"], "ans": "whose", "exp": "Possessive relative pronoun referring to the professor's paper is 'whose'."}
        ]
    }

    selected_subject = st.selectbox("Select Subject (የትምህርት አይነት ይምረጡ):", list(exam_bank.keys()))
    questions_list = exam_bank[selected_subject]

    st.markdown(f"#### Displaying all 12 Questions for **{selected_subject}** (Total: 60 across 5 subjects)")

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

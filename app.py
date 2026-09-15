import streamlit as st
st.markdown('''<style>
/* 1. Global Streamlit Button Override */
button[data-testid="baseButton-secondary"],
button[data-testid="baseButton-primary"],
.stButton > button,
div.stButton > button {
    background-color: #1d4ed8 !important;
    background-image: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
    color: #ffffff !important;
    border: 1px solid #3b82f6 !important;
    border-radius: 8px !important;
    padding: 0.75rem 1.5rem !important;
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.5px !important;
    box-shadow: 0 4px 14px rgba(37, 99, 235, 0.4) !important;
    width: 100% !important;
    cursor: pointer !important;
}

/* 2. Text & Icon Elements Inside the Button */
button[data-testid="baseButton-secondary"] *,
button[data-testid="baseButton-primary"] *,
.stButton > button *,
div.stButton > button * {
    color: #ffffff !important;
    font-weight: 700 !important;
    fill: #ffffff !important;
}

/* 3. Hover & Active States */
button[data-testid="baseButton-secondary"]:hover,
button[data-testid="baseButton-primary"]:hover,
.stButton > button:hover,
div.stButton > button:hover {
    background-color: #1e40af !important;
    background-image: linear-gradient(135deg, #1d4ed8, #1e40af) !important;
    color: #ffffff !important;
    border-color: #60a5fa !important;
    box-shadow: 0 6px 20px rgba(37, 99, 235, 0.6) !important;
    transform: translateY(-1px) !important;
}
</style>''', unsafe_allow_html=True)
import streamlit as st
st.markdown('''<style>
/* High-Contrast Primary Button Override */
div.stButton > button,
div.stButton > button:first-child,
div.stButton > button:hover,
div.stButton > button:focus,
div.stButton > button:active {
    background: #2563eb !important;
    background-color: #2563eb !important;
    color: #ffffff !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    border: 1px solid #1d4ed8 !important;
    border-radius: 8px !important;
    padding: 0.65rem 1.5rem !important;
    box-shadow: 0 4px 14px rgba(37, 99, 235, 0.4) !important;
    width: 100% !important;
}

div.stButton > button p,
div.stButton > button span,
div.stButton > button div {
    color: #ffffff !important;
    font-weight: 700 !important;
}

div.stButton > button:hover {
    background: #1d4ed8 !important;
    background-color: #1d4ed8 !important;
    color: #ffffff !important;
    box-shadow: 0 6px 20px rgba(37, 99, 235, 0.6) !important;
}
</style>''', unsafe_allow_html=True)



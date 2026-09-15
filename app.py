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


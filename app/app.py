import streamlit as st

st.set_page_config(
    page_title="Fake News AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Global sidebar + app shell styles
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

[data-testid="stAppViewContainer"] {
    background: #020916;
    font-family: 'DM Sans', sans-serif;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #040d1a !important;
    border-right: 1px solid rgba(99,102,241,0.12);
    min-width: 240px !important;
}
[data-testid="stSidebar"] > div {
    padding-top: 28px;
}

/* Hide default streamlit header */
header[data-testid="stHeader"] {
    background: transparent;
    height: 0;
}
#MainMenu, footer { display: none; }

/* Sidebar brand */
.sidebar-brand {
    padding: 0 20px 28px;
    border-bottom: 1px solid rgba(99,102,241,0.1);
    margin-bottom: 20px;
}
.brand-name {
    font-family: 'Syne', sans-serif;
    font-size: 20px;
    font-weight: 800;
    color: #f8fafc;
    letter-spacing: -0.02em;
}
.brand-sub {
    font-size: 12px;
    color: #334155;
    margin-top: 3px;
    letter-spacing: 0.04em;
}

/* Radio nav */
[data-testid="stSidebar"] .stRadio label {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 15px !important;
    color: #64748b !important;
    padding: 10px 14px !important;
    border-radius: 10px !important;
    transition: all 0.2s !important;
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
    cursor: pointer !important;
}
[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(99,102,241,0.08) !important;
    color: #a5b4fc !important;
}
[data-testid="stSidebar"] [data-baseweb="radio"] input:checked + div + label,
[data-testid="stSidebar"] .stRadio [aria-checked="true"] label {
    background: rgba(99,102,241,0.12) !important;
    color: #818cf8 !important;
}
[data-testid="stSidebar"] .stRadio > div {
    gap: 2px !important;
}

/* Scrollbar */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
    background: rgba(99,102,241,0.2);
    border-radius: 99px;
}

/* Main content padding */
[data-testid="block-container"] {
    padding: 0 clamp(16px, 4vw, 60px) !important;
    max-width: 1100px;
}

/* Responsive: hide sidebar on mobile */
@media (max-width: 640px) {
    [data-testid="stSidebar"] {
        min-width: 200px !important;
    }
    [data-testid="block-container"] {
        padding: 0 12px !important;
    }
}
</style>
""", unsafe_allow_html=True)

# Sidebar brand header
st.sidebar.markdown("""
<div class="sidebar-brand">
    <div class="brand-name">🧠 Fake News AI</div>
    <div class="brand-sub">ML-powered detection</div>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigation",
    ["🏠  Home", "🔍  Detector", "📘  About"],
    label_visibility="collapsed"
)

# Sidebar footer
st.sidebar.markdown("""
<div style="position: fixed; bottom: 24px; left: 0; width: 240px; padding: 0 20px; font-size: 12px; color: #1e293b; line-height: 1.6;">
    Built with scikit-learn<br>+ Streamlit
</div>
""", unsafe_allow_html=True)

# Route pages
if "Home" in page:
    from pages import Home
    Home.run()
elif "Detector" in page:
    from pages import Detector
    Detector.run()
elif "About" in page:
    from pages import About
    About.run()
import sys
import os

# ── Ensure project root is in sys.path on Streamlit Cloud ──
_root = os.path.dirname(os.path.abspath(__file__))
if _root not in sys.path:
    sys.path.insert(0, _root)

import streamlit as st

st.set_page_config(
    page_title="Fake News AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Hide Streamlit multipage auto-nav (caused by pages/ folder) ──
st.markdown("""
<style>
[data-testid="stSidebarNav"],
[data-testid="stSidebarNavItems"],
[data-testid="stSidebarNavSeparator"],
section[data-testid="stSidebar"] nav,
.st-emotion-cache-pbk8do,
.st-emotion-cache-1rtdyuf,
.st-emotion-cache-eczf16,
ul[data-testid="stSidebarNavItems"] {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
    overflow: hidden !important;
}
</style>
""", unsafe_allow_html=True)

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

/* Responsive mobile */
@media (max-width: 768px) {
    [data-testid="stSidebar"] {
        min-width: 200px !important;
        max-width: 80vw !important;
    }
    [data-testid="block-container"] {
        padding: 0 12px !important;
    }
    /* Keep hamburger menu button visible on mobile */
    [data-testid="collapsedControl"] {
        display: flex !important;
        visibility: visible !important;
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

# ── Auto-close sidebar on mobile after nav selection ──
st.markdown("""
<script>
(function() {
    function isMobile() {
        return window.innerWidth <= 768;
    }

    function closeSidebar() {
        // Find Streamlit's sidebar close/collapse button and click it
        const closeBtn = document.querySelector('[data-testid="collapsedControl"]') ||
                         document.querySelector('button[aria-label="Close sidebar"]') ||
                         document.querySelector('button[kind="header"]');
        if (closeBtn) closeBtn.click();

        // Fallback: find the chevron/arrow button inside the sidebar
        const sidebarBtns = document.querySelectorAll('[data-testid="stSidebar"] button');
        sidebarBtns.forEach(btn => {
            const label = btn.getAttribute('aria-label') || '';
            if (label.toLowerCase().includes('close') || label.toLowerCase().includes('collapse')) {
                btn.click();
            }
        });
    }

    function attachListeners() {
        const radioInputs = document.querySelectorAll('[data-testid="stSidebar"] input[type="radio"]');
        radioInputs.forEach(function(input) {
            if (!input.dataset.mobileListenerAttached) {
                input.dataset.mobileListenerAttached = "true";
                input.addEventListener('change', function() {
                    if (isMobile()) {
                        // Small delay so Streamlit registers the selection first
                        setTimeout(closeSidebar, 120);
                    }
                });
            }
        });
    }

    // Run on load and re-run after Streamlit re-renders
    const observer = new MutationObserver(function() {
        attachListeners();
    });

    observer.observe(document.body, { childList: true, subtree: true });

    // Initial attach attempt
    setTimeout(attachListeners, 500);
    setTimeout(attachListeners, 1500);
})();
</script>
""", unsafe_allow_html=True)

# Route pages — import from components/ (not pages/ which triggers Streamlit multipage)
if "Home" in page:
    from components import Home
    Home.run()
elif "Detector" in page:
    from components import Detector
    Detector.run()
elif "About" in page:
    from components import About
    About.run()
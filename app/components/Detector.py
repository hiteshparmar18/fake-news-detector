import sys
import os
# Go up 2 levels: components/ -> project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from src.predict import predict_news


def run():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'DM Sans', sans-serif;
    }
    [data-testid="stAppViewContainer"] { background: #020916; }
    [data-testid="stSidebar"] {
        background: #040d1a !important;
        border-right: 1px solid rgba(99,102,241,0.15);
    }
    [data-testid="stSidebar"] * { color: #cbd5e1 !important; }

    .page-header {
        padding: 48px 0 32px;
        text-align: center;
    }
    .page-eyebrow {
        font-size: 12px;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: #6366f1;
        font-weight: 500;
        margin-bottom: 14px;
    }
    .page-title {
        font-family: 'Syne', sans-serif;
        font-size: clamp(32px, 5vw, 54px);
        font-weight: 800;
        color: #f8fafc;
        letter-spacing: -0.025em;
        line-height: 1.05;
        margin: 0 0 14px;
    }
    .page-desc {
        font-size: 16px;
        color: #475569;
        max-width: 460px;
        margin: 0 auto;
        line-height: 1.7;
    }

    /* Input area */
    .stTextArea textarea {
        background: rgba(15,23,42,0.95) !important;
        border: 1px solid rgba(51,65,85,0.7) !important;
        border-radius: 16px !important;
        color: #e2e8f0 !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 15px !important;
        line-height: 1.7 !important;
        padding: 18px !important;
        transition: border-color 0.2s !important;
    }
    .stTextArea textarea:focus {
        border-color: rgba(99,102,241,0.5) !important;
        box-shadow: 0 0 0 3px rgba(99,102,241,0.1) !important;
    }
    .stTextArea label {
        color: #94a3b8 !important;
        font-size: 14px !important;
        font-weight: 500 !important;
    }

    /* Primary button */
    .stButton > button {
        border-radius: 14px !important;
        font-family: 'Syne', sans-serif !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        letter-spacing: 0.02em !important;
        transition: all 0.25s !important;
        width: 100% !important;
        padding: 14px 20px !important;
    }

    div[data-testid="column"]:nth-child(1) .stButton > button {
        background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 6px 24px rgba(99,102,241,0.3) !important;
    }
    div[data-testid="column"]:nth-child(1) .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 32px rgba(99,102,241,0.45) !important;
    }

    div[data-testid="column"]:nth-child(2) .stButton > button {
        background: rgba(15,23,42,0.8) !important;
        color: #94a3b8 !important;
        border: 1px solid rgba(51,65,85,0.7) !important;
    }
    div[data-testid="column"]:nth-child(2) .stButton > button:hover {
        border-color: rgba(99,102,241,0.4) !important;
        color: #a5b4fc !important;
        background: rgba(99,102,241,0.06) !important;
    }

    /* Clear button — 3rd column */
    div[data-testid="column"]:nth-child(3) .stButton > button {
        background: rgba(15,10,10,0.8) !important;
        color: #64748b !important;
        border: 1px solid rgba(127,29,29,0.4) !important;
    }
    div[data-testid="column"]:nth-child(3) .stButton > button:hover {
        background: rgba(239,68,68,0.08) !important;
        border-color: rgba(239,68,68,0.45) !important;
        color: #f87171 !important;
    }

    /* Spinner overrides */
    .stSpinner > div {
        border-top-color: #6366f1 !important;
    }

    /* Result banner */
    .result-banner {
        border-radius: 20px;
        padding: 28px 32px;
        margin: 28px 0 0;
        display: flex;
        align-items: center;
        gap: 20px;
        animation: resultReveal 0.5s cubic-bezier(0.34, 1.56, 0.64, 1) both;
    }
    @keyframes resultReveal {
        from { opacity: 0; transform: scale(0.92) translateY(10px); }
        to { opacity: 1; transform: scale(1) translateY(0); }
    }

    .result-real {
        background: rgba(16,42,28,0.9);
        border: 1px solid rgba(34,197,94,0.3);
    }
    .result-fake {
        background: rgba(42,16,16,0.9);
        border: 1px solid rgba(239,68,68,0.3);
    }

    .result-icon {
        font-size: 40px;
        flex-shrink: 0;
        line-height: 1;
    }
    .result-label {
        font-family: 'Syne', sans-serif;
        font-size: 26px;
        font-weight: 700;
        line-height: 1;
    }
    .result-real .result-label { color: #4ade80; }
    .result-fake .result-label { color: #f87171; }
    .result-sublabel {
        font-size: 14px;
        margin-top: 5px;
    }
    .result-real .result-sublabel { color: #16a34a; }
    .result-fake .result-sublabel { color: #b91c1c; }

    /* Confidence bar */
    .conf-section {
        margin: 24px 0;
        animation: fadeUp 0.5s 0.15s ease both;
    }
    .conf-header {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        margin-bottom: 10px;
    }
    .conf-label {
        font-size: 13px;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #475569;
        font-weight: 500;
    }
    .conf-value {
        font-family: 'Syne', sans-serif;
        font-size: 24px;
        font-weight: 700;
        color: #e2e8f0;
    }
    .conf-track {
        height: 8px;
        background: rgba(30,41,59,0.8);
        border-radius: 99px;
        overflow: hidden;
        border: 1px solid rgba(51,65,85,0.5);
    }
    .conf-fill {
        height: 100%;
        border-radius: 99px;
        background: linear-gradient(90deg, #6366f1, #8b5cf6, #c084fc);
        transition: width 1.2s cubic-bezier(0.4, 0, 0.2, 1);
        animation: fillBar 1.2s cubic-bezier(0.4, 0, 0.2, 1) both;
    }
    @keyframes fillBar {
        from { width: 0% !important; }
    }

    /* Cards for results */
    .info-card {
        background: rgba(15,23,42,0.7);
        border: 1px solid rgba(51,65,85,0.5);
        border-radius: 16px;
        padding: 22px 24px;
        margin-bottom: 16px;
        animation: fadeUp 0.5s ease both;
    }
    .info-card-title {
        font-size: 12px;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #475569;
        font-weight: 500;
        margin-bottom: 14px;
    }

    .word-chips {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
    }
    .word-chip {
        background: rgba(99,102,241,0.1);
        border: 1px solid rgba(99,102,241,0.2);
        border-radius: 99px;
        padding: 5px 14px;
        font-size: 13px;
        color: #a5b4fc;
        font-weight: 500;
    }

    .stats-mini {
        display: flex;
        gap: 20px;
        flex-wrap: wrap;
    }
    .stat-mini-item {
        display: flex;
        flex-direction: column;
        gap: 4px;
    }
    .stat-mini-val {
        font-family: 'Syne', sans-serif;
        font-size: 22px;
        font-weight: 700;
        color: #e2e8f0;
    }
    .stat-mini-lbl {
        font-size: 12px;
        color: #475569;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }

    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(14px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Highlighted text */
    .highlighted-text {
        font-size: 15px;
        line-height: 1.8;
        color: #94a3b8;
    }
    .highlighted-text mark {
        background: rgba(99,102,241,0.2);
        color: #a5b4fc;
        border-radius: 4px;
        padding: 1px 4px;
        font-weight: 500;
    }

    /* Staggered animation delays */
    .info-card:nth-child(1) { animation-delay: 0.2s; }
    .info-card:nth-child(2) { animation-delay: 0.35s; }
    .info-card:nth-child(3) { animation-delay: 0.5s; }
    .info-card:nth-child(4) { animation-delay: 0.65s; }
    </style>
    """, unsafe_allow_html=True)

    # HEADER
    st.markdown("""
    <div class="page-header">
        <div class="page-eyebrow">Real-time Analysis</div>
        <div class="page-title">Fake News Detector</div>
        <div class="page-desc">Paste any news article or headline — the AI will analyze it in seconds.</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Session state init ──
    # Use "detector_input" as the backing store — never the same key as the widget
    if "detector_input" not in st.session_state:
        st.session_state["detector_input"] = ""

    col1, col2, col3 = st.columns([5, 3, 2])
    with col1:
        analyze = st.button("🔍 Analyze with AI", use_container_width=True)
    with col2:
        sample = st.button("📌 Load Sample", use_container_width=True)
    with col3:
        clear = st.button("🗑️ Clear", use_container_width=True)

    # Handle sample — set backing store BEFORE the widget renders
    if sample:
        st.session_state["detector_input"] = "Breaking: Scientists confirm drinking coffee makes you immortal. Studies from an unknown lab in Nevada suggest that 10 cups a day reverses aging completely."

    # Handle clear — wipe backing store BEFORE the widget renders
    if clear:
        st.session_state["detector_input"] = ""

    # Textarea reads from backing store; its own key is different
    user_input = st.text_area(
        "",
        value=st.session_state["detector_input"],
        placeholder="Paste or type a news article here...",
        height=220,
        label_visibility="collapsed",
        key="detector_widget"
    )
    # Keep backing store in sync with what the user types
    st.session_state["detector_input"] = user_input

    # PREDICTION
    if analyze:
        if not user_input.strip():
            st.warning("⚠️ Please enter some text to analyze.")
        else:
            with st.spinner("🧠 Processing with AI — analyzing language patterns..."):
                import time
                time.sleep(0.4)  # brief pause for UX
                result, confidence, words = predict_news(user_input)

            is_real = "Real" in result

            # Result banner
            banner_class = "result-real" if is_real else "result-fake"
            icon = "✅" if is_real else "❌"
            sub = "Content appears credible based on learned patterns." if is_real else "Content shows patterns commonly found in false news."

            st.markdown(f"""
            <div class="result-banner {banner_class}">
                <div class="result-icon">{icon}</div>
                <div>
                    <div class="result-label">{result}</div>
                    <div class="result-sublabel">{sub}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Confidence bar
            st.markdown(f"""
            <div class="conf-section">
                <div class="conf-header">
                    <span class="conf-label">Model Confidence</span>
                    <span class="conf-value">{confidence}%</span>
                </div>
                <div class="conf-track">
                    <div class="conf-fill" style="width: {min(confidence, 100)}%"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Important words
            word_chips = "".join([f'<span class="word-chip">{w}</span>' for w in words])
            st.markdown(f"""
            <div class="info-card">
                <div class="info-card-title">🔍 Key Signal Words</div>
                <div class="word-chips">{word_chips}</div>
            </div>
            """, unsafe_allow_html=True)

            # Highlighted text
            highlighted = user_input
            for word in words:
                if word.lower() in highlighted.lower():
                    import re
                    highlighted = re.sub(
                        f'(?i)({re.escape(word)})',
                        r'<mark>\1</mark>',
                        highlighted
                    )

            st.markdown(f"""
            <div class="info-card">
                <div class="info-card-title">🧠 Highlighted Analysis</div>
                <div class="highlighted-text">{highlighted}</div>
            </div>
            """, unsafe_allow_html=True)

            # Stats
            word_count = len(user_input.split())
            char_count = len(user_input)
            unique_words = len(set(user_input.lower().split()))

            st.markdown(f"""
            <div class="info-card">
                <div class="info-card-title">📊 Text Statistics</div>
                <div class="stats-mini">
                    <div class="stat-mini-item">
                        <span class="stat-mini-val">{word_count}</span>
                        <span class="stat-mini-lbl">Words</span>
                    </div>
                    <div class="stat-mini-item">
                        <span class="stat-mini-val">{char_count}</span>
                        <span class="stat-mini-lbl">Characters</span>
                    </div>
                    <div class="stat-mini-item">
                        <span class="stat-mini-val">{unique_words}</span>
                        <span class="stat-mini-lbl">Unique Words</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
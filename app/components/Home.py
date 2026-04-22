import streamlit as st

def run():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid="stAppViewContainer"] {
        background: #020916;
    }
    [data-testid="stSidebar"] {
        background: #040d1a !important;
        border-right: 1px solid rgba(99,102,241,0.15);
    }
    [data-testid="stSidebar"] * {
        color: #cbd5e1 !important;
    }

    .hero-wrap {
        min-height: 88vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 60px 20px 40px;
        position: relative;
        overflow: hidden;
    }

    .hero-wrap::before {
        content: '';
        position: absolute;
        top: -120px; left: 50%;
        transform: translateX(-50%);
        width: 700px; height: 700px;
        background: radial-gradient(ellipse, rgba(99,102,241,0.18) 0%, rgba(139,92,246,0.08) 40%, transparent 70%);
        pointer-events: none;
    }

    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(99,102,241,0.12);
        border: 1px solid rgba(99,102,241,0.3);
        border-radius: 999px;
        padding: 6px 18px;
        font-size: 13px;
        color: #a5b4fc;
        letter-spacing: 0.05em;
        margin-bottom: 32px;
        animation: fadeSlideDown 0.7s ease both;
    }

    .hero-badge .dot {
        width: 7px; height: 7px;
        border-radius: 50%;
        background: #6366f1;
        box-shadow: 0 0 8px rgba(99,102,241,0.8);
        animation: pulse 1.8s infinite;
    }

    @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.5; transform: scale(0.85); }
    }

    .hero-title {
        font-family: 'Syne', sans-serif;
        font-size: clamp(48px, 8vw, 96px);
        font-weight: 800;
        line-height: 1.0;
        letter-spacing: -0.03em;
        color: #f8fafc;
        margin: 0 0 8px;
        animation: fadeSlideDown 0.8s 0.15s ease both;
    }

    .hero-title span {
        background: linear-gradient(135deg, #818cf8 0%, #a78bfa 50%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .hero-sub {
        font-size: clamp(17px, 2.5vw, 22px);
        color: #64748b;
        font-weight: 300;
        max-width: 520px;
        line-height: 1.65;
        margin: 18px auto 40px;
        animation: fadeSlideDown 0.9s 0.3s ease both;
    }

    @keyframes fadeSlideDown {
        from { opacity: 0; transform: translateY(-18px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .stats-row {
        display: flex;
        gap: 16px;
        justify-content: center;
        flex-wrap: wrap;
        margin: 48px 0 0;
        animation: fadeUp 1s 0.5s ease both;
    }

    .stat-card {
        flex: 1;
        min-width: 140px;
        max-width: 200px;
        background: rgba(15,23,42,0.8);
        border: 1px solid rgba(99,102,241,0.15);
        border-radius: 20px;
        padding: 28px 20px 22px;
        text-align: center;
        transition: border-color 0.3s, transform 0.3s;
        position: relative;
        overflow: hidden;
    }
    .stat-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        opacity: 0;
        transition: opacity 0.3s;
    }
    .stat-card:hover {
        border-color: rgba(99,102,241,0.4);
        transform: translateY(-6px);
    }
    .stat-card:hover::before { opacity: 1; }

    .stat-icon {
        font-size: 28px;
        margin-bottom: 14px;
        display: block;
    }
    .stat-val {
        font-family: 'Syne', sans-serif;
        font-size: 30px;
        font-weight: 700;
        color: #e2e8f0;
        line-height: 1;
    }
    .stat-lbl {
        font-size: 13px;
        color: #475569;
        margin-top: 6px;
        letter-spacing: 0.04em;
        text-transform: uppercase;
    }

    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .section {
        max-width: 900px;
        margin: 0 auto;
        padding: 0 20px 60px;
    }

    .section-label {
        font-size: 12px;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: #6366f1;
        font-weight: 500;
        margin-bottom: 14px;
    }

    .section-title {
        font-family: 'Syne', sans-serif;
        font-size: clamp(26px, 4vw, 36px);
        font-weight: 700;
        color: #f1f5f9;
        margin: 0 0 40px;
    }

    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 16px;
    }

    .feat-card {
        background: rgba(15,23,42,0.7);
        border: 1px solid rgba(51,65,85,0.6);
        border-radius: 18px;
        padding: 28px;
        transition: all 0.3s;
        position: relative;
        overflow: hidden;
    }
    .feat-card::after {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, rgba(99,102,241,0.05) 0%, transparent 60%);
        opacity: 0;
        transition: opacity 0.3s;
    }
    .feat-card:hover {
        border-color: rgba(99,102,241,0.35);
        transform: translateY(-4px);
    }
    .feat-card:hover::after { opacity: 1; }

    .feat-icon {
        width: 44px; height: 44px;
        background: rgba(99,102,241,0.12);
        border: 1px solid rgba(99,102,241,0.2);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        margin-bottom: 18px;
    }
    .feat-title {
        font-family: 'Syne', sans-serif;
        font-size: 17px;
        font-weight: 600;
        color: #e2e8f0;
        margin: 0 0 8px;
    }
    .feat-desc {
        font-size: 14px;
        color: #64748b;
        line-height: 1.65;
    }

    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(99,102,241,0.2), transparent);
        margin: 10px 0 60px;
    }

    .how-steps {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
        gap: 16px;
    }
    .step {
        background: rgba(15,23,42,0.7);
        border: 1px solid rgba(51,65,85,0.5);
        border-radius: 16px;
        padding: 24px;
        position: relative;
    }
    .step-num {
        font-family: 'Syne', sans-serif;
        font-size: 42px;
        font-weight: 800;
        color: rgba(99,102,241,0.15);
        line-height: 1;
        margin-bottom: 12px;
    }
    .step-name {
        font-size: 15px;
        font-weight: 500;
        color: #cbd5e1;
        margin-bottom: 6px;
    }
    .step-info {
        font-size: 13px;
        color: #475569;
        line-height: 1.6;
    }

    .footer-txt {
        text-align: center;
        color: #334155;
        font-size: 13px;
        padding: 30px 0 40px;
        letter-spacing: 0.03em;
    }

    /* Streamlit button override */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 14px 36px !important;
        font-family: 'Syne', sans-serif !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        letter-spacing: 0.02em !important;
        transition: all 0.3s !important;
        box-shadow: 0 8px 32px rgba(99,102,241,0.3) !important;
        min-width: 180px !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px) scale(1.02) !important;
        box-shadow: 0 12px 40px rgba(99,102,241,0.45) !important;
    }
    .stButton > button:active {
        transform: scale(0.98) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # HERO
    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-badge">
            <div class="dot"></div>
            AI-Powered Detection System
        </div>
        <div class="hero-title">
            Detect<br><span>Fake News</span><br>Instantly
        </div>
        <div class="hero-sub">
            Advanced machine learning analyzes news content in real time — 
            giving you confidence scores and key signal words.
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2,1,2])
    with col2:
        if st.button("▶ Try Detector"):
            st.success("👈 Open Detector from the sidebar")

    # STATS
    st.markdown("""
    <div class="stats-row">
        <div class="stat-card">
            <span class="stat-icon">⚡</span>
            <div class="stat-val">&lt;1s</div>
            <div class="stat-lbl">Prediction Time</div>
        </div>
        <div class="stat-card">
            <span class="stat-icon">🎯</span>
            <div class="stat-val">95%+</div>
            <div class="stat-lbl">Accuracy</div>
        </div>
        <div class="stat-card">
            <span class="stat-icon">🧠</span>
            <div class="stat-val">TF-IDF</div>
            <div class="stat-lbl">ML Feature Engine</div>
        </div>
        <div class="stat-card">
            <span class="stat-icon">🔍</span>
            <div class="stat-val">Top 10</div>
            <div class="stat-lbl">Signal Words</div>
        </div>
    </div>
    <br><br>
    """, unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # FEATURES
    st.markdown("""
    <div class="section">
        <div class="section-label">Capabilities</div>
        <div class="section-title">What makes it powerful</div>
        <div class="features-grid">
            <div class="feat-card">
                <div class="feat-icon">🔬</div>
                <div class="feat-title">Real-Time Analysis</div>
                <div class="feat-desc">Paste any news article and get instant classification with a confidence score.</div>
            </div>
            <div class="feat-card">
                <div class="feat-icon">📊</div>
                <div class="feat-title">Explainable AI</div>
                <div class="feat-desc">Know exactly which words drove the prediction — full transparency into the model's reasoning.</div>
            </div>
            <div class="feat-card">
                <div class="feat-icon">🧹</div>
                <div class="feat-title">Smart Text Cleaning</div>
                <div class="feat-desc">Automated preprocessing strips noise and stopwords before analysis begins.</div>
            </div>
            <div class="feat-card">
                <div class="feat-icon">🏋️</div>
                <div class="feat-title">Passive Aggressive Classifier</div>
                <div class="feat-desc">An online learning algorithm trained on thousands of real and fake news examples.</div>
            </div>
            <div class="feat-card">
                <div class="feat-icon">📱</div>
                <div class="feat-title">Fully Responsive</div>
                <div class="feat-desc">Works seamlessly across desktop, tablet, and mobile — no functionality lost.</div>
            </div>
            <div class="feat-card">
                <div class="feat-icon">✏️</div>
                <div class="feat-title">Word Highlighting</div>
                <div class="feat-desc">Visually identify the most influential terms directly within your submitted text.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # HOW IT WORKS
    st.markdown("""
    <div class="section">
        <div class="section-label">Pipeline</div>
        <div class="section-title">How it works</div>
        <div class="how-steps">
            <div class="step">
                <div class="step-num">01</div>
                <div class="step-name">Text Input</div>
                <div class="step-info">Paste or type any news content into the detector.</div>
            </div>
            <div class="step">
                <div class="step-num">02</div>
                <div class="step-name">Clean & Preprocess</div>
                <div class="step-info">Noise, punctuation, and common words are removed.</div>
            </div>
            <div class="step">
                <div class="step-num">03</div>
                <div class="step-name">TF-IDF Vectorize</div>
                <div class="step-info">Text is converted into a numerical feature vector.</div>
            </div>
            <div class="step">
                <div class="step-num">04</div>
                <div class="step-name">Model Predict</div>
                <div class="step-info">Classifier outputs Real or Fake with a confidence score.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer-txt">
        Built with Machine Learning & Streamlit &nbsp;·&nbsp; PassiveAggressiveClassifier + TF-IDF
    </div>
    """, unsafe_allow_html=True)
import streamlit as st

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

    .about-header {
        padding: 60px 0 48px;
        max-width: 640px;
        margin: 0 auto;
        text-align: center;
    }
    .about-eyebrow {
        font-size: 12px;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: #6366f1;
        font-weight: 500;
        margin-bottom: 14px;
    }
    .about-title {
        font-family: 'Syne', sans-serif;
        font-size: clamp(30px, 5vw, 50px);
        font-weight: 800;
        color: #f8fafc;
        letter-spacing: -0.025em;
        line-height: 1.08;
        margin: 0 0 16px;
    }
    .about-desc {
        font-size: 17px;
        color: #475569;
        line-height: 1.75;
    }

    .content-wrap {
        max-width: 820px;
        margin: 0 auto;
        padding: 0 16px 60px;
    }

    .block-card {
        background: rgba(15,23,42,0.75);
        border: 1px solid rgba(51,65,85,0.5);
        border-radius: 20px;
        padding: 28px 32px;
        margin-bottom: 20px;
        position: relative;
        overflow: hidden;
        animation: fadeUp 0.6s ease both;
    }

    .block-card-accent {
        position: absolute;
        top: 0; left: 0;
        width: 4px;
        height: 100%;
        background: linear-gradient(180deg, #6366f1, #8b5cf6);
        border-radius: 4px 0 0 4px;
    }

    .block-title {
        font-family: 'Syne', sans-serif;
        font-size: 18px;
        font-weight: 700;
        color: #e2e8f0;
        margin: 0 0 12px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .block-text {
        font-size: 15px;
        color: #64748b;
        line-height: 1.8;
    }
    .block-text strong {
        color: #94a3b8;
        font-weight: 500;
    }

    /* Pipeline steps */
    .pipeline {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
        gap: 12px;
        margin-top: 18px;
    }
    .pipe-step {
        background: rgba(8,14,32,0.7);
        border: 1px solid rgba(99,102,241,0.15);
        border-radius: 14px;
        padding: 18px 16px;
        position: relative;
    }
    .pipe-num {
        font-family: 'Syne', sans-serif;
        font-size: 11px;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #6366f1;
        font-weight: 600;
        margin-bottom: 8px;
    }
    .pipe-name {
        font-size: 14px;
        font-weight: 500;
        color: #cbd5e1;
        margin-bottom: 5px;
    }
    .pipe-desc {
        font-size: 12px;
        color: #475569;
        line-height: 1.55;
    }
    .pipe-arrow {
        position: absolute;
        top: 50%; right: -8px;
        transform: translateY(-50%);
        color: #334155;
        font-size: 16px;
        z-index: 2;
    }

    /* Why it matters bullets */
    .bullet-list {
        list-style: none;
        padding: 0; margin: 0;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    .bullet-list li {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        font-size: 15px;
        color: #64748b;
        line-height: 1.65;
    }
    .bullet-list li::before {
        content: '';
        width: 6px; height: 6px;
        border-radius: 50%;
        background: #6366f1;
        margin-top: 8px;
        flex-shrink: 0;
    }

    /* Tech stack badges */
    .tech-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 18px;
    }
    .tech-badge {
        background: rgba(99,102,241,0.08);
        border: 1px solid rgba(99,102,241,0.2);
        border-radius: 10px;
        padding: 8px 16px;
        font-size: 13px;
        color: #a5b4fc;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 7px;
    }

    /* Stagger */
    .block-card:nth-child(1) { animation-delay: 0.05s; }
    .block-card:nth-child(2) { animation-delay: 0.15s; }
    .block-card:nth-child(3) { animation-delay: 0.25s; }
    .block-card:nth-child(4) { animation-delay: 0.35s; }
    .block-card:nth-child(5) { animation-delay: 0.45s; }
    .block-card:nth-child(6) { animation-delay: 0.55s; }

    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(18px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .footer-txt {
        text-align: center;
        color: #1e293b;
        font-size: 13px;
        padding: 20px 0 40px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="about-header">
        <div class="about-eyebrow">Documentation</div>
        <div class="about-title">About this System</div>
        <div class="about-desc">
            An end-to-end machine learning pipeline for detecting misinformation — 
            transparent, explainable, and fast.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="content-wrap">', unsafe_allow_html=True)

    # What is fake news
    st.markdown("""
    <div class="block-card">
        <div class="block-card-accent"></div>
        <div class="block-title">📰 What is Fake News?</div>
        <div class="block-text">
            Fake news refers to false or misleading content presented as legitimate journalism.
            It's engineered to influence opinion, generate engagement, or spread propaganda.
            In the age of social media, misinformation propagates faster than corrections — 
            making automated detection tools an essential part of the information ecosystem.
        </div>
    </div>

    <div class="block-card">
        <div class="block-card-accent"></div>
        <div class="block-title">⚠️ Why Detection Matters</div>
        <ul class="bullet-list">
            <li>Prevents mass misinformation from distorting public decisions</li>
            <li>Helps protect trust in legitimate journalism and scientific reporting</li>
            <li>Reduces the spread of health, political, and financial disinformation</li>
            <li>Demonstrates how AI can be applied to real societal challenges</li>
        </ul>
    </div>

    <div class="block-card">
        <div class="block-card-accent"></div>
        <div class="block-title">🧠 How the Model Works</div>
        <div class="block-text">
            The system uses Natural Language Processing and a <strong>Passive Aggressive Classifier</strong> 
            — an online learning algorithm well-suited for text classification tasks. 
            It was trained on a labeled dataset of real and fake news articles.
        </div>
        <div class="pipeline">
            <div class="pipe-step">
                <div class="pipe-num">Step 01</div>
                <div class="pipe-name">Text Cleaning</div>
                <div class="pipe-desc">URLs, punctuation, numbers & stopwords removed</div>
            </div>
            <div class="pipe-step">
                <div class="pipe-num">Step 02</div>
                <div class="pipe-name">TF-IDF Vectorize</div>
                <div class="pipe-desc">Text converted to weighted numeric features</div>
            </div>
            <div class="pipe-step">
                <div class="pipe-num">Step 03</div>
                <div class="pipe-name">Classify</div>
                <div class="pipe-desc">PAClassifier predicts Real (1) or Fake (0)</div>
            </div>
            <div class="pipe-step">
                <div class="pipe-num">Step 04</div>
                <div class="pipe-name">Explain</div>
                <div class="pipe-desc">Top TF-IDF features surface the key signal words</div>
            </div>
        </div>
    </div>

    <div class="block-card">
        <div class="block-card-accent"></div>
        <div class="block-title">🔍 What the Model Detects</div>
        <div class="block-text">
            The model doesn't "read" news — it learns <strong>statistical patterns</strong> 
            from language. Fake news articles often use sensational verbs, 
            emotionally charged language, vague attribution, and unusual writing cadence. 
            The model picks up on these signals through TF-IDF feature weights 
            learned from thousands of labeled examples.
        </div>
    </div>

    <div class="block-card">
        <div class="block-card-accent"></div>
        <div class="block-title">🛠️ Tech Stack</div>
        <div class="tech-grid">
            <div class="tech-badge">🐍 Python 3</div>
            <div class="tech-badge">📊 scikit-learn</div>
            <div class="tech-badge">🧮 TF-IDF Vectorizer</div>
            <div class="tech-badge">🤖 PassiveAggressiveClassifier</div>
            <div class="tech-badge">🌐 Streamlit</div>
            <div class="tech-badge">📦 joblib</div>
            <div class="tech-badge">🔢 NumPy</div>
            <div class="tech-badge">🗃️ pandas</div>
        </div>
    </div>

    <div class="block-card">
        <div class="block-card-accent"></div>
        <div class="block-title">👨‍💻 Developer Notes</div>
        <div class="block-text">
            This project showcases a complete ML pipeline — from raw CSV ingestion and text preprocessing 
            through model training, serialization with <strong>joblib</strong>, and deployment via 
            a responsive Streamlit interface. It was originally built with ChatGPT assistance 
            and subsequently improved with Claude for UI polish, responsiveness, and UX refinement.
            <br><br>
            The model achieves <strong>95%+ accuracy</strong> on the standard Fake/Real news dataset 
            (Kaggle). Note that real-world performance depends heavily on article domain and writing style.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="footer-txt">
        Fake News AI · Built with Machine Learning & Streamlit
    </div>
    """, unsafe_allow_html=True)
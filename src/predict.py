import joblib
import numpy as np
from src.data_preprocessing import clean_text

model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

feature_names = np.array(vectorizer.get_feature_names_out())


def predict_news(text):
    cleaned = clean_text(text)
    vector = vectorizer.transform([cleaned])

    prediction = model.predict(vector)[0]

    # Some models don't support predict_proba
    try:
        prob = model.decision_function(vector)[0]
        confidence = min(abs(prob) * 100, 100)
    except:
        confidence = 75  # fallback

    # Important words
    vec_array = vector.toarray()[0]
    indices = vec_array.argsort()[-10:]
    important_words = feature_names[indices]

    # ✅ FIXED LABEL LOGIC
    result = "Real News ✅" if prediction == 1 else "Fake News ❌"

    return result, round(confidence, 2), important_words
import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score

from src.data_preprocessing import clean_text


def train():
    BASE_DIR = os.getcwd()

    fake_path = os.path.join(BASE_DIR, "data", "raw", "Fake.csv")
    true_path = os.path.join(BASE_DIR, "data", "raw", "True.csv")

    fake_df = pd.read_csv(fake_path)
    true_df = pd.read_csv(true_path)

    # Labels (IMPORTANT)
    fake_df["label"] = 0
    true_df["label"] = 1

    df = pd.concat([fake_df, true_df], axis=0)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    df["content"] = df["title"] + " " + df["text"]
    df["clean_text"] = df["content"].apply(clean_text)

    X = df["clean_text"]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    vectorizer = TfidfVectorizer(max_df=0.7)

    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # 🔥 Better model
    model = PassiveAggressiveClassifier(max_iter=1000)
    model.fit(X_train_vec, y_train)

    y_pred = model.predict(X_test_vec)

    print("Accuracy:", accuracy_score(y_test, y_pred))

    os.makedirs("models", exist_ok=True)

    joblib.dump(model, "models/model.pkl")
    joblib.dump(vectorizer, "models/vectorizer.pkl")


if __name__ == "__main__":
    train()
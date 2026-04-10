import re
import string

# Basic stopwords
stop_words = set([
    "the","is","in","and","to","of","a","for","on","with","as","at","by","an","be","this","that","from"
])

def clean_text(text):
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)

    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]

    return " ".join(tokens)
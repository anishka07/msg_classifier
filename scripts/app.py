import nltk
import pickle
import string
import streamlit as st
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from settings import Settings

ps = PorterStemmer()
model_pkl_path = Settings.MODEL_PATH
vectorizer_pkl_path = Settings.VECTORIZER_PATH


def text_transformer(text):
    text = text.lower()
    text = nltk.word_tokenize(text)  # Tokenization
    y = [i for i in text if i.isalnum()]  # Remove special characters
    texts = y[:]
    y.clear()
    y = [i for i in texts if
         i not in stopwords.words('english') and i not in string.punctuation]  # Remove stop words and punctuation
    texts = y[:]
    y.clear()
    y = [ps.stem(i) for i in texts]  # Stemming
    return ' '.join(y)


vectorizer = pickle.load(open(vectorizer_pkl_path, "rb"))
model = pickle.load(open(model_pkl_path, "rb"))

st.title("Message/Email Spam Classifier")

input_msg = st.text_area("Enter your message/email")

if st.button("Predict"):
    transformed_sms = text_transformer(input_msg)
    vector_input = vectorizer.transform([transformed_sms])
    result = model.predict(vector_input)[0]
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")

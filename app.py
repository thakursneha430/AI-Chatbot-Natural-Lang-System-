import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
texts = ["hello", "hi", "hey", "how are you", "what is your name", "bye"]
labels = ["greeting", "greeting", "greeting", "greeting", "name", "goodbye"]

# Vectorization
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Response dictionary
responses = {
    "greeting": "Hello! Nice to meet you 🙂",
    "name": "I am an AI Chatbot built with Python.",
    "goodbye": "Goodbye! Have a great day!"
}

# Function to predict intent
def get_response(user_input):
    user_vec = vectorizer.transform([user_input])
    intent = model.predict(user_vec)[0]
    return responses.get(intent, "Sorry, I didn't understand that.")

# Streamlit UI
st.title("🤖 AI Chatbot")
st.write("Simple NLP Chatbot using Python")

user_input = st.text_input("You:")

if user_input:
    response = get_response(user_input)
    st.text("Bot: " + response)
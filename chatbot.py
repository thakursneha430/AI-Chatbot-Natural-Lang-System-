from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from training_data import texts, labels

# Convert text into numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train the classifier
model = MultinomialNB()
model.fit(X, labels)

# Function to predict intent
def predict_intent(user_input):
    user_vec = vectorizer.transform([user_input])
    intent = model.predict(user_vec)[0]
    return intent

# Chatbot responses
responses = {
    "greeting": "Hello! Nice to meet you 🙂",
    "name": "I am an AI chatbot built using Python and NLP.",
    "goodbye": "Goodbye! Have a great day!"
}

# Function to get chatbot response
def get_response(user_input):
    intent = predict_intent(user_input)
    return responses.get(intent, "Sorry, I didn't understand that.")
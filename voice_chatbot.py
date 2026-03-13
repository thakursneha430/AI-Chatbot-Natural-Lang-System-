import speech_recognition as sr
import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initialize recognizer
recognizer = sr.Recognizer()

# Chatbot responses
responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there!",
    "how are you": "I am doing great.",
    "what is your name": "I am your AI voice chatbot.",
    "bye": "Goodbye! Have a nice day."
}

print("Voice Chatbot is running... Say something!")

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        # Convert speech to text
        text = recognizer.recognize_google(audio)
        text = text.lower()

        print("You said:", text)

        # Find response
        response = responses.get(text, "Sorry, I didn't understand that.")

        print("Bot:", response)
        speak(response)

        if text == "bye":
            break

    except sr.UnknownValueError:
        print("Sorry, I could not understand your voice.")
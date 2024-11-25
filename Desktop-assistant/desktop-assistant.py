import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and the speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech and return it as text
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "Sorry, I did not understand that."
        except sr.RequestError:
            print("Sorry, there is a problem with the speech recognition service.")
            return "Sorry, there is a problem with the speech recognition service."

# Function to process commands
def process_command(command):
    command = command.lower()
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "your name" in command:
        speak("I am your desktop assistant.")
    elif "how are you" in command:
        speak("I am fine, thank you. How can I assist you?")
    elif "time" in command:
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I did not understand that command.")

# Main loop
while True:
    command = recognize_speech()
    process_command(command)

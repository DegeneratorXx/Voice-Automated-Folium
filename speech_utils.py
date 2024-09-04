import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    """Speaks the given text using text-to-speech."""
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """Recognizes speech and returns the recognized text as a string, or None if there's an error or no speech is detected."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a location (say 'stop' to end)...")
        speak("Listening for a location. Say 'stop' to end.")

        while True:
            audio = recognizer.listen(source)
            try:
                location = recognizer.recognize_google(audio).strip()
                if location.lower() == "stop":
                    speak("Stopping the speech recognition.")
                    print("Stopping the speech recognition.")
                    return "stop"
                
                response = f"You said {location}. Showing the location now."
                speak(response)
                print(response)
                return location
            except sr.UnknownValueError:
                speak("Sorry, I did not understand the audio.")
                print("Sorry, I did not understand the audio.")
            except sr.RequestError:
                speak("Could not request results; check your internet connection.")
                print("Could not request results; check your internet connection.")
                
    return None

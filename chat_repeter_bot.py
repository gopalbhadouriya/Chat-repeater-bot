import speech_recognition as sr
import pyttsx3

def setup_speech_engine():
    """Initialize the speech engine."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
    return engine

def recognize_speech(recognizer, microphone):
    """Recognize speech using the given recognizer and microphone."""
    with microphone as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was a problem with the speech recognition service.")
            return None

def speak_text(engine, text):
    """Speak the given text using the speech engine."""
    engine.say(text)
    engine.runAndWait()

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    engine = setup_speech_engine()

    print("Say something...")
    while True:
        text = recognize_speech(recognizer, microphone)
        if text:
            speak_text(engine, text)
        else:
            speak_text(engine, "Please try again.")

if __name__ == "__main__":
    main()








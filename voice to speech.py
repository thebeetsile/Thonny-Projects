import pyttsx3
import speech_recognition as sr

# Initialize the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Set properties for the voice
engine.setProperty('rate', 150)    # Speed in words per minute
engine.setProperty('volume', 0.8)  # Volume level between 0 and 1
engine.setProperty('voice', 'english+f3')  # Female voice type

# Take input verbally and convert to text
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print(f"You said: {text}")
    engine.say(f"You said: {text}")
    engine.runAndWait()

except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")

except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
    
except Exception as e:
    print(f"An error occurred; {e}")

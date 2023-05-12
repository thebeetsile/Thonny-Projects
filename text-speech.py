import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Set properties for the voice
engine.setProperty('rate', 110)     # Speed in words per minute
engine.setProperty('volume', 0.5)   # Volume level between 0 and 1
engine.setProperty('voice', 'english')

# Convert text to speech
engine.say("Hello, how are you?")
engine.runAndWait()

# Add a pause
engine.setProperty('rate', 100)     # Slow down the speech rate for the pause

# Convert text to speech
engine.say("I am fine. And how are you?")
engine.runAndWait()

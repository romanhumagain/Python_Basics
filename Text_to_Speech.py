import pyttsx3

# Initialize the pyttsx3
speech = pyttsx3.init()

# Taking text from the user
text = input("Please write something -> ")

# Set speech rate and volume
speech.setProperty('rate', 150)
speech.setProperty('volume', 0.8)

# Convert text to speech
speech.say(text)

# to process and generate the output
speech.runAndWait()

import pyttsx3
list = ["ritik","anuj","tanu"]
engine = pyttsx3.init()
for i in list:
    engine.say(f"shoutout to {i}")
engine.runAndWait()
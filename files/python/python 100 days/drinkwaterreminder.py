import pyttsx3
import time
reminder="hey Anuj Drink water and take breaks in between and take care of your health"
engine = pyttsx3.init()
while True:
    time.sleep(7200)
    engine.say(f"{reminder}")
    engine.runAndWait()
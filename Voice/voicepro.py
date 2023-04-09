import gtts
from playsound import playsound
import pyttsx3

engine = pyttsx3.init()
text = input('Введите текст, который будем озвучивать:')

# engine.getProperty('rate',300)
engine.say(text)
engine.runAndWait()

# voices = engine.getProperty('voices')
# print(voices)

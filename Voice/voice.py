# pip install gTTS playsound (Скачиваем модуль)

# Импортируем модули
import gtts
from playsound import playsound

# Пишем код
def voice(name):
    tts = gtts.gTTS(name, lang='ru', slow = False)
    tts.save('audio.mp3')
    playsound('audio.mp3')

# Вызываем функцию
while True:
    voice(input('Введи текст, который будем озвучивать: '))

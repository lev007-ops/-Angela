import speech_recognition as sr
import pyttsx3
from gtts import gTTS
from tqdm import tqdm
from time import sleep
import webbrowser
import os
from colorama import init
init()

hello_text = "Привет. Я голосовой помощник Анжелла. Узнать больше обо мне можно произнеся \"Анжелла раскажи о себе\""

engine = pyttsx3.init()
for i in tqdm(range(100)):
    sleep(0.00000001)





def listen_command():
    r = sr.Recognizer()
    with sr.Microphone(device_index = 1) as source:
        print('Настраиваю микрофон')
        r.adjust_for_ambient_noise(source, duration=0.5) #настройка посторонних шумов
        print('Скажите вашу команду:')
        audio = r.listen(source)
    print('Услышала...')
    try:
        our_sp = r.recognize_google(audio, language = 'ru-RU')
        print(Back.GREEN)
        print('Вы сказали: ' + our_sp)
        return our_sp

        text = query.lower()
    except:
        return 'Не распознала'



def say_message(message):
    print(message)
    engine.say(message)
    engine.runAndWait()

say_message(hello_text)




def do_this_command(message):
    message = message.lower()
    if "анжела" in message:





        
        if "привет" in message:
            say_message("Привет друг!")
        elif "пока" in message:
            say_message("Пока!")
            exit()

        elif "открой habr вопросы" in message:
            say_message("Открываю хабр q&a")
            webbrowser.open('https://qna.habr.com/')
        elif "открой chrome" in message:
            say_message("Открываю google Chrome")
            os.startfile("C:/Program Files/Google/Chrome/Application/chrome.exe")
        elif "открой хром" in message:
            say_message("Открываю google Chrome")
            os.startfile("C:/Program Files/Google/Chrome/Application/chrome.exe")

        elif "открой tiktok" in message:
            webbrowser.open('https://www.tiktok.com/ru-RU?lang=ru-RU')
            say_message("Открываю тик ток")

        elif "открой instagram" in message:
            webbrowser.open('https://www.instagram.com/levman5_/?hl=ru')
            say_message("Открываю инстаграм")

        elif "открой инстаграм" in message:
            webbrowser.open('https://www.instagram.com/levman5_/?hl=ru')
            say_message("Открываю инстаграм")

        elif "открой telegram" in message:
            webbrowser.open('https://web.telegram.org/z/#93372553')
            say_message("Открываю телеграм")

        elif "открой телеграм" in message:
            webbrowser.open('https://web.telegram.org/z/#93372553')
            say_message("Открываю телеграм")

        elif "открой discord" in message:
            os.startfile('C:/Users/Дом/AppData/Local/Discord/Update.exe --processStart Discord.exe')
            say_message('Открываю Discord')
        
        elif "открой дискорд" in message:
            os.startfile('C:/Users/Дом/AppData/Local/Discord/Update.exe --processStart Discord.exe')
            say_message('Открываю Discord')


        elif "расскожи о себе" in message:
            info = "Я Анжелла. Голосовой помошник разработанный levman5. Ссылка на мой репозиторий в GitHub вывелась в консоль."
            say_message(info)
            print(info)

        else:
            say_message("Данной команды не существует!")

        








    elif "пока" in message:
            say_message("Пока!")
            exit()

        


            
    else:
        pass

while True:
    command = listen_command()
    do_this_command(command)
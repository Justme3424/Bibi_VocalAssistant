import os
import sys
import subprocess
import pkg_resources


def install_dep():
   required = {'datetime == 4.5','pyttsx3 == 2.90 ', 'SpeechRecognition == 3.8.1', 'PyAudio == 0.2.12'}
   installed = {pkg.key for pkg in pkg_resources.working_set}
   missing = required - installed
   if missing:
      python = sys.executable
      subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

install_dep()

import datetime
import operator
import webbrowser
from pyttsx3 import init
import locale
from speech_recognition import Recognizer, Microphone
from PIL import Image




engine = init()

#print("Ciao sono Bibi, quando avrai bisogno di me di: Hey Bibi")
#engine.say("Ciao sono Bibi, quando avrai bisogno di me di: hey bibi")
print("Ciao sono Bibi, dimmi cosa ti serve?")
engine.say("Ciao sono Bibi,dimmi cosa ti serve?")
engine.runAndWait()

def speak(risp):
    engine.say(risp)
    engine.runAndWait()
    #engine.getProperty("voices")


def listen():
    r = Recognizer()  # oggetto riconoscitore vocale
    #print(Microphone.list_microphone_names())
    with Microphone(device_index=1) as source: #accendo mic
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source) #genera audio
        try:
            return r.recognize_google(audio, language="it-IT").lower()#converte audio in testo
        except:
            print("listen error")


def commands(text):
    if "ora" in text:
        risp = f"sono le{datetime.datetime.now().strftime('%H e %M')}"
        speak(risp)
    elif "giorno" in text:
        locale.setlocale(locale.LC_TIME, "it-IT")
        risp = f"oggi è{datetime.datetime.today().strftime('%A %d %B')}"
        speak(risp)
    elif "musica" in text:
        os.startfile("C://Users//sabri//AppData//Local//Microsoft//WindowsApps//Spotify.exe")
    elif "youtube" in text:
        speak("Cosa vuoi cercare?")
        keyword = listen()
        if keyword != '':
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.get().open(url)
            speak(f"Ecco i risultati su youtube per {keyword}")
    elif "cerca" in text:
        speak("Cosa vuoi cercare?")
        keyword = listen()
        if keyword != '':
            #for url in googlesearch.search(keyword, num_results=3):
            webbrowser.get().open(f"https://www.google.com/search?q={keyword}")
            speak(f"ecco i risultati su google per {keyword}")
    elif "calcola" in text: #DA SISTEMARE!!!!
        speak("Cosa vuoi calcolare?")
        keyword = listen()
        if keyword != '':
            speak(eval_binary_expr(*(listen().split())))
    elif "discord" in text:
        os.startfile("C://Users//sabri//Desktop//Discord.lnk")
    elif "ho finito" in text:
        speak("Alla prossima")
        #image.close()
        exit()


def get_operator_fn(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        'x' : operator.mul,
        'divided' :operator.__truediv__,
        'Mod' : operator.mod,
        'mod' : operator.mod,
        '^' : operator.xor,
        }[op]


def eval_binary_expr(op1, oper, op2):
    op1,op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)


WAKE = "b&b"
#
#while True:
#        print("Sto ascoltando :)")
#        text = listen()
#        if text == WAKE:
#            speak('dimmi')
#            image = Image.open('C://Users//sabri//PycharmProjects//BibiVocal//Bibi.png')
#            image.reduce(200)
#            image.show()
#            text = listen()
#            while text != 'no':
#                commands(text)
#                print(text)
#        else:
#            print(text)

while True:
    print("Sto ascoltando :)")
    text = listen()
    commands(text)
    #image = Image.open('C://Users//sabri//PycharmProjects//BibiVocal//Bibi.png')
    #image.reduce(200)
    #image.show()
    print(text)


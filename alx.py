import speech_recognition as sr 
import webbrowser
from datetime import datetime
import os, pyaudio, random
from gtts import gTTS 
import wikipedia
import time
import sys

#variabile
wikipedia.set_lang("ro")
ro = 'ro'
r = sr.Recognizer()
voicee = ''
#Diacritice : ă

#mp3
startup = 'start.mp3'
intrr = 'Bine lol'
greetings1 = 'Bună'
finish = 'finish.mp3'
term1 = 'La revedere' 
salut = 'Salut!'
rim = 'Totul pare mare atunci cand esti mic Nu-i nimic Totul pare de neatins Nu te lasa invins Vorbesc de pace, si-arata armele Cum viata mea cand toti trebuia sa fim egali din nastere'

#liste

#gtts variabile
s = gTTS(text=salut, lang=ro , slow=False)
intrrr  = gTTS(text=intrr, lang=ro, slow=False)
gr1 = gTTS(text=greetings1, lang=ro, slow=False) 
fn1 = gTTS(text=term1, lang=ro, slow=False) 


#gtts salvari variabile
intrrr.save('int.mp3')
s.save('salut.mp3')
gr1.save("gr1.mp3")
fn1.save("fn1.mp3")



#inregistrare sunet
def sound():
    os.system("mpg321 start.mp3")
    time.sleep(1)
    os.system("mpg321 ping.mp3")
    with sr.Microphone() as source:
        ff = r.listen(source)
        try:
            global voicee
            print("Text: "+r.recognize_google(ff, language = "ro-RO"))
            voicee = r.recognize_google(ff, language = "ro-RO")
        except:
           os.system("mpg321 fn1.mp3")



sound()
if 'salut' in voicee :
    os.system("mpg321 salut.mp3")
    os.system("mpg321 fn1.mp3")
    os.system("python pp.py")
elif 'ce faci' in voicee :
    os.system("mpg321 int.mp3")
    os.system("mpg321 fn1.mp3")
    os.system("python pp.py")
elif 'caută pe Wikipedia' in voicee :
    os.system("mpg321 ping.mp3")
    with sr.Microphone() as source:
        fuc = r.listen(source)
        try:
            print("Text: "+r.recognize_google(fuc, language = "ro-RO"))
            wikip = r.recognize_google(fuc, language = "ro-RO")
            os.system("mpg321 ping.mp3")
        except:
           os.system("mpg321 fn1.mp3")
           os.system("python pp.py")
    res = str(wikipedia.summary(wikip, sentences=2))
    fin = gTTS(text=res, lang=ro , slow=False)
    fin.save("wikipedia.mp3")
    os.system("mpg321 wikipedia.mp3")
    os.system("python pp.py")
elif "Caută pe Facebook" in voicee :
    os.system("mpg321 ping.mp3")
    with sr.Microphone() as source:
        fac = r.listen(source)
        try:
            print("Text: "+r.recognize_google(fac, language = "ro-RO"))
            fb = r.recognize_google(fac, language = "ro-RO")
        except:
           os.system("mpg321 fn1.mp3")
           os.system("python3.6 alx.py")
    webbrowser.open("https://www.facebook.com/search/top/?q=" + fb)
    os.system("python pp.py")
elif "pune muzică" in voicee :
    os.system("mpg321 ping.mp3")
    with sr.Microphone() as source:
        you = r.listen(source)
        try:
            print("Text: "+r.recognize_google(you, language = "ro-RO"))
            yt = r.recognize_google(you, language = "ro-RO")
            os.system("mpg321 ping.mp3")
        except:
           os.system("mpg321 fn1.mp3")
           os.system("python pp.py")
    #os.system(f"youtube-dl -o 'muzica.%(ext)s' 'ytsearch1:{muzi}'")
    # youtube-dl -x --audio-format mp3 https://www.youtube.com/watch?v=jwD4AEVBL6Q
    os.system(f"youtube-dl  -x --audio-format mp3 -o 'muzica.%(ext)s' 'ytsearch1:{yt}'")
    os.system("mpg321 muzica.mp3")
    os.system("rm muzica.mp3")
    os.system("python pp.py")
# hour â

elif "Cât e ceasul" in voicee :
    os.system("mpg321 ping.mp3")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    timm = gTTS(text=current_time, lang=ro , slow=False)
    timm.save("time.mp3")
    os.system("mpg321 time.mp3")
    os.system("python pp.py")

elif "secret" in voicee :
    os.system(f"youtube-dl  -x --audio-format mp3 -o 'sec.%(ext)s' 'ytsearch1:{yt}'")
    os.system("mpg321 sec.mp3")
    os.system("rm sec.mp3")
    os.system("python pp.py")
else :
    os.system("python pp.py")


#https://www.youtube.com/watch?v=UfumsRKSpeo

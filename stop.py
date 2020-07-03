import snowboydecoder
import os

def detected_callback():
    print "hotword detected"
    os.system("mpg321 pin.mp3")
    os.system("pkill -f alx.py")
    os.system("python3.6 alx.py")
    



while True :
    detector = snowboydecoder.HotwordDetector("Stop.pmdl", sensitivity=0.5, audio_gain=1)
    detector.start(detected_callback)

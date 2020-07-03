import snowboydecoder
import os

def detected_callback():
    print "hotword detected"
    os.system("mpg321 pin.mp3")
    os.system("python3.6 alx.py")
    
detector = snowboydecoder.HotwordDetector("Ok PC.pmdl", sensitivity=0.5, audio_gain=1)
detector.start(detected_callback)

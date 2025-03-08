import requests
from gtts import gTTS
import os
import subprocess as s
import cv2
import ctypes
import _thread                   
import random
#ctypes.windll.user32.SystemParametersInfoW(20,0,"F:FANA experiment\posters\ai.gif", 0) 
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

session.get("https://jams-jnnce.in/aicmd.txt")

def dispimage( threadName, img):
   cv2.namedWindow("AIML", cv2.WND_PROP_FULLSCREEN)
   cv2.setWindowProperty("AIML",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

import winreg, ctypes, win32con

FILL,FIT,STRETCH,TILE,CENTER,SPAN = 0,1,2,3,4,5
MODES = (0,10),(0,6),(0,2),(1,0),(0,0),(0,22)
value1,value2 = MODES[FIT] # choose mode here

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, winreg.KEY_WRITE)
winreg.SetValueEx(key, "TileWallpaper", 0, winreg.REG_SZ, str(value1))
winreg.SetValueEx(key, "WallpaperStyle", 0, winreg.REG_SZ, str(value2))
winreg.CloseKey(key)
posters="F:\\FANA experiment\\posters"    
ctypes.windll.user32.SystemParametersInfoW(20,6,posters+'\\fana1.jpg', 3)
storecmd=""
0
cnt=-1

while True:

    try:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
        url = 'https://jams-jnnce.in//getAICMD.php'
        

        x = session.get("https://jams-jnnce.in/aicmd.txt",headers=headers)
        #print(storecmd,x)
        
        if storecmd==x.text.strip():
            continue                            
        storecmd=x.text.strip()
        #print(x.text)
        if x.text.strip()=="clap":
             s.call(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe ', '-Incurse  ','audios\\standard clap_Audio Trimmer.wav', 'vlc://quit'])
        elif x.text.strip()=="invite":
             ctypes.windll.user32.SystemParametersInfoW(20,0,posters+'\\fana1.jpg', 3)
             cmd="Namaskara..Hi Everyone...My name is FANA one of your favourite anchor. Welcome you all for this auspicious occasion. Enjoy the program..will come back soon"
             language = 'en'
             mobj = gTTS(text=cmd, lang=language, slow=False)
             mobj.save("aicmd.mp3")
             s.call(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe ', '-Incurse  ','aicmd.mp3', 'vlc://quit'])
        elif x.text.strip()=="reset":
              ctypes.windll.user32.SystemParametersInfoW(20,6,posters+'\\fana1.jpg', 3)
              storecmd=""
        elif x.text.strip()=="clap1":
             s.call(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe ', '-Incurse  ','audios\\clap with whistle_Audio Trimmer.wav', 'vlc://quit'])
        elif x.text.strip()=="clap2":
             s.call(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe ', '-Incurse  ','audios\\loud applause_Audio Trimmer.wav', 'vlc://quit'])
        elif x.text.strip()=="clap3":
             s.call(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe ', '-Incurse  ','audios\\ambience_Audio Trimmer.wav', 'vlc://quit'])
        elif x.text.strip()=="tsir":
            cmd="Thank you Sir"
            language = 'en'
            mobj = gTTS(text=cmd, lang=language, slow=False)
            mobj.save("aicmd.mp3")
            s.call(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe ', '-Incurse  ','aicmd.mp3', 'vlc://quit'])
        elif x.text=="tmam":
            cmd="Thank you Mam"
            language = 'en'
            mobj = gTTS(text=cmd, lang=language, slow=False)
            mobj.save("aicmd.mp3")
            s.call(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe ', '-Incurse  ','aicmd.mp3', 'vlc://quit'])
        elif x.text.strip()=="cjohar":
            cmd="I request  Sayyed Johar Sir to give away prizes"
            language = 'en'
            mobj = gTTS(text=cmd, lang=language, slow=False)
            mobj.save("aicmd.mp3")
            s.call(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe ', '-Incurse  ','aicmd.mp3', 'vlc://quit'])
        elif x.text.strip()=="cashwini":
            cmd="I request Ashwini Mam to give away prizes"
            language = 'en'
            mobj = gTTS(text=cmd, lang=language, slow=False)
            mobj.save("aicmd.mp3")
            # audio = AudioSegment.from_mp3("aicmd.mp3")
        
            # audio.speedup(playback_speed=12.0) # speed up by 2x
                
            # # export to mp3
            # audio.export("aicmd.mp3", format="mp3")

            s.call(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe ', '-Incurse  ','aicmd.mp3', 'vlc://quit'])
        elif x.text.strip()=="cchetan":
            cmd="I request Chetan Sir to give away prizes"
            language = 'en'
            mobj = gTTS(text=cmd, lang=language, slow=False)
            mobj.save("aicmd.mp3")
            # audio = AudioSegment.from_mp3("aicmd.mp3")
        
            # audio.speedup(playback_speed=12.0) # speed up by 2x
                
            # # export to mp3
            # audio.export("aicmd.mp3", format="mp3")
            
            s.call(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe ', '-Incurse  ','aicmd.mp3', 'vlc://quit'])
                                   
        elif(x.text.strip()=="jokes"):
           cnt=(cnt+1)%4
           
           s.call(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe ', '-Incurse  ','audios\\Troll'+str(cnt+1)+'.mp3', 'vlc://quit'])
           continue

         
        elif(x.text.strip()==""):
            continue
        
        else:
            arr=x.text.strip().split("###")
            event=arr[1].strip()
            print(event)
            if event=="Quiz":
                #print('here')
                #import ctypes
                #img = cv2.imread('quizposter.jpg')
                #thread.start_new_thread( dispimage, ("Thread-1", img, ) )
                #cv2.namedWindow("AIML", cv2.WND_PROP_FULLSCREEN)
                #cv2.setWindowProperty("AIML",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
                ctypes.windll.user32.SystemParametersInfoW(20,6,posters+"\\quiz.jpg", 0) 
         #speak("Background changed succesfully")
            elif event=="Debate":
                #import ctypes
                #img = cv2.imread('debateposter.jpg')
                #thread.start_new_thread( dispimage, ("Thread-1", img, ) )
                ctypes.windll.user32.SystemParametersInfoW(20,6,posters+"\\debate.jpg", 0)
        #speak("Background changed succesfully")
            elif event=="Poster Making":
                #import ctypes
                #img = cv2.imread('debateposter.jpg')
                #thread.start_new_thread( dispimage, ("Thread-1", img, ) )
                ctypes.windll.user32.SystemParametersInfoW(20,6,posters+"\\poster making.jpg", 0) 
        #speak("Background changed succesfully")
            elif event=="Minute to WIN It":
                #import ctypes
                #img = cv2.imread('debateposter.jpg')
                #thread.start_new_thread( dispimage, ("Thread-1", img, ) )
                ctypes.windll.user32.SystemParametersInfoW(20,6,posters+"\\Minute to win it.jpg", 0)
        #speak("Background changed succesfully")
            elif event=="Carrom":
                #import ctypes
                #img = cv2.imread('debateposter.jpg')
                #thread.start_new_thread( dispimage, ("Thread-1", img, ) )
                ctypes.windll.user32.SystemParametersInfoW(20,6,posters+"\\carrom.jpg", 0)
        #speak("Background changed succesfully")
            elif event=="Chess":
                #import ctypes
                #img = cv2.imread('debateposter.jpg')
                #thread.start_new_thread( dispimage, ("Thread-1", img, ) )
                ctypes.windll.user32.SystemParametersInfoW(20,6,posters+"\\chess poster.png", 0)
        #speak("Background changed succesfully")
            elif event=="Treasure-Hunt":
                #import ctypes
                #img = cv2.imread('debateposter.jpg')
                #thread.start_new_thread( dispimage, ("Thread-1", img, ) )
                ctypes.windll.user32.SystemParametersInfoW(20,6,posters+"\\TreasureHunt.jpeg", 0)
        #speak("Background changed succesfully")
    
            elif event=="Badminton Men":
                #import ctypes
                #img = cv2.imread('debateposter.jpg')
                #thread.start_new_thread( dispimage, ("Thread-1", img, ) )
                ctypes.windll.user32.SystemParametersInfoW(20,0,posters+"\\badminton mens.jpg", 0)
        #speak("Background changed succesfully")
            elif event=="Badminton Women":
                #import ctypes
                #img = cv2.imread('debateposter.jpg')
                #thread.start_new_thread( dispimage, ("Thread-1", img, ) )
                ctypes.windll.user32.SystemParametersInfoW(20,6,posters+"\\badminton womens.jpg", 0)
        #speak("Background changed succesfully")
            elif event=="Table Tennis":
                #import ctypes
                #img = cv2.imread('debateposter.jpg')
                #thread.start_new_thread( dispimage, ("Thread-1", img, ) )
                ctypes.windll.user32.SystemParametersInfoW(20,6,posters+"\\table tennis.jpg", 0)
        #speak("Background changed succesfully")
            elif event=="Harmony Music Gala":
                #import ctypes
                #img = cv2.imread('debateposter.jpg')
                #thread.start_new_thread( dispimage, ("Thread-1", img, ) )
                ctypes.windll.user32.SystemParametersInfoW(20,6,posters+"\\musical day.jpg", 0)
        #speak("Background changed succesfully")
            elif event=="Mehendi":
                #import ctypes
                #img = cv2.imread('debateposter.jpg')
                #thread.start_new_thread( dispimage, ("Thread-1", img, ) )
                ctypes.windll.user32.SystemParametersInfoW(20,6,posters+"\\Mehendi.jpg", 0)
        #speak("Background changed succesfully")
            elif event=="Pencil Sketch":
                #import ctypes
                #img = cv2.imread('debateposter.jpg')
                #thread.start_new_thread( dispimage, ("Thread-1", img, ) )
                ctypes.windll.user32.SystemParametersInfoW(20,6,posters+"\\pencil sketch.png", 0)
        #speak("Background changed succesfully")
            elif event=="Ragging Quiz Fourth Sem":
                #import ctypes
                #img = cv2.imread('debateposter.jpg')
                #thread.start_new_thread( dispimage, ("Thread-1", img, ) )
                ctypes.windll.user32.SystemParametersInfoW(20,6,posters+"\\qiuz.jpg", 0)
        #speak("Background changed succesfully")
            elif event=="Ragging Quiz Second Sem":
                #import ctypes
                #img = cv2.imread('debateposter.jpg')
                #thread.start_new_thread( dispimage, ("Thread-1", img, ) )
                ctypes.windll.user32.SystemParametersInfoW(20,6,posters+"\\qiuz.jpg", 0)
        #speak("Background changed succesfully")
            elif event=="Ragging-Story":
                #import ctypes
                #img = cv2.imread('debateposter.jpg')
                #thread.start_new_thread( dispimage, ("Thread-1", img, ) )
                ctypes.windll.user32.SystemParametersInfoW(20,6,posters+"\\stroy.jpg", 0)
        #speak("Background changed succesfully")
            elif event=="Ragging-Essay":
                #import ctypes
                #img = cv2.imread('debateposter.jpg')
                #thread.start_new_thread( dispimage, ("Thread-1", img, ) )
                ctypes.windll.user32.SystemParametersInfoW(20,6,posters+"\\essay.jpg", 0)
        #speak("Background changed succesfully")
            elif event=="Ragging-Slogans":
                #import ctypes
                #img = cv2.imread('debateposter.jpg')
                #thread.start_new_thread( dispimage, ("Thread-1", img, ) )
                ctypes.windll.user32.SystemParametersInfoW(20,6,posters+"\\slogan.jpg", 0)
            cmd=arr[0]
            language = 'en'
            mobj = gTTS(text=cmd, lang=language, slow=False)
            mobj.save("aicmd.mp3")
            # audio = AudioSegment.from_mp3("aicmd.mp3")
        
            # audio.speedup(playback_speed=12.0) # speed up by 2x
                
            # # export to mp3
            # audio.export("aicmd.mp3", format="mp3")

            s.call(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe ', '-Incurse  ','aicmd.mp3', 'vlc://quit'])
    except Exception as error:
        print(error)


        

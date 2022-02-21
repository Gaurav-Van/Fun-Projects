import os
import subprocess as sp
from cv2 import cv2
cv = cv2

paths = {'Notepad': 'C:\\WINDOWS\\system32\\notepad.exe',
         'Teams': 'C:\\Users\\Asus\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"',
         'Brave': 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk',
         'Youtube': 'C:\\Users\\Asus\\Desktop\\YouTube.lnk',
         'Discord': 'C:\\Users\\Asus\\AppData\\Local\\Discord\\app-1.0.9004\\Discord.exe',
         'Spotify': 'C:\\Users\\Asus\\AppData\\Roaming\\Spotify\\Spotify.exe',
         'Whatsapp': 'C:\\Users\\Asus\\AppData\\Local\\WhatsApp\\WhatsApp.exe',
         }


def open_camera():
    capture = cv.VideoCapture(0)
    while True:
        isTrue, frame = capture.read()
        cv.imshow('WEBCAM', frame)
        if cv.waitKey(1) & 0xFF == ord('w'):
            break
    capture.release()
    cv.destroyAllWindows()


def open_Notepad():
    os.startfile(paths['Notepad'])


def open_Teams():
    os.startfile(paths['Teams'])


def open_Brave():
    os.startfile(paths['Brave'])


def open_Youtube():
    os.startfile(paths['Youtube'])


def open_Discord():
    os.startfile(paths['Discord'])


def open_Spotify():
    os.startfile(paths['Spotify'])


def open_Whatsapp():
    os.startfile(paths['Whatsapp'])


def open_cmd():
    os.system('start cmd')



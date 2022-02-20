import os
import subprocess as sp

paths = {'Notepad': '%windir%\\system32\\notepad.exe',
         'Teams': 'C:\\Users\\Asus\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart "Teams.exe"',
         'Brave': 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk',
         'Youtube': '"C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\chrome_proxy.exe" '
                    ' --profile-directory=Default --app-id=agimnkijcaahngcdmfeangaknmldooml',
         'Discord': 'C:\\Users\\Asus\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe',
         'Spotify': 'C:\\Users\\Asus\\AppData\\Roaming\\Spotify\\Spotify.exe',
         'Whatsapp': 'C:\\Users\\Asus\\AppData\\Local\\WhatsApp\\WhatsApp.exe',
         }


def open_camera():
    sp.run('start microsoft.windows.camera', shell=True)


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



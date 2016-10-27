import telebot
import os
import sys
import random
import logging
import time

bot = telebot.TeleBot(os.environ["tu_mae_token"])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "/tumae")

@bot.message_handler(commands=['stop'])
def stopBot(message):
	try:
		bot.reply_to(message, "Vale vale, lo paro")
		return 0
	except:
		logFile=open('file.log','a') #Abro el fichero log, si no esta lo crea, si esta escribe a continuacion
		print(sys.exc_info())
		logFile.write("\n"+time.strftime("%c")+"--> "+sys.exc_info())
		logFile.close()

def recibe(messages):
	try:
		for m in messages:
			if m.chat.type == 'group' or m.chat.type == 'supergroup':
				ran_ = random.randint(1, 9)

				if ran_ < 3:
					if m.from_user.username == 'SRMarin':
						bot.send_message(m.chat.id, 'Comprate un cuello sirolo')
					elif m.from_user.username == 'Raulytaso':
						bot.send_message(m.chat.id, 'Subete los pantalones mierda')
					elif m.from_user.username == 'McMayXIII':
						bot.send_message(m.chat.id, 'Porreroooo')

				ran = random.randint(1,20)

				if m.content_type == 'text':
					if 'quien' in m.text or 'Quien' in m.text:
						if(ran==1):
							bot.send_message(m.chat.id, '/lamaedelsergio')
						else:
							bot.send_message(m.chat.id, '/tumae')
					if 'cafeto' in m.text:
						if(ran==1):
							bot.send_message(m.chat.id, '/lamaedelsergio')
						else:
							bot.send_message(m.chat.id, '/tumae')
					if 'cafeteria' in m.text:
						if(ran==1):
							bot.send_message(m.chat.id, '/lamaedelsergio')
						else:
							bot.send_message(m.chat.id, '/tumae')
	#            if m.content_type == 'text':
	#               if '/spam' in m.text:
	#                   for i in range (0, 10):
	#                        bot.send_message(m.chat.id, '/spam')

				ran = random.randint(1,200)
				if ran==2 :
					import urllib
					ran2 = random.randint(1, 2)
					f = open('1.jpg', 'wb')
					if ran2==1 :
						string='http://cageme.herokuapp.com/500/500'

					if ran2==2 :
						string='http://cageme.herokuapp.com/g/500/500'

					# if ran2==3 :
					#    string='https://www.placecage.com/c/'

					f.write(urllib.urlopen(string).read())

					f.close()

					photo = open('1.jpg', 'rb')
					bot.send_photo(m.chat.id,photo)

			else:
				bot.send_message(m.chat.id, "tus muertos siroloooooooo")
	except Exception, ex:
		logFile=open('file.log','a') #Abro el fichero log, si no esta lo crea, si esta escribe a continuacion
		logFile.write("\n"+time.strftime("%c")+" "+str(sys.exc_info()))
		logFile.close()

bot.set_update_listener(recibe)
bot.polling(none_stop=False)

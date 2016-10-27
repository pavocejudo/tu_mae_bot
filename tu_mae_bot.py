import telebot
import os
import random
import logging

bot = telebot.TeleBot(os.environ["tu_mae_token"])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "/tumae")

def recibe(messages):
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
                elif m.from_user.username == 'MikeHendrix':
                    bot.send_message(m.chat.id, 'Calla drogadictooo')

            rand = random.randint(1,20)

            message=' '

            if m.content_type == 'text':
                Msgs=['/tumae', '/lamaedelsergio', '/paQueQuieresSaberEsoJaJaSaludos', '/elCuellodelSegio']
                #eliminamos if innecesarios

                if 'quien' in m.text or 'Quien' in m.text:
                    bot.send_message(m.chat.id, Msgs[random.randint(0,3)])
                elif 'cafeto' in m.text:
                    bot.send_message(m.chat.id, Msgs[random.randint(0,3)])
                elif 'cafeteria' in m.text:
                    bot.send_message(m.chat.id, Msgs[random.randint(0,3)])
                elif 'alguien en' in m.text:
                    bot.send_message(m.chat.id, Msgs[random.randint(0,3)])
#            if m.content_type == 'text':
#               if '/spam' in m.text:
#                   for i in range (0, 10):
#                        bot.send_message(m.chat.id, '/spam')

            ran = random.randint(1,1000)
            """ le damos un 5% de probabilidad de que pase"""
            if ran <= 5 :
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

bot.set_update_listener(recibe)
bot.polling(none_stop=False)

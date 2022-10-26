from email import message
from re import I
import telebot
import random

bot = telebot.TeleBot("5626480043:AAHeFnkH1akTtsh_nqGx-YvA6MS9IT3eqxA", parse_mode=None)

a = 100
c = 0

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	global a
	global c
	if a > 0:
		bot.send_message(message.chat.id,str(a - int(message.text))+': Candies left')
		a = a - int(message.text)
		c = 0
	if a <=0  and c == 0:
		bot.send_message(message.chat.id, 'You won')
	if a > 28:
		b = random.randint(1, 28)
		bot.send_message(message.chat.id, f'Bot took {b} candies. {str(a - b)}: Candies left')
		a = a - b
		c = 1
	if 0 < a < 28:
		b = random.randint(1, a)
		bot.send_message(message.chat.id, f'Bot took {b} candies. {str(a - b)}: Candies left')
		a = a - b
		c = 1
	if a == 0 and c == 1:
		bot.send_message(message.chat.id, 'Bot won')


bot.infinity_polling()
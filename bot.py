import telebot
from telebot import types

bot = telebot.TeleBot("6978784825:AAElNJtSZHoV0OLHJREebRSguM8q8b2HbIk", parse_mode=None)
#user = bot.get_me()

@bot.message_handler(commands=["start"])
def send_welcome(message):	
	welcome_message = "Welcome! This bot was developed by M.V. Kapustin as a pet project."
	bot.send_message(message.chat.id, welcome_message)
	markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
	who_btn = types.KeyboardButton("1. Who is M.V. Kapustin?")
	when_btn = types.KeyboardButton("2. When was this bot developed?")
	why_btn = types.KeyboardButton("3. Why was this bot developed?")
	
	markup.add(who_btn, when_btn, why_btn)
	bot.send_message(message.chat.id, "Choose one:", reply_markup=markup)
	
@bot.message_handler(commands=["help"])
def send_welcome(message):	
	help_message = "... help message ... "
	bot.send_message(message.chat.id, help_message)
	
@bot.message_handler(content_types=["text"])
def send_welcome(message):	
	if message.text == "1. Who is M.V. Kapustin?":
		bot.send_message(message.chat.id, "M.V. Kapustin is ...")
	elif message.text == "2. When was this bot developed?":
		bot.send_message(message.chat.id, "This bot was developed at 14:44 08.12.2023 :)")
	elif message.text == "3. Why was this bot developed?":
		bot.send_message(message.chat.id, "This bot was developed due to ...")
	else:
		bot.send_message(message.chat.id, "Sorry i don't understand this message. Try to use buttons or /help")

bot.infinity_polling()
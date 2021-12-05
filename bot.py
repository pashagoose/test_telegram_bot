import telebot
import os
import random

PICTURES_COUNT = 10

token = os.environ['TELEGRAM_BOT_TOKEN']

bot = telebot.TeleBot(token, parse_mode=None)
random.seed(42)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Audi, how are you doing?")

@bot.message_handler(commands=['quote'])
def send_meme(message):
	picture_id = random.randint(1, PICTURES_COUNT)

	picture = open("./memes/{}.jpg".format(picture_id), "rb")
	bot.send_photo(message.chat.id, picture)

bot.infinity_polling()

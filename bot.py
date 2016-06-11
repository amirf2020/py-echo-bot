import telebot
from telebot import types
token = 226346511
bot = telebot.TeleBot(226346511)
	
f = "Bot Firstname: {}".format(bot.get_me().first_name)
u = "\nBot username: {}".format(bot.get_me().username)
i = "\nBot ID: {}".format(bot.get_me().id)
c = "\n\nThank you for using this source :) \n                 \e[41m@Mrhalix"
print(f + u + i + c)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	markup = types.InlineKeyboardMarkup()
	itembtna = types.InlineKeyboardButton('Bot Source',url='http://github.com/mrhalix/py-echo-bot')
	markup.row(itembtna)
    	bot.reply_to(message, "*Hi* i'm a `echo bot` written in [Python](http://python.org) language",reply_markup=markup,parse_mode='markdown',disable_web_page_preview=True)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()

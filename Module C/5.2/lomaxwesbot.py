import telebot

bot = telebot.TeleBot('5629502171:AAHZDndUNBMT2ygrzZzk0T9Qz1QiO1nykWk')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, {message.chat.username}")

@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

@bot.message_handler(content_types=['voice', ])
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Какой противный у тебя голосок!')

bot.polling(none_stop=True)


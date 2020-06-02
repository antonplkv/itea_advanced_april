from telebot import TeleBot

bot = TeleBot("1265290766:AAGdW71kUxAvg3aZzhN_5s4DusJfCSsvsYs")


@bot.message_handler(commands=['start'])
def hello(message):
    print(message)
    bot.send_message(message.chat.id, 'Здравствуй!')


@bot.message_handler(content_types=['text'])
def hello(message):
    bot.send_message(message.chat.id, message.text[::-1])



bot.polling()
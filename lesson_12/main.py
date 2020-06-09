from telebot import TeleBot
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
import random
from config import TOKEN


bot = TeleBot(TOKEN)

GREETINGS = ('hello', 'привет', 'hi', 'salut')

PRODUCTS_DB = {
    'tomato': 'Fresh tomato',
    'cucumber': 'Green fresh cuccumber'
}


def is_greetings(message):
    try:
        result = message.text.lower().strip() in GREETINGS
    except AttributeError:
        result = False
    return result


@bot.message_handler(commands=['start'])
def start(message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text=random.choice(GREETINGS).capitalize(), request_contact=True)

    kb.add(button)
    bot.send_message(message.chat.id, 'Нажмите на кнопку', reply_markup=kb)


@bot.message_handler(commands=['inline'])
def products_inline(message):
    kb = InlineKeyboardMarkup()
    buttons = [InlineKeyboardButton(k, callback_data=f'product_{k}') for k in PRODUCTS_DB.keys()]

    kb.add(*buttons)

    bot.send_message(message.chat.id, 'Выберите продукт', reply_markup=kb)


@bot.callback_query_handler(func=lambda call: call.data.startswith('product_'))
def my_query(call):
    bot.send_message(call.from_user.id, PRODUCTS_DB[call.data.split('_')[1]])


@bot.message_handler(func=is_greetings)
def greetings(message):
    bot.send_message(message.chat.id, random.choice(GREETINGS).capitalize())


@bot.message_handler(content_types=['text'])
def any_text(message):
    print(message)
    bot.send_message(message.chat.id, message.text[::-1])


if __name__ == '__main__':
    bot.polling()

from mongoengine import SequenceField

SequenceField
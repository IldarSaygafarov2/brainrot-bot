from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def show_start_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton(text='Начать'))
    return kb
    
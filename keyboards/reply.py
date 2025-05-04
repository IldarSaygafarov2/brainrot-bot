from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def show_start_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(
        KeyboardButton(text="Библиотека"),
        KeyboardButton(text="Отгадать"),
    )
    return kb

from telebot import types

from data.loader import bot
from keyboards.inline import (
    show_library_first_chars_menu,
    show_first_char_memes_menu,
    show_start_menu_inline,
    return_to_callback_menu,
)
from utils._json import read_json
from utils.helpers import find_object_by_key

data = read_json("brainrot_data.json")


@bot.message_handler(commands=["start"])
def handle_command_start(message: types.Message):
    chat_id = message.from_user.id

    bot.send_message(
        chat_id,
        "Вас приветствует бот Italian Brainrot, нажмите на кнопку ниже чтобы начать",
        reply_markup=show_start_menu_inline(),
    )


@bot.callback_query_handler(func=lambda call: call.data == "return_home")
def handle_return_home(call: types.CallbackQuery):
    chat_id = call.message.chat.id

    bot.edit_message_text(
        "Вас приветствует бот Italian Brainrot, нажмите на кнопку ниже чтобы начать",
        chat_id,
        message_id=call.message.id,
        reply_markup=show_start_menu_inline(),
    )


@bot.callback_query_handler(func=lambda call: call.data == "show_library")
def show_memes_library(call: types.CallbackQuery):
    chat_id = call.message.chat.id

    # chat_id = message.from_user.id

    bot.edit_message_text(
        "Выберите один из пунктов ниже",
        chat_id=chat_id,
        message_id=call.message.id,
        reply_markup=show_library_first_chars_menu(
            data, chat_id, callback="return_home"
        ),
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith("first_char"))
def get_first_char_memes(call: types.CallbackQuery):
    _, first_char, chat_id = call.data.split(":")

    if call.message.text:
        bot.edit_message_text(
            "Выберите один из пунктов ниже",
            chat_id,
            message_id=call.message.id,
            reply_markup=show_first_char_memes_menu(
                data, first_char, callback="show_library"
            ),
        )
    if call.message.photo:
        bot.delete_message(chat_id=chat_id, message_id=call.message.id)
        bot.send_message(
            chat_id,
            "Выберите один из пунктов ниже",
            reply_markup=show_first_char_memes_menu(
                data, first_char, callback="show_library"
            ),
        )


@bot.callback_query_handler(func=lambda call: call.data.startswith("detail"))
def get_meme_detail(call: types.CallbackQuery):
    _, meme_name, first_char = call.data.split(":")
    item = find_object_by_key(data, first_char, meme_name)

    chat_id = call.message.chat.id

    image_link = item["image_link"]
    name = item["name"]

    if not image_link:
        bot.delete_message(chat_id=chat_id, message_id=call.message.id)
        bot.send_message(
            chat_id,
            name,
            reply_markup=return_to_callback_menu(f"first_char:{first_char}:{chat_id}"),
        )
    else:
        bot.delete_message(chat_id=chat_id, message_id=call.message.id)
        bot.send_photo(
            chat_id,
            caption=name,
            photo=image_link,
            reply_markup=return_to_callback_menu(f"first_char:{first_char}:{chat_id}"),
        )

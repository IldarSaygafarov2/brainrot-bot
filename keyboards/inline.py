from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def show_start_menu_inline():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.row(
        InlineKeyboardButton(text="Библиотека", callback_data="show_library"),
        InlineKeyboardButton(text="Отгадать", callback_data="start_game"),
    )
    return kb


def show_library_first_chars_menu(data, chat_id: int, callback: str = ""):
    kb = InlineKeyboardMarkup(row_width=3)
    buttons = []
    for first_char in data.keys():
        buttons.append(
            InlineKeyboardButton(
                text=first_char, callback_data=f"first_char:{first_char}:{chat_id}"
            )
        )
    kb.add(*buttons)
    if callback:
        kb.row(InlineKeyboardButton(text="Назад", callback_data=callback))
    return kb


def show_first_char_memes_menu(data, first_char: str, callback: str = ""):
    first_char_items = data.get(first_char)

    kb = InlineKeyboardMarkup(row_width=2)
    buttons = []

    for item in first_char_items:
        buttons.append(
            InlineKeyboardButton(
                text=item["name"],
                callback_data=f'detail:{item["name"]}:{first_char}',
            )
        )

    kb.add(*buttons)
    if callback:
        kb.row(InlineKeyboardButton(text="Назад", callback_data=callback))
    return kb


def return_to_callback_menu(callback: str):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text="Назад", callback_data=callback))
    return kb

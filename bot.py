import os
from dotenv import load_dotenv
from telebot import TeleBot, types
from keyboards import show_start_menu
load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

bot = TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def handle_command_start(message: types.Message):
    chat_id = message.from_user.id

    bot.send_message(chat_id, 'Вас приветствует бот Italian Brainrot, нажмите на кнопку ниже чтобы начать',
                     reply_markup=show_start_menu())


if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)

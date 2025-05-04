import os

from dotenv import load_dotenv
from telebot import TeleBot

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = TeleBot(token=TOKEN)

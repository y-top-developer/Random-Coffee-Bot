import telebot
import logging

from settings import TELEGRAM_TOKEN

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode='markdown')


bot.infinity_polling()

import telebot
import logging

from settings import TELEGRAM_TOKEN, LANGUAGES
from frontend.admin_settings import get_admin_settings_menu, ask_company_name, get_admin_companies_menu


logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode='markdown')


@bot.message_handler(commands=['get_admin_settings_menu'])
def get_admin_settings_menu_main(message):
    user_id = message.from_user.id

    get_admin_settings_menu(bot, 'en', user_id)


@bot.message_handler(commands=['get_admin_companies_menu'])
def get_admin_companies_menu_handler(message):
    user_id = message.from_user.id

    from dotmap import DotMap
    company = DotMap()
    company.name = 'My Company'
    company.id = '123'
    companies = [company]

    get_admin_companies_menu(bot, 'en', user_id, companies)


@bot.message_handler(commands=['ask_company_name'])
def ask_company_name_main(message):
    user_id = message.from_user.id

    ask_company_name(bot, 'en', user_id)


bot.infinity_polling()

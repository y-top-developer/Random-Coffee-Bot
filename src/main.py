import telebot
import logging

from settings import TELEGRAM_TOKEN, LANGUAGES
from frontend.user_settings import (ask_language, ask_password, ask_name, ask_link, get_user_settings_menu,
                                    get_user_profile, get_user_change_profile_menu, get_user_companies_menu, ask_mode_menu, get_user_status)

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode='markdown')


@bot.message_handler(commands=['ask_language'])
def ask_language_main(message):
    user_id = message.from_user.id

    language_code = message.from_user.language_code
    if language_code not in LANGUAGES:
        language_code = 'en'

    ask_language(bot, language_code, user_id)


@bot.message_handler(commands=['ask_password'])
def ask_password_handler(message):
    user_id = message.from_user.id
    ask_password(bot, 'en', user_id)


@bot.message_handler(commands=['ask_name'])
def ask_name_handler(message):
    user_id = message.from_user.id
    ask_name(bot, 'en', user_id)


@bot.message_handler(commands=['ask_link'])
def ask_link_handler(message):
    user_id = message.from_user.id
    ask_link(bot, 'en', user_id)


@bot.message_handler(commands=['get_user_settings_menu'])
def get_user_settings_menu_handler(message):
    user_id = message.from_user.id
    get_user_settings_menu(bot, 'en', user_id)


@bot.message_handler(commands=['get_user_profile'])
def get_user_profile_handler(message):
    user_id = message.from_user.id
    get_user_profile(bot, 'en', user_id, 'USER PROFILE EXAMPLE')


@bot.message_handler(commands=['get_user_change_profile_menu'])
def get_user_change_profile_menu_handler(message):
    user_id = message.from_user.id
    get_user_change_profile_menu(bot, 'en', user_id)


@bot.message_handler(commands=['get_user_companies_menu'])
def get_user_companies_menu_handler(message):
    user_id = message.from_user.id

    from dotmap import DotMap
    company = DotMap()
    company.name = 'My Company'
    company.id = '123'
    companies = [company]

    get_user_companies_menu(bot, 'en', user_id, companies)


@bot.message_handler(commands=['ask_mode_menu'])
def ask_mode_menu_handler(message):
    user_id = message.from_user.id

    from dotmap import DotMap
    company = DotMap()
    company.id = '123'

    ask_mode_menu(bot, 'en', user_id, company)


@bot.message_handler(commands=['get_user_status'])
def get_user_status_handler(message):
    user_id = message.from_user.id

    get_user_status(bot, 'en', user_id, 'company#1 - run - Anton')


bot.infinity_polling()

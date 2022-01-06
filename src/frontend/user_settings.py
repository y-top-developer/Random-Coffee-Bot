from telebot import types

from settings import LANGUAGES
from frontend.text import (ASK_LANGUAGE, ASK_PASSWORD, ASK_NAME, ASK_LINK, SHOW_PROFILE, CHANGE_PROFILE,
                           MY_COMPANIES, SET_RUN, SET_PAUSE, SETTINGS, BACK,
                           ASK_WHAT_CHANGE_IN_PROFILE, MY_NAME, MY_LINK, STATUS, WORK, ABOUT, LANGUAGE,
                           CONGRATULATIONS_WITH_SUCCESS_INITIALIZATION, USER_PROFILE_FORMAT)


def ask_language(bot, language_code, user_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row_width = 2

    keyboard.add(
        *[types.InlineKeyboardButton(
            text=language,
            callback_data=f'user_language_code_{language}'
        ) for language in LANGUAGES]
    )

    bot.send_message(
        user_id, ASK_LANGUAGE[language_code], reply_markup=keyboard)


def ask_password(bot, language_code, user_id):
    bot.send_message(user_id, ASK_PASSWORD[language_code])


def ask_name(bot, language_code, user_id):
    bot.send_message(user_id, ASK_NAME[language_code])


def ask_link(bot, language_code, user_id):
    bot.send_message(user_id, ASK_LINK[language_code])


def success_initialization(bot, language_code, user_id):
    bot.send_message(
        user_id, CONGRATULATIONS_WITH_SUCCESS_INITIALIZATION[language_code])


def get_user_settings_menu(bot, language_code, user_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row_width = 1

    keyboard.add(
        types.InlineKeyboardButton(
            text=SHOW_PROFILE[language_code],
            callback_data='user_show_profile'
        ),
        types.InlineKeyboardButton(
            text=CHANGE_PROFILE[language_code],
            callback_data='user_change_profile'
        ),
        types.InlineKeyboardButton(
            text=MY_COMPANIES[language_code],
            callback_data='user_my_companies'
        ),
        types.InlineKeyboardButton(
            text=STATUS[language_code],
            callback_data='user_status'
        ),
        types.InlineKeyboardButton(
            text=BACK[language_code],
            callback_data='user_back'
        ),
    )

    bot.send_message(
        user_id, SETTINGS[language_code], reply_markup=keyboard)


def get_user_profile(bot, language_code, user_id, user):

    user_profile = USER_PROFILE_FORMAT[language_code].format(
        name=user.name,
        link=user.link,
        work=user.work,
        about=user.about
    )

    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(
        types.InlineKeyboardButton(
            text=BACK[language_code],
            callback_data='user_back_get_user_profile'
        )
    )

    bot.send_message(user_id, user_profile, reply_markup=keyboard)


def get_user_change_profile_menu(bot, language_code, user_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row_width = 1

    keyboard.add(
        types.InlineKeyboardButton(
            text=MY_NAME[language_code],
            callback_data='user_change_name'
        ),
        types.InlineKeyboardButton(
            text=MY_LINK[language_code],
            callback_data='user_change_link'
        ),
        types.InlineKeyboardButton(
            text=WORK[language_code],
            callback_data='user_change_work'
        ),
        types.InlineKeyboardButton(
            text=ABOUT[language_code],
            callback_data='user_change_about'
        ),
        types.InlineKeyboardButton(
            text=LANGUAGE[language_code],
            callback_data='user_change_language'
        ),
        types.InlineKeyboardButton(
            text=BACK[language_code],
            callback_data='user_back_get_user_change_profile_menu'
        )
    )
    bot.send_message(
        user_id, ASK_WHAT_CHANGE_IN_PROFILE[language_code], reply_markup=keyboard)


def get_user_companies_menu(bot, language_code, user_id, companies):
    keyboard = types.InlineKeyboardMarkup()

    for company in companies:
        keyboard.add(
            types.InlineKeyboardButton(
                text=company.name,
                callback_data=f'user_company_{company.id}'
            )
        )

    keyboard.add(
        types.InlineKeyboardButton(
            text=BACK[language_code],
            callback_data='user_back'
        )
    )
    bot.send_message(
        user_id, MY_COMPANIES[language_code], reply_markup=keyboard)


def ask_mode_menu(bot, language_code, user_id, company):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row_width = 1

    keyboard.add(
        types.InlineKeyboardButton(
            text=SET_RUN[language_code],
            callback_data=f'user_set_run_{company.id}'
        ),
        types.InlineKeyboardButton(
            text=SET_PAUSE[language_code],
            callback_data=f'user_set_pause_{company.id}'
        ),
        types.InlineKeyboardButton(
            text=BACK[language_code],
            callback_data='user_back'
        )
    )

    bot.send_message(
        user_id, MY_COMPANIES[language_code], reply_markup=keyboard)


def get_user_status(bot, language_code, user_id, status_message):
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(
        types.InlineKeyboardButton(
            text=BACK[language_code],
            callback_data='user_back'
        )
    )

    bot.send_message(user_id, status_message, reply_markup=keyboard)

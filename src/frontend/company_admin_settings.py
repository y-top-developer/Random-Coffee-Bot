from telebot import types

from frontend.text import (SET_PAUSE, SET_RUN, SHOW_PROFILE, USERS, USER_SETTINGS, BACK, SETTINGS,
                  PAIRS, GENERATE_PAIRS, SEND_INVITES, GET_PASSWORD, GENERATE_PASSWORD, ASK_WHICH_USER_CHOOSE, BLOCK,
                  YES, NO, ARE_YOU_SURE, DONE)


def get_company_admin_user_settings_menu(bot, language_code, user_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row_width = 1

    keyboard.add(
        types.InlineKeyboardButton(
            text=SHOW_PROFILE[language_code],
            callback_data='company_admin_show_profile'
        ),
        types.InlineKeyboardButton(
            text=BLOCK[language_code],
            callback_data='company_admin_block'
        ),
        types.InlineKeyboardButton(
            text=SET_RUN[language_code],
            callback_data='company_admin_set_run'
        ),
        types.InlineKeyboardButton(
            text=SET_PAUSE[language_code],
            callback_data='company_admin_set_pause'
        ),
        types.InlineKeyboardButton(
            text=BACK[language_code],
            callback_data='company_admin_back'
        )
    )

    bot.send_message(
        user_id, SETTINGS[language_code], reply_markup=keyboard)


def ask_which_user_choose(bot, language_code, user_id):
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(
        types.InlineKeyboardButton(
            text=BACK[language_code],
            callback_data='company_admin_back'
        )
    )

    bot.send_message(
        user_id, ASK_WHICH_USER_CHOOSE[language_code], reply_markup=keyboard)


def ask_are_you_sure(bot, language_code, user_id):
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(
        types.InlineKeyboardButton(
            text=YES[language_code],
            callback_data='company_admin_yes'
        ),
        types.InlineKeyboardButton(
            text=NO[language_code],
            callback_data='company_admin_no'
        )
    )

    bot.send_message(
        user_id, ARE_YOU_SURE[language_code], reply_markup=keyboard)


def done(bot, language_code, user_id):
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(
        types.InlineKeyboardButton(
            text=BACK[language_code],
            callback_data='company_admin_back'
        )
    )

    bot.send_message(
        user_id, DONE[language_code], reply_markup=keyboard)


def show_users(bot, language_code, user_id, users_message):
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(
        types.InlineKeyboardButton(
            text=BACK[language_code],
            callback_data='company_admin_back'
        )
    )

    bot.send_message(user_id, users_message, reply_markup=keyboard)


def get_company_admin_settings_menu(bot, language_code, user_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row_width = 1

    keyboard.add(
        types.InlineKeyboardButton(
            text=USERS[language_code],
            callback_data='company_admin_users'
        ),
        types.InlineKeyboardButton(
            text=USER_SETTINGS[language_code],
            callback_data='company_admin_user_settings'
        ),
        types.InlineKeyboardButton(
            text=PAIRS[language_code],
            callback_data='company_admin_pairs'
        ),
        types.InlineKeyboardButton(
            text=GENERATE_PAIRS[language_code],
            callback_data='company_admin_generate_pairs'
        ),
        types.InlineKeyboardButton(
            text=SEND_INVITES[language_code],
            callback_data='company_admin_send_invites'
        ),
        types.InlineKeyboardButton(
            text=GET_PASSWORD[language_code],
            callback_data='company_admin_get_password'
        ),
        types.InlineKeyboardButton(
            text=GENERATE_PASSWORD[language_code],
            callback_data='company_admin_generate_password'
        ),
        types.InlineKeyboardButton(
            text=BACK[language_code],
            callback_data='company_admin_back'
        )
    )

    bot.send_message(
        user_id, SETTINGS[language_code], reply_markup=keyboard)


def get_user_profile(bot, language_code, user_id, user_profile):
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(
        types.InlineKeyboardButton(
            text=BACK[language_code],
            callback_data='company_admin_back'
        )
    )

    bot.send_message(user_id, user_profile, reply_markup=keyboard)

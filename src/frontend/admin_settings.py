from telebot import types

from frontend.text import (CREATE_COMPANY, SET_COMPANY_ADMIN, BACK, SETTINGS,
                  ASK_COMPANY_NAME, ASK_WHO_WILL_BE_COMPANY_ADMIN, MY_COMPANIES)


def get_admin_companies_menu(bot, language_code, user_id, companies):
    keyboard = types.InlineKeyboardMarkup()

    for company in companies:
        keyboard.add(
            types.InlineKeyboardButton(
                text=company.name,
                callback_data=f'admin_company_{company.id}'
            )
        )

    keyboard.add(
        types.InlineKeyboardButton(
            text=BACK[language_code],
            callback_data='admin_back'
        )
    )
    bot.send_message(
        user_id, MY_COMPANIES[language_code], reply_markup=keyboard)


def ask_company_name(bot, language_code, user_id):
    bot.send_message(user_id, ASK_COMPANY_NAME[language_code])


def ask_who_will_be_company_admin(bot, language_code, user_id):
    bot.send_message(user_id, ASK_WHO_WILL_BE_COMPANY_ADMIN[language_code])


def get_admin_settings_menu(bot, language_code, user_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row_width = 1

    keyboard.add(
        types.InlineKeyboardButton(
            text=CREATE_COMPANY[language_code],
            callback_data='admin_create_company'
        ),
        types.InlineKeyboardButton(
            text=SET_COMPANY_ADMIN[language_code],
            callback_data='admin_set_company_admin'
        ),
        types.InlineKeyboardButton(
            text=BACK[language_code],
            callback_data='admin_back'
        ),
    )

    bot.send_message(
        user_id, SETTINGS[language_code], reply_markup=keyboard)

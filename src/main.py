import telebot
import logging

from backend.orm import (
    get_user,
    set_user,
    set_user_field,
    get_company_by_password
)

from frontend.user_settings import (
    ask_language,
    ask_link,
    ask_password,
    ask_name,
    success_initialization,
    get_user_settings_menu,
    success_initialization,
    get_user_profile,
    get_user_change_profile_menu
)
from frontend.general import (
    replace_keyboard_on_choosen_option,
)

from settings import TELEGRAM_TOKEN, LANGUAGES, ADMIN


# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode='markdown')

# Initialization


class InitializationStates:
    get_password = 1
    get_name = 2
    get_link = 3
    complete = 4

# Initialization ask language


@bot.message_handler(commands=['start'])
def ask_language_handler(message):
    user_id = message.from_user.id

    user = get_user(user_id)
    if not user or not user.is_verified:
        set_user(user_id)
        language_code = message.from_user.language_code
        if language_code not in LANGUAGES:
            language_code = 'en'

        ask_language(bot, language_code, user_id)
    else:
        user = get_user(user_id)
        language_code = user.language_code
        get_user_settings_menu(bot, language_code, user_id)
        bot.set_state(user_id, InitializationStates.complete)


@bot.callback_query_handler(func=lambda call: call.data.startswith('user_language_code_'))
def ask_language_callback(call):
    user_id = call.message.chat.id
    message_id = call.message.message_id
    username = call.from_user.username
    next_state = InitializationStates.get_password

    message_text = call.message.text
    language_code = call.data[len('user_language_code_'):]

    replace_keyboard_on_choosen_option(
        bot, language_code, user_id, message_id, message_text, language_code)

    set_user_field(user_id, 'language_code', language_code)
    user = get_user(user_id)
    language_code = user.language_code
    if username == ADMIN:
        next_state = InitializationStates.get_name
        set_user_field(user_id, 'is_verified', True)
        ask_name(bot, language_code, user_id)
    else:
        ask_password(bot, language_code, user_id)
    bot.set_state(user_id, next_state)

# Initialization get password


@bot.message_handler(state=InitializationStates.get_password)
def get_password_handler(message):
    user_id = message.from_user.id
    next_state = InitializationStates.get_name

    password = message.text

    user = get_user(user_id)
    language_code = user.language_code

    if not user.is_verified:
        company = get_company_by_password(password)
        if company:
            set_user_field(user_id, 'is_verified', True)
            set_user_field(user_id, 'companies', company.name)
            ask_name(bot, language_code, user_id)
            bot.set_state(user_id, next_state)

# Initialization get name


@bot.message_handler(state=InitializationStates.get_name)
def get_name_handler(message):
    user_id = message.from_user.id
    next_state = InitializationStates.get_link

    name = message.text

    user = get_user(user_id)
    language_code = user.language_code

    if user.is_verified:
        set_user_field(user_id, 'name', name)
        ask_link(bot, language_code, user_id)
        bot.set_state(user_id, next_state)

# Initialization get link


@bot.message_handler(state=InitializationStates.get_link)
def get_link_handler(message):
    user_id = message.from_user.id
    next_state = InitializationStates.complete

    link = message.text

    user = get_user(user_id)
    language_code = user.language_code

    if user.is_verified:
        set_user_field(user_id, 'link', link)
        success_initialization(bot, language_code, user_id)
        bot.set_state(user_id, next_state)


# User Settings Menu

@bot.message_handler(commands=['help'])
def get_user_settings_menu_handler(message):
    user_id = message.from_user.id

    user = get_user(user_id)

    if user and user.is_verified:
        language_code = user.language_code
        get_user_settings_menu(bot, language_code, user_id)

# User Settings Menu - User Show Profile


@bot.callback_query_handler(func=lambda call: call.data == 'user_show_profile')
def user_show_profile_callback(call):
    user_id = call.message.chat.id
    message_id = call.message.message_id

    user = get_user(user_id)
    language_code = user.language_code

    message_text = call.message.text
    choosen_option = call.data

    replace_keyboard_on_choosen_option(
        bot, language_code, user_id, message_id, message_text, choosen_option)

    get_user_profile(bot, language_code, user_id, user)


# User Settings Menu - User Change Profile

class ChangeProfileStates:
    get_name = 10
    get_link = 20
    get_work = 30
    get_about = 40
    complete = 50


@bot.callback_query_handler(func=lambda call: call.data == 'user_change_profile')
def user_change_profile_callback(call):
    user_id = call.message.chat.id
    message_id = call.message.message_id

    user = get_user(user_id)
    language_code = user.language_code

    message_text = call.message.text
    choosen_option = call.data

    replace_keyboard_on_choosen_option(
        bot, language_code, user_id, message_id, message_text, choosen_option)

    get_user_change_profile_menu(bot, language_code, user_id)

# User Settings Menu - User Change Profile - Options


@bot.callback_query_handler(func=lambda call: call.data == 'user_change_name')
def user_change_name_callback(call):
    user_id = call.message.chat.id
    message_id = call.message.message_id

    user = get_user(user_id)
    language_code = user.language_code

    message_text = call.message.text
    choosen_option = call.data

    replace_keyboard_on_choosen_option(
        bot, language_code, user_id, message_id, message_text, choosen_option)

    ask_name(bot, language_code, user_id)
    bot.set

# Backs


@bot.callback_query_handler(func=lambda call: call.data in [
    'user_back_get_user_profile',
    'user_back_get_user_change_profile_menu'
])
def back_to_user_settings_callback(call):
    user_id = call.message.chat.id
    message_id = call.message.message_id

    user = get_user(user_id)
    language_code = user.language_code

    message_text = call.message.text
    choosen_option = 'back'

    replace_keyboard_on_choosen_option(
        bot, language_code, user_id, message_id, message_text, choosen_option)

    get_user_settings_menu(bot, language_code, user_id)


bot.add_custom_filter(telebot.custom_filters.StateFilter(bot))
bot.add_custom_filter(telebot.custom_filters.IsDigitFilter())

if __name__ == "__main__":
    # bot.infinity_polling()
    bot.polling()

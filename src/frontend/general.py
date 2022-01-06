from frontend.text import BACK, CHANGE_PROFILE, MY_NAME, SHOW_PROFILE


def replace_keyboard_on_choosen_option(bot, language_code, user_id, message_id, message_text, option):

    if option == 'user_show_profile':
        option = SHOW_PROFILE[language_code]
    elif option == 'back':
        option = BACK[language_code]
    elif option == 'user_change_profile':
        option = CHANGE_PROFILE[language_code]
    elif option == 'user_change_name':
        option = MY_NAME[language_code]

    answer = f'{message_text}\n\n🐱 {option}'
    bot.edit_message_text(
        chat_id=user_id,
        message_id=message_id,
        text=answer
    )

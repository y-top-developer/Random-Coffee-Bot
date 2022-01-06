from frontend.company_admin_settings import get_company_admin_settings_menu, show_users, ask_which_user_choose, get_company_admin_user_settings_menu, ask_are_you_sure, done, get_user_profile


@bot.message_handler(commands=['get_company_admin_settings_menu'])
def get_company_admin_settings_menu_handler(message):
    user_id = message.from_user.id

    get_company_admin_settings_menu(bot, 'en', user_id)


@bot.message_handler(commands=['get_company_admin_user_settings_menu'])
def get_company_admin_user_settings_menu_handler(message):
    user_id = message.from_user.id

    get_company_admin_user_settings_menu(bot, 'en', user_id)


@bot.message_handler(commands=['done'])
def done_handler(message):
    user_id = message.from_user.id

    done(bot, 'en', user_id)


@bot.message_handler(commands=['ask_are_you_sure'])
def ask_are_you_sure_handler(message):
    user_id = message.from_user.id

    ask_are_you_sure(bot, 'en', user_id)


@bot.message_handler(commands=['show_users'])
def show_users_handler(message):
    user_id = message.from_user.id

    show_users(bot, 'en', user_id, 'user1\nuser2')


@bot.message_handler(commands=['ask_which_user_choose'])
def ask_which_user_choose_handler(message):
    user_id = message.from_user.id

    ask_which_user_choose(bot, 'en', user_id)


@bot.message_handler(commands=['get_user_profile'])
def get_user_profile_handler(message):
    user_id = message.from_user.id
    get_user_profile(bot, 'en', user_id, 'USER PROFILE EXAMPLE')

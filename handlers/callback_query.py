import handlers.setting as st, handlers.tests as ts
from handlers.support.importing import *

@dp.callback_query_handler(text="toMenu")
async def inline_toMenu(call: CallbackQuery):

    try:
        await menu.toMenuWithout(call.message.chat.id, call.message.message_id)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с inline_toMenu: {ex}')
        print(f"callback_query.py [INFO] Неполадки с inline_toMenu: {ex}")

@dp.callback_query_handler(text="back_menu_test")
async def inline_toMenu(call: CallbackQuery):

    try:
        await menu.toMenuWithout(call.message.chat.id, call.message.message_id)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с inline_toMenu: {ex}')
        print(f"callback_query.py [INFO] Неполадки с inline_toMenu: {ex}")

@dp.callback_query_handler(text='menu_setting')
async def inline_menu_setting(c: CallbackQuery):
    try:
        setting_inline_button = InlineKeyboardMarkup(row_width=2)

        if db.getting(c.message.chat.id, 'language') in ['ru', 'uk']:
            setting_inline_button.add(InlineKeyboardButton(text='Да, вперед', callback_data='yes_test'))

            if db.getting(c.message.chat.id, 'language') in ['ru', 'uk']:
                
                if db.getting(c.message.chat.id, 'gender') in ["male", "female"]:

                        await bot.edit_message_text("⚙️ Настройки:", c.message.chat.id, c.message.message_id)
                        await bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id, reply_markup=setting_button_ru_men)

                        await bot.edit_message_text("⚙️ Налаштування:", c.message.chat.id, c.message.message_id)
                        await bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id, reply_markup=setting_button_uk_men)

                elif (db.getting(c.message.chat.id, 'gender') == "female"):

                        await bot.edit_message_text("⚙️ Настройки:", c.message.chat.id, c.message.message_id)
                        await bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id, reply_markup = setting_button_ru_women)

                        await bot.edit_message_text("⚙️ Налаштування:", c.message.chat.id, c.message.message_id)
                        await bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id, reply_markup = setting_button_uk_women)
                else:
                    db.adding(c.message.chat.id, 'gender', "male")

        else: 
            db.adding(c.message.chat.id, 'language', 'ru')

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с inline_menu_setting: {ex}')
        print(f"callback_query.py [INFO] Неполадки с inline_menu_setting: {ex}")

@dp.callback_query_handler(text='setting_gender')
async def inline_menu_setting_setting_gender(c: CallbackQuery):

    try:
        if (db.getting(c.message.chat.id, 'gender') == "female"):
            db.adding(c.message.chat.id, 'gender', "male")
            await inline_menu_setting_setting(c)
        else:
            db.adding(c.message.chat.id, 'gender', "female")
            await inline_menu_setting(c)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с setting_gender_ru: {ex}')
        print(f"callback_query.py [INFO] Неполадки с setting_gender_ru: {ex}")

@dp.callback_query_handler(text='setting_gender_ru')
async def setting_gender_ru(c: CallbackQuery):

    try:
        if (db.getting(c.message.chat.id, 'gender') == "female"):
            db.adding(c.message.chat.id, 'gender', "male")
            await inline_menu_setting(c)
        else:
            db.adding(c.message.chat.id, 'gender', "female")
            await inline_menu_setting(c)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с setting_gender_ru: {ex}')
        print(f"callback_query.py [INFO] Неполадки с setting_gender_ru: {ex}")

@dp.callback_query_handler(text='setting_gender_uk')
async def setting_gender_uk(c: CallbackQuery):
    try:
        if (db.getting(c.message.chat.id, 'gender') == "female"):
            db.adding(c.message.chat.id, 'gender', "male")
            await inline_menu_setting(c)
        else:
            db.adding(c.message.chat.id, 'gender', "female")
            await inline_menu_setting(c)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с setting_gender_uk: {ex}')
        print(f"callback_query.py [INFO] Неполадки с setting_gender_uk: {ex}")

@dp.callback_query_handler(text='setting_language_ru')
async def setting_language_ru(c: CallbackQuery):
    try:
        if (db.getting(c.message.chat.id, 'language') == "ru"):
            db.adding(c.message.chat.id, 'language', "uk")
            await inline_menu_setting(c)
        else:
            db.adding(c.message.chat.id, 'language', "ru")
            await inline_menu_setting(c)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с setting_language_ru: {ex}')
        print(f"callback_query.py [INFO] Неполадки с setting_language_ru: {ex}")

@dp.callback_query_handler(text='setting_language_uk')
async def setting_language_uk(c: CallbackQuery):
    try:
        if (db.getting(c.message.chat.id, 'language') == "uk"):
            db.adding(c.message.chat.id, 'language', "ru")
            await inline_menu_setting(c)
        else:
            db.adding(c.message.chat.id, 'language', "uk")
            await inline_menu_setting(c)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с setting_language_uk: {ex}')
        print(f"callback_query.py [INFO] Неполадки с setting_language_uk: {ex}")

@dp.callback_query_handler(text="menu_test")
async def inline_menu_setting_tests(call: CallbackQuery):
    try:
        await ts.tests(call.message.chat.id, call.message.message_id)
    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с inline_menu_setting_tests: {ex}')
        print(f"callback_query.py [INFO] Неполадки с inline_menu_setting_tests: {ex}")

@dp.callback_query_handler(text="menu_setting")
async def inline_menu_setting_setting(call: CallbackQuery):
    try:
        await st.setting(call.message)
    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с inline_menu_setting_setting: {ex}')
        print(f"callback_query.py [INFO] Неполадки с inline_menu_setting_setting: {ex}")

@dp.callback_query_handler(text="menu_calendar")
async def inline_menu_setting_сalendar(call: CallbackQuery):
    try:
        await call.message.answer("Нихера пока-что")
        import handlers.tests as ts
    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с inline_menu_setting_сalendar: {ex}')
        print(f"callback_query.py [INFO] Неполадки с inline_menu_setting_сalendar: {ex}")

@dp.callback_query_handler(text="menu_game")
async def inline_menu_setting_game(call: CallbackQuery):
    try:
        await call.message.answer("Тут нихера нет")
    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с inline_menu_setting_game: {ex}')
        print(f"callback_query.py [INFO] Неполадки с inline_menu_setting_game: {ex}")

@dp.callback_query_handler(text="fb_yes")
async def inline_fb_yes(call: CallbackQuery):

    try:
        lang = db.getting(call.message.chat.id, 'language')
        user_name = call.message.chat.username
        name = call.message.chat.first_name
        await bot.send_message(ADMIN[0], f"@{user_name}: {name}, хочет поговорить :)")
        await bot.send_message(call.message.chat.id, f"{general_text_answer[f'{lang}_feedback_yes']}", parse_mode='html')
        await menu.toMenu(call.message)
    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с inline_fb_yes: {ex}')
        print(f"callback_query.py [INFO] Неполадки с inline_fb_yes: {ex}")

@dp.callback_query_handler(text="fb_no")
async def inline_fb_no(call: CallbackQuery):
    try:
        lang = db.getting(call.message.chat.id, 'language')
        await bot.send_message(call.message.chat.id, f"{general_text_answer[f'{lang}_ask_admin_no']}", parse_mode='html', reply_markup=None)
        await menu.toMenu(call.message)
    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с inline_fb_no: {ex}')
        print(f"callback_query.py [INFO] Неполадки с inline_fb_no: {ex}")
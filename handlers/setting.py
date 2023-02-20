from handlers.support.importing import *

@dp.callback_query_handler(ChatTypeFilter(chat_type=ChatType.PRIVATE), text='menu_setting')
async def inline_menu_setting(c: CallbackQuery):
    try:

        if db.getting(c.message.chat.id, 'language') in ['ru', 'uk']:
            if db.getting(c.message.chat.id, 'gender') in ['man', 'woman']:

                await bot.edit_message_text(short_texts[f"{db.getting(c.message.chat.id, 'language')}_setting"],
                c.message.chat.id, c.message.message_id, reply_markup=InlineKeyboardMarkup(row_width=1).add(
                    InlineKeyboardButton(text= short_texts[f"{db.getting(c.message.chat.id, 'language')}_setting_lang"], callback_data='setting_language'),
                    InlineKeyboardButton(text=short_texts[f"{db.getting(c.message.chat.id, 'language')}_setting_{db.getting(c.message.chat.id, 'gender')}"], callback_data='setting_gender')))

            else: db.adding(c.message.chat.id, 'gender', 'man'), await inline_menu_setting(c)

        else: db.adding(c.message.chat.id, 'language', 'ru'), await inline_menu_setting(c)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с inline_menu_setting: {ex}')
        print(f"callback_query.py [INFO] Неполадки с inline_menu_setting: {ex}")

@dp.callback_query_handler(text='setting_gender')
async def inline_menu_setting_gender(c: CallbackQuery):

    try:
        if db.getting(c.message.chat.id, 'gender') == 'woman':  db.adding(c.message.chat.id, 'gender', "man")
        else:  db.adding(c.message.chat.id, 'gender', "woman") 

        await c.answer(reverse_info[f"{db.getting(c.message.chat.id, 'language')}_gender"]) 
        await inline_menu_setting(c)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с inline_menu_setting_gender: {ex}')
        print(f"callback_query.py [INFO] Неполадки с inline_menu_setting_gender: {ex}")

@dp.callback_query_handler(text='setting_language')
async def inline_menu_setting_language(c: CallbackQuery):

    try:
        if db.getting(c.message.chat.id, 'language') == 'ru':  db.adding(c.message.chat.id, 'language', "uk")
        else:  db.adding(c.message.chat.id, 'language', "ru") 

        await c.answer(reverse_info[f"{db.getting(c.message.chat.id, 'language')}_lang"]) 
        await inline_menu_setting(c)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с inline_menu_setting_language: {ex}')
        print(f"callback_query.py [INFO] Неполадки с inline_menu_setting_language: {ex}")

@dp.callback_query_handler(text='setting_name')
async def inline_menu_setting_name(c: CallbackQuery):

    try:
        if (db.getting(c.message.chat.id, 'gender') == "woman"):
            db.adding(c.message.chat.id, 'gender', "man")
            await inline_menu_setting(c)
        else:
            db.adding(c.message.chat.id, 'gender', "woman")
            await inline_menu_setting(c)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с setting_gender_ru: {ex}')
        print(f"callback_query.py [INFO] Неполадки с setting_gender_ru: {ex}")
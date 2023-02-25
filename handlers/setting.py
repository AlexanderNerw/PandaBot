from handlers.support.importing import *

@dp.callback_query_handler(text='menu_setting')
async def inline_menu_setting(c: CallbackQuery) -> None:
    try:
        setting_button =    InlineKeyboardMarkup(row_width=3) \
        .add(   InlineKeyboardButton(text = settings[f"{db.getting(c.message.chat.id, 'gender')}_{db.getting(c.message.chat.id, 'language')}"], callback_data='setting_gender'), 
                InlineKeyboardButton(text = settings[f"language_{db.getting(c.message.chat.id, 'language')}"], callback_data='setting_language')) \
        .add(   InlineKeyboardButton(text = settings[f"notice_{db.getting(c.message.chat.id, 'notice')}_{db.getting(c.message.chat.id, 'language')}"], callback_data='setting_notice')) \
        .add(   InlineKeyboardButton(text = settings[f"name_{db.getting(c.message.chat.id, 'language')}"]+db.getting(c.message.chat.id, 'username'), callback_data='setting_name'))\
        .add(   InlineKeyboardButton(text = '🔙 Назад', callback_data='toMenu'))

        await bot.edit_message_text(general_text[f"{db.getting(c.message.chat.id, 'language')}_setting"], c.message.chat.id, c.message.message_id, parse_mode='html', reply_markup=setting_button)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'setting.py [INFO] Неполадки с inline_menu_setting: {ex}')
        print(f"setting.py [INFO] Неполадки с inline_menu_setting: {ex}")

@dp.callback_query_handler(text='setting_gender')
async def inline_menu_setting_gender(c: CallbackQuery) -> None:
    try:

        if db.getting(c.message.chat.id, 'gender') == 'woman':
            db.adding(c.message.chat.id, 'gender', "man")
        else:  
            db.adding(c.message.chat.id, 'gender', "woman") 

        await c.answer(reverse_info[f"{db.getting(c.message.chat.id, 'language')}_gender"]) 
        await inline_menu_setting(c)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'setting.py [INFO] Неполадки с inline_menu_setting_gender: {ex}')
        print(f"setting.py [INFO] Неполадки с inline_menu_setting_gender: {ex}")

@dp.callback_query_handler(text='setting_language')
async def inline_menu_setting_language(c: CallbackQuery) -> None:
    try:

        db.adding(c.message.chat.id, 'language', "uk") if db.getting(c.message.chat.id, 'language') == 'ru' else db.adding(c.message.chat.id, 'language', "ru")

        await c.answer(reverse_info[f"{db.getting(c.message.chat.id, 'language')}_lang"]) 
        await inline_menu_setting(c)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'setting.py [INFO] Неполадки с inline_menu_setting_language: {ex}')
        print(f"setting.py [INFO] Неполадки с inline_menu_setting_language: {ex}")

class SetName(StatesGroup):
    name = State()

@dp.callback_query_handler(text='setting_name')
async def inline_menu_setting_name(c: CallbackQuery) -> None:
    try:

        await bot.delete_message(c.message.chat.id, c.message.message_id), await SetName.name.set()
        await bot.send_message(c.message.chat.id, general_text[f"{db.getting(c.message.chat.id, 'language')}_set_name"], reply_markup=
        ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(db.getting(c.message.chat.id, 'username')))

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'setting.py [INFO] Неполадки с inline_menu_setting_name: {ex}')
        print(f"setting.py [INFO] Неполадки с inline_menu_setting_name: {ex}")

@dp.message_handler(content_types='text', state=SetName)
async def set_name(message: Message, state: FSMContext) -> None: 
    try:
        if message.text == '/menu':
            await bot.send_message(f"{db.getting(message.chat.id, 'language')}_ask_admin_no", reply_markup=ReplyKeyboardRemove())

        else: 
            db.adding(message.chat.id, 'username', message.text)
            await bot.send_message(message.chat.id, general_text[f"{db.getting(message.chat.id, 'language')}_to_menu"], reply_markup=ReplyKeyboardRemove())
            

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'setting.py [INFO] Неполадки с inline_menu_setting_notice: {ex}')
        print(f"setting.py [INFO] Неполадки с inline_menu_setting_notice: {ex}")

    finally:   
        await state.finish()
        await menu.toMenu(message)

@dp.callback_query_handler(text='setting_notice')
async def inline_menu_setting_notice(c: CallbackQuery) -> None:
    try:

        if (db.getting(c.message.chat.id, 'notice') == 1):  db.adding(c.message.chat.id, 'notice', 0)
        else:                                               db.adding(c.message.chat.id, 'notice', 1)

        await inline_menu_setting(c)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'setting.py [INFO] Неполадки с inline_menu_setting_notice: {ex}')
        print(f"setting.py [INFO] Неполадки с inline_menu_setting_notice: {ex}")
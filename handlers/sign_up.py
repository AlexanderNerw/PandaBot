from aiogram.dispatcher.filters.builtin import CommandStart, ChatTypeFilter
from handlers.support.importing import *


# Машина сострояний
class ProfileStateGroup(StatesGroup):
    start = State()
    lang = State()
    name = State()
    gender = State()

##################################### - СТАРТ ЛИЧНОГО ЧАТА - #######################################################

@dp.message_handler(CHAT_PRIVATE, CommandStart())  ## - СТАРТ МЕНЮ ################### 
async def start(message: Message, state: FSMContext) -> None:
    try:    

        if (not db.user_in_database(message.chat.id)) or (not db.user_online_in_database(message.chat.id)):  # Пользователя нет в БД или он не онлайн

            db.add_subs(message.chat.id)
            if message.from_user.language_code in ['ru','uk']:
                await message.answer(   general_text[f'{message.from_user.language_code}_hello'] + f"<b>{message.chat.first_name}</b>! 😉"
                                     +  start_sign_up[f'{message.from_user.language_code}_bot_start'], parse_mode='html', reply_markup=
                                        InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                                        InlineKeyboardButton("Регистрация 🔸" if message.from_user.language_code == 'ru' else "Регiстрацiя 🔸", callback_data='Регистрация 🔸')))

            else: await message.answer( general_text['ru_hello'] + f"<b>{message.chat.first_name}</b>! 😉"
                                     +  start_sign_up['ru_bot_start'], parse_mode='html', reply_markup=
                                        InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                                        InlineKeyboardButton("Регистрация 🔸", callback_data='Регистрация 🔸')))
            await ProfileStateGroup.start.set()

        else:  # Пользователь есть в БД
            lang = db.getting(message.chat.id, 'language')
            await message.answer(f"{general_text[f'{lang}_hello']}, <b>{db.getting(message.chat.id, 'username')}</b>! {start_sign_up[f'{lang}_again_bot_start']}", parse_mode='html')
            await menu.toMenu(message)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'sign_up.py [INFO] Неполадки со start-menu: {ex}')
        print(f'sign_up.py [INFO] Неполадки со start-menu: {ex}')
#==============================================================================
@dp.callback_query_handler(CHAT_PRIVATE, text = 'Регистрация 🔸', state='*')
async def start_reg(c: CallbackQuery, state: FSMContext) -> None:
    try:
        if (not db.user_in_database(c.message.chat.id)) or (not db.user_online_in_database(c.message.chat.id)):  # Пользователя нет в БД или он не онлайн
            choice_lang_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*["Русский", "Українська"])

            db.adding(c.message.chat.id, 'username', c.message.chat.first_name), await c.answer()
            await bot.send_message(c.message.chat.id, start_sign_up[f'ru_start_1/3'], parse_mode='html', reply_markup=choice_lang_kb)
            await ProfileStateGroup.start.set()
            await ProfileStateGroup.next()

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'sign_up.py [INFO] Неполадки в start_reg: {ex}')
        print(f'sign_up.py [INFO] Неполадки в start_reg: {ex}')
#==============================================================================
@dp.message_handler(CHAT_PRIVATE, content_types=['text'], state=ProfileStateGroup.lang)
async def start_lang(message: Message, state: FSMContext) -> None:
    try:
        
        if message.text in ['Русский', 'Українська']:

            async with state.proxy() as data:
                data['lang'] = 'ru' if message.text == 'Русский' else 'uk' 

            db.adding(message.chat.id, 'language', data['lang'])
            await message.answer(start_sign_up[f"{data['lang']}_start_2/3"], parse_mode='html',
            reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(message.chat.first_name)))
            await ProfileStateGroup.next()

        else:
            await message.reply(start_sign_up['ru_dont_know_start'])

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'sign_up.py [INFO] Неполадки в start_lang: {ex}')
        print(f'sign_up.py [INFO] Неполадки в start_lang: {ex}')
#==============================================================================
@dp.message_handler(CHAT_PRIVATE, content_types=['text'], state=ProfileStateGroup.name)
async def start_name(message: Message, state: FSMContext) -> None:

    try:
        async with state.proxy() as data: 
            if len(message.text) < 31:
                db.adding(message.from_user.id, 'username', message.text)
                buttons = ["Я парень 🧔🏽‍♂️", "Я девушка 👱🏼‍♀️"] if data['lang'] == 'ru' else ["Я хлопець 🧔🏽‍♂️", "Я дівчина 👱🏼‍♀️"]

                await message.answer(start_sign_up[f"{data['lang']}_start_3/3"], parse_mode='html',
                reply_markup=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*buttons))
                await ProfileStateGroup.next()

            else:
                await message.reply(start_sign_up[f"{data['lang']}_start_too_long_name"])

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'sign_up.py [INFO] Неполадки в start_name: {ex}')
        print(f'sign_up.py [INFO] Неполадки в start_name: {ex}')
#==============================================================================
@dp.message_handler(CHAT_PRIVATE, content_types=['text'], state=ProfileStateGroup.gender)
async def start_gender(message: Message, state: FSMContext) -> None:
    try:
        if message.text in ['Я парень 🧔🏽‍♂️', 'Я хлопець 🧔🏽‍♂️', "Я девушка 👱🏼‍♀️", "Я дівчина 👱🏼‍♀️"]:

            async with state.proxy() as data: 
                db.adding(message.from_user.id, 'gender', 'man' if message.text in ['Я парень 🧔🏽‍♂️', 'Я хлопець 🧔🏽‍♂️'] else 'woman')
                await bot.send_message(ADMIN[1], '[INFO] Новый зарегистрированный пользователь')
                await message.answer(general_text[f"{data['lang']}_to_menu"], reply_markup=ReplyKeyboardRemove())
                db.adding(message.chat.id, 'status', 1)
                await state.finish(), await menu.toMenu(message)

        else:
            await message.reply(start_sign_up[f"{data['lang']}_dont_know_start"])

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'sign_up.py [INFO] Неполадки в start_gender: {ex}')
        print(f'sign_up.py [INFO] Неполадки в start_gender: {ex}')


##################################### - СТАРТ ГРУППОВОГО ЧАТА -  ###################################################

@dp.message_handler(CHAT_GROUP, CommandStart())  ## - СТАРТ МЕНЮ ################### 
async def start_group(message: Message, state: FSMContext) -> None:
    try:    
        if (not db.user_in_database(message.chat.id)) or (not db.user_online_in_database(message.chat.id)):  # Пользователя нет в БД или он не онлайн

            db.add_subs(message.chat.id)
            if message.from_user.language_code in ['ru','uk']:
                await message.answer(message.from_user.id,
                                        general_text[f'{message.from_user.language_code}_hello'] + f" <b>{message.chat.first_name}</b>! 😉"
                                     +  start_sign_up[f'{message.from_user.language_code}_bot_start'], parse_mode='html', reply_markup=
                                        InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                                        InlineKeyboardButton("Регистрация 🔸" if message.from_user.language_code == 'ru' else "Регiстрацiя 🔸", callback_data='Регистрация 🔸')))

            else:
                await message.answer(   general_text[f'ru_hello'] + f"<b>{message.chat.first_name}</b>! 😉"
                                     +  start_sign_up['ru_bot_start'], parse_mode='html', reply_markup=
                                        InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                                        InlineKeyboardButton("Регистрация 🔸", callback_data='Регистрация 🔸')))

            await ProfileStateGroup.start.set()

        else:  # Пользователь есть в БД

            lang = db.getting(message.from_user.id, 'language')
            await message.answer(f"{general_text[f'{lang}_hello']}, <b>{db.getting(message.from_user.id, 'username')}</b>! {start_sign_up[f'{lang}_again_bot_start']}", parse_mode='html')
            await menu.toMenu(message)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'sign_up.py [INFO] Неполадки со start-menu: {ex}')
        print(f'sign_up.py [INFO] Неполадки со start-menu: {ex}')





def register(dp : Dispatcher):
    dp.register_message_handler(start, CommandStart(), ChatTypeFilter(chat_type=ChatType.PRIVATE))
    dp.register_message_handler(start_lang, content_types=['text'], state=ProfileStateGroup.lang)
    dp.register_message_handler(start_name, content_types=['text'], state=ProfileStateGroup.name)
    dp.register_message_handler(start_gender, content_types=['text'], state=ProfileStateGroup.gender)
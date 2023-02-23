from aiogram.dispatcher.filters.builtin import CommandStart, ChatTypeFilter
from handlers.support.importing import *


# Машина сострояний
class ProfileStateGroup(StatesGroup):
    start = State()
    lang = State()
    name = State()
    gender = State()


@dp.message_handler(ChatTypeFilter(chat_type=ChatType.PRIVATE), CommandStart())  # СТАРТ МЕНЮ ###################### commands=['start'] CommandStart()
async def start(message: Message, state: FSMContext) -> None:
    try:    

        if (not db.user_in_database(message.chat.id)) or (not db.user_online_in_database(message.chat.id)):  # Пользователя нет в БД или он не онлайн
            choice_reg = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(InlineKeyboardButton("Регистрация 🔸", callback_data='Регистрация 🔸'))
            db.add_subs(message.chat.id)

            if message.from_user.language_code in ['ru','uk']:
                await message.answer(f"{general_text[f'{message.from_user.language_code}_hello']} <b>{message.chat.first_name}</b>! 😉 {start_sign_up[f'{message.from_user.language_code}_bot_start']}",
                                        parse_mode='html', reply_markup=choice_reg)

            else:
                await message.answer(start_sign_up[f'ru_bot_start'])

            await ProfileStateGroup.start.set()

        else:  # Пользователь есть в БД

            lang = db.getting(message.from_user.id, 'language')
            await message.answer(f"{general_text[f'{lang}_hello']}, <b>{db.getting(message.from_user.id, 'username')}</b>! {start_sign_up[f'{lang}_again_bot_start']}", parse_mode='html')
            await menu.toMenu(message)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'sing_up.py [INFO] Неполадки со start-menu: {ex}')
        print(f'sing_up.py [INFO] Неполадки со start-menu: {ex}')

#==============================================================================

@dp.callback_query_handler(text = 'Регистрация 🔸', state='*')
async def start_reg(c: CallbackQuery, state: FSMContext) -> None:
    try:
        if (not db.user_in_database(c.message.chat.id)) or (not db.user_online_in_database(c.message.chat.id)):  # Пользователя нет в БД или он не онлайн
            choice_lang_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*["Русский", "Українська"])

            db.adding(c.message.chat.id, 'username', c.message.chat.first_name), await c.answer()
            await bot.send_message(c.message.chat.id, start_sign_up[f'ru_start_1/3'], parse_mode='html', reply_markup=choice_lang_kb)
            await ProfileStateGroup.next()

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'main.py [INFO] Неполадки в start_reg: {ex}')
        print(f'main.py [INFO] Неполадки в start_reg: {ex}')

@dp.message_handler(content_types=['text'], state=ProfileStateGroup.lang)
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
        await bot.send_message(ADMIN[1], f'main.py [INFO] Неполадки в start_lang: {ex}')
        print(f'main.py [INFO] Неполадки в start_lang: {ex}')

#==============================================================================

@dp.message_handler(content_types=['text'], state=ProfileStateGroup.name)
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
        await bot.send_message(ADMIN[1], f'main.py [INFO] Неполадки в start_name: {ex}')
        print(f'main.py [INFO] Неполадки в start_name: {ex}')

#==============================================================================

@dp.message_handler(content_types=['text'], state=ProfileStateGroup.gender)
async def start_gender(message: Message, state: FSMContext) -> None:

    try:

        if message.text in ['Я парень 🧔🏽‍♂️', 'Я хлопець 🧔🏽‍♂️', "Я девушка 👱🏼‍♀️", "Я дівчина 👱🏼‍♀️"]:

            async with state.proxy() as data: 
                db.adding(message.from_user.id, 'gender', 'man' if message.text in ['Я парень 🧔🏽‍♂️', 'Я хлопець 🧔🏽‍♂️'] else 'woman')
                await bot.send_message(ADMIN[1], '[INFO] Новый зарегистрированный пользователь')
                await message.answer(start_sign_up[f"{data['lang']}_start_to_menu"], reply_markup=ReplyKeyboardRemove())
                await state.finish()
                db.add_subs_online(message.chat.id)
                await menu.toMenu(message)

        else:
            await message.reply(start_sign_up[f"{data['lang']}_dont_know_start"])

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'sing_up.py [INFO] Неполадки в start_gender: {ex}')
        print(f'main.py [INFO] Неполадки в start_gender: {ex}')


def register(dp : Dispatcher):
    dp.register_message_handler(start, CommandStart(), ChatTypeFilter(chat_type=ChatType.PRIVATE))
    dp.register_message_handler(start_lang, content_types=['text'], state=ProfileStateGroup.lang)
    dp.register_message_handler(start_name, content_types=['text'], state=ProfileStateGroup.name)
    dp.register_message_handler(start_gender, content_types=['text'], state=ProfileStateGroup.gender)
from aiogram.dispatcher.filters.builtin import CommandStart, ChatTypeFilter
from handlers.support.importing import *


# Машина сострояний
class ProfileStateGroup(StatesGroup):
    lang = State()
    name = State()
    gender = State()


@dp.message_handler(CommandStart(), ChatTypeFilter(chat_type=ChatType.PRIVATE))  # СТАРТ МЕНЮ ###################### commands=['start']
async def start(message: Message) -> None:

    try:

        lang = message.from_user.language_code
        if (not db.user_in_database(message.chat.id)):  # Пользователя нет в БД
            if lang in ['ru','uk']:
                await message.answer(f"{hello[lang]} <b>{message.chat.first_name}</b>! 😉 {start_sign_up[f'{lang}_bot_start']}",
                parse_mode='html', reply_markup=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*["Русский", "Українська"]))

                await message.answer(start_sign_up[f'{lang}_start_1/3'])
                await ProfileStateGroup.lang.set()

            else:
                await message.answer(start_sign_up['en'])
                await ProfileStateGroup.lang.set()

        else:  # Пользователь есть в БД

            try:
                name = db.getting(message.from_user.id, 'username')
                lang = db.getting(message.from_user.id, 'language')
                await message.answer(f"{hello[lang]}, <b>{name}</b>! {start_sign_up[f'{lang}_again_bot_start']}", parse_mode='html')
                await menu.toMenu(message)

            except Exception as ex:
                await bot.send_message(ADMIN[1], 'main.py [INFO] Неполадки со start-menu: # Пользователь есть в БД', ex)
                print('main.py [INFO] Неполадки со start-menu: # Пользователь есть в БД', ex)
                

    except Exception as ex:
        await bot.send_message(ADMIN[1], 'main.py [INFO] Неполадки со start-menu: ', ex)
        print('main.py [INFO] Неполадки со start-menu: ', ex)


@dp.message_handler(content_types=['text'], state=ProfileStateGroup.lang)
async def start_lang(message: Message) -> None:

    try:
        
        if message.text in ['Русский', 'Українська']:
            lang = 'uk' if message.text == 'Українська' else 'ru'
            db.add_subs(message.from_user.id)
            db.adding(message.from_user.id, 'language', lang)
            await message.answer(start_sign_up[f'{lang}_start_2/3'], parse_mode='html',
            reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(message.chat.first_name)))
            await ProfileStateGroup.next()

        else:
            await message.reply(start_sign_up['ru_dont_know_start'])

    except Exception as ex:
        await bot.send_message(ADMIN[1], 'main.py [INFO] Неполадки в start_lang: ', ex)
        print('main.py [INFO] Неполадки в start_lang: ', ex)


@dp.message_handler(content_types=['text'], state=ProfileStateGroup.name)
async def start_name(message: Message) -> None:

    try:
        lang = db.getting(message.from_user.id, 'language') 
        db.adding(message.from_user.id, 'username', message.text)
        buttons = ["Я парень 🧔🏽‍♂️", "Я девушка 👱🏼‍♀️"] if lang == 'ru' else ["Я хлопець 🧔🏽‍♂️", "Я дівчина 👱🏼‍♀️"]

        await message.answer(start_sign_up[f'{lang}_start_3/3'], parse_mode='html',
        reply_markup=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*buttons))
        await ProfileStateGroup.next()

    except Exception as ex:
        await bot.send_message(ADMIN[1], 'main.py [INFO] Неполадки в start_name: ', ex)
        print('main.py [INFO] Неполадки в start_name: ', ex)


@dp.message_handler(content_types=['text'], state=ProfileStateGroup.gender)
async def start_gender(message: Message, state: FSMContext) -> None:

    try:
        lang = db.getting(message.from_user.id, 'language')
        if message.text in ['Я парень 🧔🏽‍♂️', 'Я хлопець 🧔🏽‍♂️', "Я девушка 👱🏼‍♀️", "Я дівчина 👱🏼‍♀️"]:
            gender = 'male' if message.text in ['Я парень 🧔🏽‍♂️', 'Я хлопець 🧔🏽‍♂️'] else 'female'
            db.adding(message.from_user.id, 'gender', gender)

            await bot.send_message(ADMIN[1], '[INFO] Новый зарегистрированный пользователь')
            await message.answer(start_sign_up[f'{lang}_start_to_menu'], reply_markup=ReplyKeyboardRemove())
            await state.finish()
            await menu.toMenu(message)

        else:
            await message.reply(start_sign_up[f'{lang}_dont_know_start'])

    except Exception as ex:
        await bot.send_message(ADMIN[1], 'main.py [INFO] Неполадки в start_gender: ', ex)
        print('main.py [INFO] Неполадки в start_gender: ', ex)


from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, Message, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from handlers.config import dp, bot, Dispatcher, ADMIN
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from handlers.querry_db import db
from handlers.dialogs import *
from aiogram import executor
from callback_query import *
from handlers.tests import *
import asyncio, menu


# Машина сострояний
class ProfileStateGroup(StatesGroup):
    lang = State()
    name = State()
    gender = State()


@dp.message_handler(commands=['start'])  # СТАРТ МЕНЮ ######################
async def start(message: Message) -> None:

    try:
        lang = message.from_user.language_code
        if (not db.subsex(message.from_user.id)):  # Пользователя нет в БД
            if lang in ['ru','uk']:
                await message.answer(f"{hello[lang]} <b>{message.chat.first_name}</b>! 😉 {start_sign_up[f'{lang}_bot_start']}",
                parse_mode='html', reply_markup=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*["Русский", "Українська"]))

                await message.answer(start_sign_up[f'{lang}_start_1/3'])
                await ProfileStateGroup.lang.set()

            else:
                await message.answer(start_sign_up['en'])
                await ProfileStateGroup.lang.set()

        else:  # Пользователь есть в БД
            name = db.getting(message.from_user.id, 'username')
            lang = db.getting(message.from_user.id, 'language')
            await message.answer(f"{hello[lang]}, <b>{name}</b>! {start_sign_up[f'{lang}_again_bot_start']}", parse_mode='html')
            await menu.toMenu(message)

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


# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№ БОТ БОТ БОТ БОТ БОТ №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

# ******************************* АДМИНИСТРИРОВАНИЕ *******************************

@dp.message_handler(commands=['help'])
async def help_panel(message: Message) -> None:
    language = db.getting(message.chat.id, 'language')
    await message.answer(help_menu[language], parse_mode='html')

# ------------------------------------------------

@dp.message_handler(commands=['negr'])
async def admin_panel(message: Message) -> None:

    try:
        if message.from_user.id in ADMIN:
            await message.answer('Hi, my lord.')
            await message.answer('Here:\n/start - Старт, общий запуск\n/pizda - Тестирование функций\n/poh - Пнуть Саню\n/sending - (id) (text)\n/mega_sending - (text)')
        else:
            await message.answer('Кудааа мы лезем? Не положено, давай в меню.')
            await menu.toMenu(message)
    except Exception as ex:
        await bot.send_message(ADMIN[1], 'main.py [INFO] Неполадки в admin_panel: ', ex)
        print('main.py [INFO] Неполадки в admin_panel: ', ex)

# ------------------------------------------------

@dp.message_handler(commands=['mega_send'])
async def mega_sending(message: Message) -> None:

    if message.from_user.id in ADMIN:
        try:
            a = db.get_all('user_id')
            for i in a:
                await bot.send_message(*i, message.from_chat.text[13:])
        except Exception as ex:
            await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки в mega_sending: {ex}")
            print(f"main.py [INFO] Неполадки в mega_sending: {ex}")
    else:
        await message.answer('Кудааа мы лезем? Не положено, давай в меню.')
        await menu.toMenu(message)

# ------------------------------------------------

@dp.message_handler(commands=['send'])
async def sending(message: Message) -> None:

    if message.from_user.id in ADMIN:
        try:
            await bot.send_message(message.text[9:20], f"〽️ Автор: {message.text[20:]}")
        except Exception as ex:
            await bot.send_message(ADMIN[1], f"main.py [INFO] Неполдаки в sending: {ex}")
            print(f"main.py [INFO] Неполадки в sending: {ex}")
    else:
        await message.answer('Кудааа мы лезем? Не положено, давай в меню.')
        await menu.toMenu(message)

# ------------------------------------------------

class AskAdmin(StatesGroup):
    ask = State()

@dp.message_handler(commands=['cancel'], state=AskAdmin)
async def ask_cancel(message: Message, state: FSMContext) -> None:

    try:
        lang = db.getting(message.from_user.id, 'language')
        await bot.send_message(message.chat.id, ask_admin_no[lang], reply_markup=ask_admin_no)
        await state.finish()
        await menu.toMenu(message)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки в ask_cancel: {ex}")
        print(f"main.py [INFO] Неполадки в ask_cancel: {ex}")


@dp.message_handler(commands=['ask'])
async def ask_user(message: Message) -> None:
    try:
        lang = db.getting(message.from_user.id, 'language')
        name = message.from_user.first_name

        if message.text.strip() != '/ask':
            await bot.send_message(ADMIN[1], f'{name} - id: {message.chat.id}, @{message.chat.username}\nMessage: {message.text[5:]}')

        else:
            await message.answer(empty_ask[lang])
            await AskAdmin.ask.set()

    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки в ask_user: {ex}")
        print(f"main.py [INFO] Неполадки в ask_user: {ex}")


@dp.message_handler(content_types=['text'], state=AskAdmin.ask)
async def ask_text(message: Message, state: FSMContext) -> None:
    try:
        lang = db.getting(message.from_user.id, 'language')
        name = message.from_user.first_name
        await bot.send_message(ADMIN[1], f'{message.from_user.first_name} - id: {message.chat.id}, @{message.chat.username}\nMessage: {message.text}')
        await state.finish()
        await menu.toMenu(message)
    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки в ask_user_text: {ex}")
        print(f"main.py [INFO] Неполадки в ask_user_text: {ex}")


# ------------------------------------------------

@dp.message_handler(commands=["feedback"])
async def feedback(message: Message) -> None:

    try:
        if (db.getting(message.chat.id, 'language') == "ru"):
            await message.answer("Говорят, через это меню можно поговорить с автором бота. Точно хочешь? 🙂", reply_markup=kb.fbBRu)
        else:
            await message.answer("Кажуть, через цей відділ можна поговорити з автором бота. Точно хочеш? 🙂", reply_markup=kb.fbBUa)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'main.py [INFO] Неполдаки в начале feedback: {ex}')
        print(f"main.py [INFO] Неполадки в начале feedback: {ex}")

# ------------------------------------------------

@dp.message_handler(commands=['poh'])
async def poh(message: Message):
    lang = db.getting(message.from_user.id, 'language')

    try:
        name = db.getting(message.from_user.id, 'username')
        await bot.send_message(ADMIN[1], f"@{message.chat.username}: {name}, {message.chat.id} тебя пнул :)")
        if lang == 'ru':
            await message.answer('Всё сделано босс. Я его пнул 😀')
        elif lang == 'uk':
            await message.answer('Все зроблено босс. Я його пнув 😀')

    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки с poh: {ex}")
        print(f"main.py [INFO] Неполадки с poh: {ex}")

# ------------------------------------------------

@dp.message_handler(commands=['pizda'])
async def pizda(message: Message):
    lang = 'ru'
    try:
        await message.answer(f"{depression_beka_result[f'{lang}0-9']}\n\n", parse_mode='html')
        await message.answer(f"{depression_beka_result[f'{lang}10-15']}\n\n", parse_mode='html')
        await message.answer(f"{depression_beka_result[f'{lang}16-19']}\n\n", parse_mode='html')
        await message.answer(f"{depression_beka_result[f'{lang}20-29']}\n\n", parse_mode='html')
        await message.answer(f"{depression_beka_result[f'{lang}30-63']}\n\n", parse_mode='html')
        print(message.chat.first_name)
    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки с test-panel pizda: {ex}")
        print(f"main.py [INFO] Неполадки с test-panel pizda: {ex}")

# ------------------------------------------------


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    #users = db.get_all()
    #print(users)
    #for user in users:
    #    await bot.send_message(user['user_id'], f'Ща я тебя удалю из базы данных, подожди', reply_markup=go_to_menu)
    #await bot.send_message(720526928, f'Летс гоу', reply_markup=go_to_menu)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
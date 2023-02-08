from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, Message
import handlers.setting as st, handlers.keyboards as kb, handlers.tests as ts, menu, callback_querry
from aiogram.dispatcher.filters.state import State, StatesGroup
from handlers.config import dp, bot, Dispatcher, ADMIN
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram import executor
from handlers.querry_db import db
from handlers.dialogs import *



# Машина сострояний
class ClientStateGroup(StatesGroup):
    photo = State()
    desc = State()

@dp.message_handler(commands=['cancel'])
async def get_cancel(message: Message, state: FSMContext) -> None:
    await state.finish()


#№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№ БОТ БОТ БОТ БОТ БОТ №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

@dp.message_handler(commands=['start'])
async def welcome(message) -> None: ################### СТАРТ МЕНЮ ######################
    global msg
    msg = message

    try:
        if(not db.subsex(message.from_user.id)): # Пользователя нет в БД

            name_start = str(message.from_user.first_name)
            language = str(message.from_user.language_code)
            db.add_subs(message.from_user.id)
            db.adding(message.from_user.id, 'username', name_start)
            db.adding(message.from_user.id, 'language', language)
            await message.answer( f"{hi[language]} <b>{name_start}</b>! 😉 {hi_start[language]}" , parse_mode='html', reply_markup=kb.languageB)

        else: # Пользователь есть в БД
            global name
            name = db.getting(message.from_user.id, 'username')
            language = db.getting(message.from_user.id, 'language')
            await message.answer( f"{hi[language]} <b>{name}</b>! {again_hi_start[language]}", parse_mode='html')

    except Exception as ex:
        print('[INFO] Error of start-menu: ', ex)

#------------------------------------------------  

#******************************* АДМИНИСТРИРОВАНИЕ *******************************

@dp.message_handler(commands=['help'])
async def help_panel(message) -> None:
    global msg
    msg = message
    await message.answer('Here:\n/start - Старт, общий запуск\n/poh - Пнуть Админа\n/ask - Сообщение админу ( /ask text )"\n/feedback - Связь с автором')
  
#------------------------------------------------  

@dp.message_handler(commands=['negritos'])
async def admin_panel(message) -> None:
    global msg
    msg = message
    try:
        if message.from_user.id in ADMIN:
            await message.answer('Hi, my lord.')
            await message.answer('Here:\n/start - Старт, общий запуск\n/terakota - Тестирование функций\n/hyi - Пнуть Саню\n/sending - (id) (text)\n/mega_sending - (text)')
        else:
            await message.answer('Кудааа мы лезем? Не положено, давай в меню.')
            await menu.toMenu(message)
    except Exception as ex:
        print('Ошибка панели админа: ', ex)

#------------------------------------------------  

@dp.message_handler(commands=['mega_sending'])
async def mega_sending(message) -> None:
    global msg
    msg = message
    try:
        a = db.get_all('user_id')
        for i in a:
            await bot.send_message(*i, message.from_chat.text[13:])
    except Exception as ex:
        print("mega_sending не нормас: ", ex)

#------------------------------------------------  

@dp.message_handler(commands=['sending'])
async def sending(message) -> None:
    global msg
    msg = message

    try:
        await bot.send_message(message.text[9:20], f"Автор: {message.text[20:]}")
    except Exception as ex:
        print("mega_sending не нормас: ", ex)

#------------------------------------------------  

@dp.message_handler(commands=['ask'])
async def ask(message) -> None:
    global msg, name
    msg = message
    name = message.from_user.first_name
    try:
        await bot.send_message(ADMIN[0], f'{name} - id: {message.from_user.id}, @{message.from_user.username}\nMessage: {message.text[5:]}')
    except Exception as ex:
        print("mega_sending не нормас: ", ex)

#------------------------------------------------  

@dp.message_handler(commands=["feedback"])
async def feedback(message) -> None: 
    global msg
    msg = message
    try:
        if (db.getting(message.from_user.id, 'language') == "ru"):
            await message.answer("Говорят, через это меню можно поговорить с автором бота. Точно хочешь? 🙂", reply_markup=kb.fbBRu)
        else: 
            await message.answer("Кажуть, через цей відділ можна поговорити з автотором бота. Точно хочеш? 🙂", reply_markup=kb.fbBUa)

    except Exception as ex:
        print('Ошибка feedback начала: ', ex)

#------------------------------------------------  

@dp.message_handler(commands=['poh'])
async def poh(message):
    global msg
    msg = message

    try:
        user_name = message.from_user.username
        name = db.getting(message.from_user.id, 'name')
        await bot.send_message(ADMIN[0], f"@{user_name}: {name} тебя пнул :)")
        await message.answer('Всё сделано босс. Я его уложил')
    except Exception as ex:
        print("poh не нормас: ", ex)

#------------------------------------------------  

@dp.message_handler(commands=['pizda'])
async def pizda(message):
    global msg
    msg = message
    try:
        pass
    except Exception as ex:
        print("pizda не нормас: ", ex)

#------------------------------------------------  


if __name__ == '__main__':
    executor.start_polling(dispatcher = dp, skip_updates= True)
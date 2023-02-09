from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, Message, KeyboardButton
import handlers.setting as st, handlers.keyboards as kb, handlers.tests as ts, menu, callback_querry
from aiogram.dispatcher.filters.state import State, StatesGroup
from handlers.config import dp, bot, Dispatcher, ADMIN
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram import executor
from handlers.querry_db import db
from handlers.dialogs import *


# Машина сострояний
class ProfileStateGroup(StatesGroup):
    lang = State()
    name = State()
    gender = State()

@dp.message_handler(commands=['start']) ################### СТАРТ МЕНЮ ######################
async def start(message: Message) -> None:
    language = message.from_user.language_code
    try:
        if(not db.subsex(message.from_user.id)): # Пользователя нет в БД
            if language == 'ru' or language == 'uk':
                await message.answer( f"{hi[language]} <b>{message.from_user.first_name}</b>! 😉 {hi_start[language]}",
                                                                                                parse_mode='html', reply_markup=kb.languageB)
                await message.answer(get_lang_start[language])
                await ProfileStateGroup.lang.set()                                                                               

            else:
                await message.answer(hi_start['en'])
                await ProfileStateGroup.lang.set()

        else: # Пользователь есть в БД
            names = db.getting(message.from_user.id, 'username')
            language = db.getting(message.from_user.id, 'language')
            await message.answer( f"{hi[language]} <b>{names}</b>! {again_hi_start[language]}", parse_mode='html')
            await menu.toMenu(message)

    except Exception as ex:
        print('[INFO] Error of start-menu: ', ex)

@dp.message_handler(commands=['cancel'], state='*')
async def get_cancel(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await start(message)

@dp.message_handler( content_types=['text'], state=ProfileStateGroup.lang )
async def start_lang(message: Message) -> None:
    try:
        nameKb = ReplyKeyboardMarkup(resize_keyboard=True)
        nameKb.add(KeyboardButton(message.from_user.first_name))

        if message.text == 'Русский':
            db.add_subs(message.from_user.id)
            db.adding(message.from_user.id, 'language', 'ru')
            await message.answer('Супер!\n2/3: Как мне тебя называть? 🙂', reply_markup=nameKb)
            await ProfileStateGroup.next()

        elif message.text == 'Українська':
            db.add_subs(message.from_user.id)
            db.adding(message.from_user.id, 'language', 'uk')
            await message.answer('Супер!\n2/3: Як мені тебе називати? 🙂', reply_markup=nameKb)
            await ProfileStateGroup.next()
        else:
            await message.reply(dont_know_start[message.from_user.language_code])
    except Exception as ex:
        print('[INFO] Error in start_lang: ', ex)


@dp.message_handler( content_types=['text'], state=ProfileStateGroup.name )
async def start_name(message: Message) -> None:
    try:
        db.adding(message.from_user.id, 'username', message.text)
        if db.getting(message.from_user.id, 'language') == 'ru':
            await message.answer('3/3: Хорошо, ты парень или девушка? 🚻', reply_markup=kb.start_gender_butt_ru)

        elif db.getting(message.from_user.id, 'language') == 'uk':
            await message.answer('3/3: Добре, ти хлопець чи дівчина? 🚻', reply_markup=kb.start_gender_butt_uk)

        await ProfileStateGroup.next()

    except Exception as ex:
        print('[INFO] Error in start_name: ', ex)


@dp.message_handler( content_types=['text'], state=ProfileStateGroup.gender )
async def start_gender(message: Message, state: FSMContext) -> None:
    try:
        lang = db.getting(message.from_user.id, 'language')
        if message.text == 'Я парень 🧔🏽‍♂️' or message.text == 'Я хлопець 🧔🏽‍♂️':
            db.adding(message.from_user.id, 'gender', 'male')
            await bot.send_message(ADMIN[0], 'Новый зарегистрированный пользователь')
            await message.answer(new_user_menu[lang])
            await state.finish()
            await menu.toMenu(message)
        
        elif message.text == "Я девушка 👱🏼‍♀️" or message.text == "Я дівчина 👱🏼‍♀️":
            db.adding(message.from_user.id, 'gender', 'female')
            await bot.send_message(ADMIN[0], 'Новый зарегистрированный пользователь')
            await message.answer(new_user_menu[lang])
            await state.finish()
            await menu.toMenu(message)

        else:
            await message.reply(dont_know_start[lang])

    except Exception as ex:
        print('[INFO] Error in start_gender: ', ex)


#№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№ БОТ БОТ БОТ БОТ БОТ №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

#******************************* АДМИНИСТРИРОВАНИЕ *******************************


@dp.message_handler(commands=['help'])
async def help_panel(message: Message) -> None:
    global msg, a
    msg = message
    await message.answer('Here:\n/start - Старт, общий запуск\n/poh - Пнуть Админа\n/ask - Сообщение админу ( /ask <em>your text</em> )"\n/feedback - Прямая связь с автором', parse_mode='html')
  
#------------------------------------------------  

@dp.message_handler(commands=['negritos'])
async def admin_panel(message: Message) -> None:
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
async def mega_sending(message: Message) -> None:
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
async def sending(message: Message) -> None:
    global msg
    msg = message

    try:
        await bot.send_message(message.text[9:20], f"Автор: {message.text[20:]}")
    except Exception as ex:
        print("mega_sending не нормас: ", ex)

#------------------------------------------------  

@dp.message_handler(commands=['ask'])
async def ask(message: Message) -> None:
    lang = db.getting(message.from_user.id, 'language')
    name = message.from_user.first_name
    if message.text[5:] == None:
        try:
            await bot.send_message(ADMIN[0], f'{name} - id: {message.chat.id}, @{message.chat.username}\nMessage: {message.text[5:]}')
        except Exception as ex:
            print("mega_sending не нормас: ", ex)
    else:
        await message.answer(empty_ask[lang])
#------------------------------------------------  

@dp.message_handler(commands=["feedback"])
async def feedback(message: Message) -> None: 

    try:
        if (db.getting(message.chat.id, 'language') == "ru"):
            await message.answer("Говорят, через это меню можно поговорить с автором бота. Точно хочешь? 🙂", reply_markup=kb.fbBRu)
        else: 
            await message.answer("Кажуть, через цей відділ можна поговорити з автотором бота. Точно хочеш? 🙂", reply_markup=kb.fbBUa)

    except Exception as ex:
        print('Ошибка feedback начала: ', ex)

#------------------------------------------------  

@dp.message_handler(commands=['poh'])
async def poh(message: Message):
    lang = db.getting(message.from_user.id, 'language')

    try:
        name = db.getting(message.from_user.id, 'username')
        await bot.send_message(ADMIN[0], f"@{message.chat.username}: {name}, {message.chat.id} тебя пнул :)")
        if lang == 'ru':
            await message.answer('Всё сделано босс. Я его пнул 😀')
        elif lang == 'uk':
            await message.answer('Все зроблено босс. Я його пнув 😀')

    except Exception as ex:
        print("poh не нормас: ", ex)

#------------------------------------------------  

@dp.message_handler(commands=['pizda'])
async def pizda(message: Message):

    try:
        await message.answer(message)
    except Exception as ex:
        print("pizda не нормас: ", ex)

#------------------------------------------------  

if __name__ == '__main__':
    executor.start_polling(dispatcher = dp, skip_updates= True)
from aiogram import Bot, Dispatcher, executor, types
import logging, handlers.uslovie
from config import dp, bot, ADMIN
from querry_db import QuerryDB
from handlers import keyboards as kb, tests as ts, setting as st
from handlers.dialogs import ru, en, uk

# соединение с БД
db = QuerryDB()

# уровень логов
logging.basicConfig(level=logging.INFO)

#№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№ БОТ БОТ БОТ БОТ БОТ №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№


@dp.message_handler(commands=['start'])
async def welcome(message): ################### СТАРТ МЕНЮ ######################
    global msg
    msg = message
    print(message)
    try:
        if(not db.subsex(message.from_user.id)): # Пользователя нет в БД

            name_start = str(message.from_user.first_name)
            language = str(message.from_user.language_code)
            db.add_subs(message.from_user.id) # / Добавление пользователя в БД
            db.adding(message.from_user.id, 'username', name_start)
            

            if language == 'ru': #                                 Если при старте русский язык
                db.adding(message.from_user.id, 'language', 'ru')
                await message.answer("Привет, <b>" + name_start + "</b>! 😉" + ru['hi_start'], parse_mode='html', reply_markup=kb.languageB)

            elif language == 'uk': #                              Если при старте украинский язык
                db.adding(message.from_user.id, 'language', 'uk')
                db.adding(message.from_user.id,'language', language) ######################/ Добавление языка и имени
                await message.answer("Привiт, <b>" + name_start + "</b>! 😉" + uk['hi_start'], parse_mode='html', reply_markup=kb.languageB)

            else:              # Сообщение на англ. что бот не поддерживает их язык
                await message.answer(en["error"], parse_mode='html', reply_markup=kb.languageB)

        else: # Пользователь есть в БД
            global name
            name = db.getting(message.from_user.id, 'username')
            language = db.getting(message.from_user.id, 'language')

            if (language == 'ru'): # Русский
                await message.answer("Привет, <b>" + name + "</b>! Приятно увидеть тебя снова :)", parse_mode='html')
            else:                                                      # Украинский
                await message.answer("Привіт, <b>" + name + "</b>! Приємно побачити тебе знову :)",parse_mode='html')
    except Exception as ex:
        print('Ошибка старт-меню:', ex)

@dp.message_handler(commands=['menu'])
async def toMenu(message): #******************* ГЛАВНОЕ МЕНЮ *********************
    global msg
    msg = message
    try:
        if (db.getting(message.from_user.id, 'language') == "ru"): #            Русский язык
            await message.answer("🔸                <b>Главное меню</b>                🔸\n\nЗдесь ты можешь пользоваться моими функциями.",
            parse_mode='html', reply_markup=kb.board_menu)
                        
        elif (db.getting(message.from_user.id, 'language') == "uk"): #            Украинский язык
            await message.answer("🔸                <b>Головне меню</b>                🔸\n\nТут ти можеш користуватися моїми функціями.",
            parse_mode='html', reply_markup = kb.board_menu)
    except Exception as ex:
        print('Ошибка главного меню: ', ex)


#******************************* КОМАНДЫ НАСТРОЙКИ*******************************

#@dp.message_handler(commands=['hyi'])
async def hyi(message):
    global msg
    msg = message

    try:
        await bot.edit_message_reply_markup(message.from_user.id, message.id)
        await message.answer('Всё сделано босс')
    except Exception as ex:
        print("Tarakota не нормас: ", ex)

@dp.callback_query_handler(text='menu_setting')
async def inline_menu(c):
    if (db.getting(c.message.chat.id, 'gender') == "Male"):
        if (db.getting(c.message.chat.id, 'language') == "ru"): 

            await bot.edit_message_text("⚙️Настройки:", chat_id=c.message.chat.id, message_id=c.message.message_id)
            await bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=kb.setting_button_ru_men)
        else:
            await bot.edit_message_text("Налаштування:", chat_id=c.message.chat.id, message_id=c.message.message_id)
            await bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=kb.setting_button_uk_men)

    elif (db.getting(c.message.chat.id, 'gender') == "Female"):
        if (db.getting(c.message.chat.id, 'language') == "ru"): 

            await bot.edit_message_text("⚙️ Настройки:", chat_id=c.message.chat.id, message_id=c.message.message_id)
            await bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=kb.setting_button_ru_women)
        else:
            await bot.edit_message_text("⚙️ Налаштування:", chat_id=c.message.chat.id, message_id=c.message.message_id)
            await bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=kb.setting_button_uk_women)
    else:
        db.adding(c.message.chat.id, 'gender', "Male")

@dp.callback_query_handler(text='setting_gender_ru')
async def setting_gender_ru(c):
    if (db.getting(c.message.chat.id, 'gender') == "Female"):
        db.adding(c.message.chat.id, 'gender', "Male")
        await inline_menu(c)
    else:
        db.adding(c.message.chat.id, 'gender', "Female")
        await inline_menu(c)

@dp.callback_query_handler(text='setting_gender_uk')
async def setting_gender_uk(c):
    if (db.getting(c.message.chat.id, 'gender') == "Female"):
        db.adding(c.message.chat.id, 'gender', "Male")
        await inline_menu(c)
    else:
        db.adding(c.message.chat.id, 'gender', "Female")
        await inline_menu(c)

@dp.callback_query_handler(text='setting_language_ru')
async def setting_language_ru(c):
    if (db.getting(c.message.chat.id, 'language') == "ru"):
        db.adding(c.message.chat.id, 'language', "uk")
        await inline_menu(c)
    else:
        db.adding(c.message.chat.id, 'language', "ru")
        await inline_menu(c)

@dp.callback_query_handler(text='setting_language_uk')
async def setting_language_uk(c):
    if (db.getting(c.message.chat.id, 'language') == "uk"):
        db.adding(c.message.chat.id, 'language', "ru")
        await inline_menu(c)
    else:
        db.adding(c.message.chat.id, 'language', "uk")
        await inline_menu(c)

#******************************* АДМИНИСТРИРОВАНИЕ *******************************

@dp.message_handler(commands=['help'])
async def help_panel(message):
    global msg
    msg = message
    await message.answer('Here:\n/start - Старт, общий запуск\n/poh - Пнуть Админа\n/ask - Сообщение админу ( /ask text )"\n/feedback - Связь с автором')
  

@dp.message_handler(commands=['negritos'])
async def admin_panel(message):
    global msg
    msg = message
    try:
        if message.from_user.id in ADMIN:
            await message.answer('Hi, my lord.')
            await message.answer('Here:\n/start - Старт, общий запуск\n/terakota - Тестирование функций\n/hyi - Пнуть Саню\n/sending - (id) (text)\n/mega_sending - (text)')
        else:
            await message.answer('Кудааа мы лезем? Не положено, давай в меню.')
            await toMenu(message)
    except Exception as ex:
        print('Ошибка панели админа: ', ex)

@dp.message_handler(commands=['mega_sending'])
async def mega_sending(message):
    global msg
    msg = message
    try:
        a = db.get_all('user_id')
        for i in a:
            await bot.send_message(*i, message.from_chat.text[13:])
    except Exception as ex:
        print("mega_sending не нормас: ", ex)

@dp.message_handler(commands=['sending'])
async def sending(message):
    global msg
    msg = message

    try:
        await bot.send_message(message.text[9:20], f"Автор: {message.text[20:]}")
    except Exception as ex:
        print("mega_sending не нормас: ", ex)

@dp.message_handler(commands=['ask'])
async def ask(message):
    global msg, name
    msg = message
    name = message.from_user.first_name
    try:
        await bot.send_message(ADMIN[0], f'{name} - id: {message.from_user.id}, @{message.from_user.username}\nMessage: {message.text[5:]}')
    except Exception as ex:
        print("mega_sending не нормас: ", ex)

@dp.message_handler(commands=["feedback"])
async def feedback(message): 
    global msg
    msg = message
    try:
        if (db.getting(message.from_user.id, 'language') == "ru"):
            await message.answer("Говорят, через это меню можно поговорить с автором бота. Точно хочешь? 🙂", reply_markup=kb.fbBRu)
        else: 
            await message.answer("Кажуть, через цей відділ можна поговорити з автотором бота. Точно хочеш? 🙂", reply_markup=kb.fbBUa)

    except Exception as ex:
        print('Ошибка feedback начала: ', ex)

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

@dp.message_handler(commands=['pizda'])
async def pizda(message):
    global msg
    msg = message
    try:
        pass
    except Exception as ex:
        print("pizda не нормас: ", ex)

@dp.message_handler(commands=['restart'])
async def restart(message):
    global msg
    msg = message
    print(type(msg))
    #await message.answer("Обновление бота..")

#******************************** CallBack Inline All*********************************

@dp.callback_query_handler(text="fb_yes")
async def inline_fb_yes(call:types.CallbackQuery):

    try:
        user_name = call.message.chat.username
        name = call.message.chat.first_name
        await bot.send_message(ADMIN[0], f"@{user_name}: {name}, хочет поговорить :)")
        await bot.send_message(call.message.chat.id, """Хорошо! Когда нибудь с тобой свяжутся 😉 (или нет)\n
        Ты можешь просто написать ему: @alexnerw\nА пока что перенаправляю в тебя меню:""", parse_mode='html', reply_markup=None)
        await toMenu(msg)
    except Exception as ex:
        print("""Отчёт об ошибке:\n
        fb_yes чёт подвело: """, ex)

@dp.callback_query_handler(text="fb_no")
async def inline_fb_no(call:types.CallbackQuery):
    try:

        await bot.send_message(call.message.chat.id, "Хорошо! Нет так нет :)", parse_mode='html', reply_markup=None)
        await toMenu(msg)
    except Exception as ex:
        print("""Отчёт об ошибке:\n
        fb_no чёт подвело: """, ex)

#******************************** CallBack Inline Menu *********************************
   
@dp.callback_query_handler(text="menu_test")
async def inline_menu_tests(call:types.CallbackQuery):
    try:
        #await bot.answer_callback_query(call.message.chat.id)
        await ts.tests(call.message)
    except Exception as ex:
        print("Шо то не так с call_menu_test: ", ex)

@dp.callback_query_handler(text="menu_setting")
async def inline_menu_setting(call:types.CallbackQuery):
    try:
        await st.setting(call.message)
    except Exception as ex:
        print("Шо то не так с call_menu_setting:", ex)

@dp.callback_query_handler(text="menu_calendar")
async def inline_menu_сalendar(call:types.CallbackQuery):
    try:
        await call.message.answer("Нихера пока-что")
    except Exception as ex:
        print("Шо то не так с call_menu_сalendar: ", ex)

@dp.callback_query_handler(text="menu_game")
async def inline_menu_game(call:types.CallbackQuery):
    try:
        await call.message.answer("Тут нихера нет")
    except Exception as ex:
        print("Шо то не так с call_menu_game: ", ex)


def register_uslovie(dp : Dispatcher):
    dp.register_message_handler(welcome, content_types=['command'])
    #dp.register_message_handler(input_name, content_types=['man'])

if __name__ == '__main__':
    #************************************ ЗАПУСК *************************************
    executor.start_polling(dp, skip_updates=True)

from aiogram import Bot, Dispatcher, executor, types
import keyboards as kb, tests as ts, setting as st
from config import dp, bot, ADMIN
from querry_db import db
from dialogs import *
import menu


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

            await bot.edit_message_text("⚙️ Настройки:", c.message.chat.id, c.message.message_id)
            await bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id, reply_markup=kb.setting_button_ru_men)
        else:
            await bot.edit_message_text("⚙️ Налаштування:", c.message.chat.id, c.message.message_id)
            await bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id, reply_markup=kb.setting_button_uk_men)

    elif (db.getting(c.message.chat.id, 'gender') == "Female"):
        if (db.getting(c.message.chat.id, 'language') == "ru"): 

            await bot.edit_message_text("⚙️ Настройки:", c.message.chat.id, c.message.message_id)
            await bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id, reply_markup = kb.setting_button_ru_women)
        else:
            await bot.edit_message_text("⚙️ Налаштування:", c.message.chat.id, c.message.message_id)
            await bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id, reply_markup = kb.setting_button_uk_women)
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

@dp.callback_query_handler(text="fb_yes")
async def inline_fb_yes(call:types.CallbackQuery):

    try:
        user_name = call.message.chat.username
        name = call.message.chat.first_name
        await bot.send_message(ADMIN[0], f"@{user_name}: {name}, хочет поговорить :)")
        await bot.send_message(call.message.chat.id, """Хорошо! Когда нибудь с тобой свяжутся 😉 (или нет)\n
        Ты можешь просто написать ему: @alexnerw\nА пока что перенаправляю в тебя меню:""", parse_mode='html', reply_markup=None)
        await menu.toMenu(msg)
    except Exception as ex:
        print("""Отчёт об ошибке:\n
        fb_yes чёт подвело: """, ex)

@dp.callback_query_handler(text="fb_no")
async def inline_fb_no(call:types.CallbackQuery):
    try:

        await bot.send_message(call.message.chat.id, "Хорошо! Нет так нет :)", parse_mode='html', reply_markup=None)
        await menu.toMenu(msg)
    except Exception as ex:
        print("""Отчёт об ошибке:\n
        fb_no чёт подвело: """, ex)
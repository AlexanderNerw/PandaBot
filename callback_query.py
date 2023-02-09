import handlers.keyboards as kb, handlers.setting as st, handlers.tests as ts
from aiogram import Bot, Dispatcher, executor, types
from handlers.config import dp, bot, ADMIN, storage
from handlers.querry_db import db
from handlers.dialogs import *
import menu

@dp.callback_query_handler(text='menu_setting')
async def inline_menu(c):
    try:
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

    except Exception as ex:
        await bot.send_message(ADMIN[1], 'callback_query.py [INFO] Неполадки с inline_menu: ', ex)
        print("callback_query.py [INFO] Неполадки с inline_menu: ", ex)

@dp.callback_query_handler(text='menu_setting_back')
async def inline_menu_back(c):
    try:
        if (db.getting(c.message.chat.id, 'language') == "ru"): #            Русский язык
            await bot.edit_message_text("🔸                <b>Главное меню</b>                🔸\n\nЗдесь ты можешь пользоваться моими функциями.",
            c.message.chat.id, c.message.message_id, parse_mode='html', reply_markup = kb.board_menu)
                        
        elif (db.getting(c.message.chat.id, 'language') == "uk"): #            Украинский язык
            await bot.edit_message_text("🔸                <b>Головне меню</b>                🔸\n\nТут ти можеш користуватися моїми функціями.",
            c.message.chat.id, c.message.message_id, parse_mode='html', reply_markup = kb.board_menu)
    except Exception as ex:
        await bot.send_message(ADMIN[1], 'callback_query.py [INFO] Неполадки с inline_menu_back: ', ex)
        print("callback_query.py [INFO] Неполадки с inline_menu_back: ", ex)

@dp.callback_query_handler(text='setting_gender_ru')
async def setting_gender_ru(c):

    try:
        if (db.getting(c.message.chat.id, 'gender') == "Female"):
            db.adding(c.message.chat.id, 'gender', "Male")
            await inline_menu(c)
        else:
            db.adding(c.message.chat.id, 'gender', "Female")
            await inline_menu(c)

    except Exception as ex:
        await bot.send_message(ADMIN[1], 'callback_query.py [INFO] Неполадки с setting_gender_ru: ', ex)
        print("callback_query.py [INFO] Неполадки с setting_gender_ru: ", ex)

@dp.callback_query_handler(text='setting_gender_uk')
async def setting_gender_uk(c):
    try:
        if (db.getting(c.message.chat.id, 'gender') == "Female"):
            db.adding(c.message.chat.id, 'gender', "Male")
            await inline_menu(c)
        else:
            db.adding(c.message.chat.id, 'gender', "Female")
            await inline_menu(c)

    except Exception as ex:
        await bot.send_message(ADMIN[1], 'callback_query.py [INFO] Неполадки с setting_gender_uk: ', ex)
        print("callback_query.py [INFO] Неполадки с setting_gender_uk: ", ex)

@dp.callback_query_handler(text='setting_language_ru')
async def setting_language_ru(c):
    try:
        if (db.getting(c.message.chat.id, 'language') == "ru"):
            db.adding(c.message.chat.id, 'language', "uk")
            await inline_menu(c)
        else:
            db.adding(c.message.chat.id, 'language', "ru")
            await inline_menu(c)

    except Exception as ex:
        await bot.send_message(ADMIN[1], 'callback_query.py [INFO] Неполадки с setting_language_ru: ', ex)
        print("callback_query.py [INFO] Неполадки с setting_language_ru: ", ex)

@dp.callback_query_handler(text='setting_language_uk')
async def setting_language_uk(c):
    try:
        if (db.getting(c.message.chat.id, 'language') == "uk"):
            db.adding(c.message.chat.id, 'language', "ru")
            await inline_menu(c)
        else:
            db.adding(c.message.chat.id, 'language', "uk")
            await inline_menu(c)

    except Exception as ex:
        await bot.send_message(ADMIN[1], 'callback_query.py [INFO] Неполадки с setting_language_uk: ', ex)
        print("callback_query.py [INFO] Неполадки с setting_language_uk: ", ex)

@dp.callback_query_handler(text="menu_test")
async def inline_menu_tests(call:types.CallbackQuery):
    try:
        await ts.tests(call.message)
    except Exception as ex:
        await bot.send_message(ADMIN[1], 'callback_query.py [INFO] Неполадки с inline_menu_tests: ', ex)
        print("callback_query.py [INFO] Неполадки с inline_menu_tests: ", ex)

@dp.callback_query_handler(text="menu_setting")
async def inline_menu_setting(call:types.CallbackQuery):
    try:
        await st.setting(call.message)
    except Exception as ex:
        await bot.send_message(ADMIN[1], 'callback_query.py [INFO] Неполадки с inline_menu_setting: ', ex)
        print("callback_query.py [INFO] Неполадки с inline_menu_setting: ", ex)

@dp.callback_query_handler(text="menu_calendar")
async def inline_menu_сalendar(call:types.CallbackQuery):
    try:
        await call.message.answer("Нихера пока-что")
        import handlers.tests as ts
    except Exception as ex:
        await bot.send_message(ADMIN[1], 'callback_query.py [INFO] Неполадки с inline_menu_сalendar: ', ex)
        print("callback_query.py [INFO] Неполадки с inline_menu_сalendar: ", ex)

@dp.callback_query_handler(text="menu_game")
async def inline_menu_game(call:types.CallbackQuery):
    try:
        await call.message.answer("Тут нихера нет")
    except Exception as ex:
        await bot.send_message(ADMIN[1], 'callback_query.py [INFO] Неполадки с inline_menu_game: ', ex)
        print("callback_query.py [INFO] Неполадки с inline_menu_game: ", ex)

@dp.callback_query_handler(text="fb_yes")
async def inline_fb_yes(call:types.CallbackQuery):

    try:
        user_name = call.message.chat.username
        name = call.message.chat.first_name
        await bot.send_message(ADMIN[0], f"@{user_name}: {name}, хочет поговорить :)")
        await bot.send_message(call.message.chat.id, """Хорошо! Когда нибудь с тобой свяжутся 😉 (или нет)\n
        Ты можешь просто написать ему: @alexnerw\nА пока что перенаправляю в тебя меню:""", parse_mode='html', reply_markup=None)
        await menu.toMenu(call.message)
    except Exception as ex:
        await bot.send_message(ADMIN[1], 'callback_query.py [INFO] Неполадки с inline_fb_yes: ', ex)
        print("callback_query.py [INFO] Неполадки с inline_fb_yes: ", ex)

@dp.callback_query_handler(text="fb_no")
async def inline_fb_no(call:types.CallbackQuery):
    try:

        await bot.send_message(call.message.chat.id, "Хорошо! Нет так нет :)", parse_mode='html', reply_markup=None)
        await menu.toMenu(call.message)
    except Exception as ex:
        await bot.send_message(ADMIN[1], 'callback_query.py [INFO] Неполадки с inline_fb_no: ', ex)
        print("callback_query.py [INFO] Неполадки с inline_fb_no: ", ex)
import handlers.setting as st, handlers.tests as ts, menu
from support.querry_db import db
from support.config import *
from support.dialogs import *
from support.keyboards import *

#========================================================================================
@dp.callback_query_handler(CHAT_PRIVATE, text="toMenuSafe")
async def inline_to_menu_safe(call: CallbackQuery):
    try: await menu.toMenu(call.message), await call.answer()
    except Exception as ex: await exceptions("callback_query.py", 'inline_to_menu_safe', ex)

#========================================================================================
@dp.callback_query_handler(CHAT_PRIVATE, text="menu_test")
async def inline_menu_tests(call: CallbackQuery):
    try: await ts.tests(call.message.chat.id, call.message.message_id), await call.answer()
    except Exception as ex: await exceptions("callback_query.py", 'inline_menu_tests', ex)

#========================================================================================
@dp.callback_query_handler(CHAT_PRIVATE, text="menu_calendar")
async def inline_menu_сalendar(call: CallbackQuery):
    try: await call.message.answer("Нихера пока-что"), await call.answer()
    except Exception as ex: await exceptions("callback_query.py", 'inline_menu_сalendar', ex)

#========================================================================================
@dp.callback_query_handler(CHAT_PRIVATE, text="menu_game")
async def inline_menu_game(call: CallbackQuery):
    try: await call.message.answer("Пока ничо нет, можешь наехать на автора. Ну а чо он."), await call.answer()
    except Exception as ex: await exceptions("callback_query.py", 'inline_menu_game', ex)

#========================================================================================
@dp.callback_query_handler(CHAT_PRIVATE, text="fb_yes")
async def inline_fb_yes(call: CallbackQuery):
    try:
        await bot.send_message(ADMIN[1], f"@{call.message.chat.username}: {call.message.chat.first_name}, хочет поговорить :)"), await call.answer()
        await bot.send_message(call.message.chat.id, general_text[f"{db.getting(call.message.chat.id, 'language')}_feedback_ok"], parse_mode='html')

    except Exception as ex: await exceptions("callback_query.py", 'inline_fb_yes', ex)

#========================================================================================
@dp.callback_query_handler(CHAT_PRIVATE, text="fb_no")
async def inline_fb_no(call: CallbackQuery):
    try:
        await bot.send_message(call.message.chat.id, general_text[f"{db.getting(call.message.chat.id, 'language')}_ask_admin_no"], parse_mode='html', reply_markup=None)
        await menu.toMenu(call.message), await call.answer()
        
    except Exception as ex: await exceptions("callback_query.py", 'inline_fb_no', ex)
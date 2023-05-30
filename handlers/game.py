from support.querry_db import db
from support.config import dp, CallbackQuery, CHAT_PRIVATE, exceptions
from handlers.menu import toMenu


@dp.callback_query_handler(CHAT_PRIVATE, text="menu_game")
async def inline_menu_game(call: CallbackQuery):
    try: await call.message.answer("Пока ничо нет, можешь наехать на автора. Ну а чо он."), await call.answer()
    except Exception as ex: await exceptions("callback_query.py", 'inline_menu_game', ex)
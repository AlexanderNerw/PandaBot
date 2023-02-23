import handlers.setting as st, handlers.tests as ts
from handlers.support.importing import *


@dp.callback_query_handler(text="menu_test")
async def inline_menu_tests(call: CallbackQuery):
    try:
        await ts.tests(call.message.chat.id, call.message.message_id)
    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с st.inline_menu_setting_tests: {ex}')
        print(f"callback_query.py [INFO] Неполадки с st.inline_menu_setting_tests: {ex}")

@dp.callback_query_handler(text="menu_calendar")
async def inline_menu_сalendar(call: CallbackQuery):
    try:
        await call.message.answer("Нихера пока-что")
        import handlers.tests as ts
    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с st.inline_menu_setting_сalendar: {ex}')
        print(f"callback_query.py [INFO] Неполадки с st.inline_menu_setting_сalendar: {ex}")

@dp.callback_query_handler(text="menu_game")
async def inline_menu_game(call: CallbackQuery):
    try:
        await call.message.answer("Тут нихера нет")
    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с st.inline_menu_setting_game: {ex}')
        print(f"callback_query.py [INFO] Неполадки с st.inline_menu_setting_game: {ex}")

@dp.callback_query_handler(text="fb_yes")
async def inline_fb_yes(call: CallbackQuery):

    try:
        lang = db.getting(call.message.chat.id, 'language')
        user_name = call.message.chat.username
        name = call.message.chat.first_name
        await bot.send_message(ADMIN[0], f"@{user_name}: {name}, хочет поговорить :)")
        await bot.send_message(call.message.chat.id, f"{general_text[f'{lang}_feedback_yes']}", parse_mode='html')
        await menu.toMenu(call.message)
    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с inline_fb_yes: {ex}')
        print(f"callback_query.py [INFO] Неполадки с inline_fb_yes: {ex}")

@dp.callback_query_handler(text="fb_no")
async def inline_fb_no(call: CallbackQuery):
    try:
        lang = db.getting(call.message.chat.id, 'language')
        await bot.send_message(call.message.chat.id, f"{general_text[f'{lang}_ask_admin_no']}", parse_mode='html', reply_markup=None)
        await menu.toMenu(call.message)
    except Exception as ex:
        await bot.send_message(ADMIN[1], f'callback_query.py [INFO] Неполадки с inline_fb_no: {ex}')
        print(f"callback_query.py [INFO] Неполадки с inline_fb_no: {ex}")
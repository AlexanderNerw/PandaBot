from support.config import CHAT_PRIVATE, ADMIN, bot, dp, feedback_button, exceptions
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from support.dialogs import general_text
from support.querry_db import db
from handlers.menu import toMenu


################################################# - FEEDBACK and POH - ###################################

@dp.message_handler(CHAT_PRIVATE, commands=["feedback"])                                                ## ОБРАТНАЯ СВЯЗЬ -> callback_querry.py (fb_yes, fb_no)
async def feedback(message: Message) -> None:
    try:
        lang = db.getting(message.chat.id, 'language')
        await message.answer(general_text[f'{lang}_feedback_yes'], reply_markup=feedback_button[lang])

    except Exception as ex: await exceptions("feedback", 'feedback', ex)

#------------------------------------------------------------------------------
@dp.message_handler(CHAT_PRIVATE, commands=['poh'])                                                     ## ПРОСТО ПНУТЬ АДМИНА
async def poh(message: Message):
    try:
        lang = db.getting(message.from_user.id, 'language')
        await bot.send_message(ADMIN, f"@{message.chat.username}: {db.getting(message.from_user.id, 'username')}, {message.chat.id} тебя пнул :)")

        if lang == 'uk':    await message.answer('Все зроблено босс. Я його пнув 😀')
        else:               await message.answer('Всё сделано босс. Я его пнул 😀')

    except Exception as ex: await exceptions("feedback", 'poh', ex)



#################################################### - ASK from USER to ADMIN - ##########################
class AskAdmin(StatesGroup):
    ask = State()

@dp.callback_query_handler(CHAT_PRIVATE, text='go_back', state=AskAdmin)                                ## ОТМЕНА ВОПРОСА АДМИНУ
async def ask_cancel(call: CallbackQuery, state: FSMContext) -> None:
    try:

        lang = db.getting(call.message.from_user.id, 'language')
        await bot.send_message(call.message.chat.id, general_text[f'{lang}_ask_admin_no'])
        await state.reset_data()
        await state.finish()
        await toMenu(call.message)

    except Exception as ex: await exceptions("main.py", 'ask_cancel', ex)

#------------------------------------------------------------------------------
@dp.message_handler(CHAT_PRIVATE, commands=['ask'])                                                     ## ЗАДАТЬ ВОПРОС АДМИНУ
async def ask_user(message: Message) -> None:
    try:
        lang = db.getting(message.from_user.id, 'language')
        name = message.from_user.first_name

        if (message.text).strip() != '/ask':
            await bot.send_message(ADMIN, f'{name} - id: {message.chat.id}, @{message.chat.username}\nMessage: {message.text[5:]}')
            await bot.send_message(message.chat.id, general_text[f'{lang}_send_ask'])
        else:
            await bot.send_message(message.chat.id, general_text[f'{lang}_empty_ask'],
                                   reply_markup=InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Назад', callback_data='go_back')))
            await AskAdmin.ask.set()

    except Exception as ex: await exceptions("main.py", 'ask_user', ex)

#------------------------------------------------------------------------------
@dp.message_handler(CHAT_PRIVATE, content_types=['text'], state=AskAdmin.ask)                           ## ОТПРАВКА ASK 
async def ask_user_text(message: Message, state: FSMContext) -> None:
    try:
        lang = db.getting(message.from_user.id, 'language')
        name = message.from_user.first_name
        await bot.send_message(ADMIN, f'{message.from_user.first_name} - id: {message.chat.id}, @{message.chat.username}\nMessage: {message.text}')
        await bot.send_message(message.chat.id, f"{general_text[f'{lang}_send_ask']}")
        await state.reset_data()
        await state.finish()
        await toMenu(message)

    except Exception as ex: await exceptions("main.py", 'ask_user_text', ex)



##################################################### - YES or NO  FEEDBACK - ############################
@dp.callback_query_handler(CHAT_PRIVATE, text="fb_yes")
async def inline_fb_yes(call: CallbackQuery):
    try:
        await bot.send_message(ADMIN, f"@{call.message.chat.username}: {call.message.chat.first_name}, хочет поговорить :)"), await call.answer()
        await bot.send_message(call.message.chat.id, general_text[f"{db.getting(call.message.chat.id, 'language')}_feedback_ok"], parse_mode='html')

    except Exception as ex: await exceptions("feedback.py", 'inline_fb_yes', ex)

#========================================================================================
@dp.callback_query_handler(CHAT_PRIVATE, text="fb_no")
async def inline_fb_no(call: CallbackQuery):
    try:
        await bot.send_message(call.message.chat.id, general_text[f"{db.getting(call.message.chat.id, 'language')}_ask_admin_no"], parse_mode='html', reply_markup=None)
        await toMenu(call.message), await call.answer()
        
    except Exception as ex: await exceptions("feedback.py", 'inline_fb_no', ex)
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from support.config import dp, bot, exceptions, CHAT_PRIVATE
from support.querry_db import db
from handlers.menu import toMenu


#===========================================================#
@dp.message_handler(CHAT_PRIVATE, content_types=['text'])
async def reaction(message: Message):

    text_user = str(message.text).lower()

    try:
        # РАЗГОВОР =========================================            
        
            if text_user in ["как дела?", "как настроение?"]: await bot.send_message(message.chat.id, 'Всё отлично, спасибо :)')
            #---------------------------------------------------
            #elif "анекдот" in text_user: await bot.send_message(message.chat.id, general_text[f"{lang}_joke_for_like"] + all_jokes[random.randint(0,888)], parse_mode='html')
            #---------------------------------------------------
            elif text_user in ["меню", "menu"]: await toMenu(message)

            elif message.text in ["Я парень 🧔🏽‍♂️", "Я девушка 👱🏼‍♀️", "Я хлопець 🧔🏽‍♂️", "Я дівчина 👱🏼‍♀️", 'Русский', 'Українська 🇺🇦']:
                if (not db.user_in_database(message.chat.id)) or (not db.user_online(message.chat.id)):
                    await bot.send_message(message.chat.id, "Похоже возникли некоторые неполадки.. ⤵️", reply_markup=
                                        InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
                                        InlineKeyboardButton("Регистрация 🔸" if message.from_user.language_code == 'ru' else "Регiстрацiя 🔸", callback_data='Регистрация 🔸')))
            # ПРИМОЧКИ ====================================
            else: await bot.send_message(message.chat.id, 'Я не знаю что ответить :(') 

    except Exception as ex: await exceptions("reactions.py", 'reaction', ex)

from aiogram import Bot, Dispatcher, executor, types
from menu import toMenu
from handlers.config import dp, bot, ADMIN
from handlers.querry_db import db
import handlers.keyboards as kb


@dp.message_handler(content_types=['name'])
async def input_name(message):
    if (db.getting(message.from_user.id, 'language') == 'ru'):
        await message.answer("Как мне тебя называть?")

        await message.answer("Як мені до тебе звертатись?")

@dp.message_handler(content_types=['text'])
async def reaction(message):

# РУССКОЕ #############################################################################################################################################
    
    if (db.getting(message.from_user.id, 'language') == 'ru'):

        ## РЕГИСТРАЦИЯ ******************************************************************

            if message.text == "Как дела?":
                await message.answer('Всё отлично, а ты как?')
            elif message.text == "Как настроение?":
                await message.answer('Потрясающе!')

            elif message.text == "Тесты":
                await message.answer('Вот список доступных тестов:', reply_markup=types.ReplyKeyboardRemove())


         # ЯЗЫК ******************************************************************************************

            elif message.text == "Русский":
                await message.answer('Хорошо!', reply_markup=types.ReplyKeyboardRemove())
                db.adding(message.from_user.id, 'language', 'ru')              
                await toMenu(message)

            elif message.text == "Українська":
                await message.answer('Добре! Ви змінили мову на українську.', reply_markup=types.ReplyKeyboardRemove())
                db.adding(message.from_user.id, 'language', 'uk')
                await toMenu(message)

         # ПОЛ ******************************************************************************************

            elif message.text == "Я парень" or message.text == "Я парень 🧔🏽‍♂️":
                if (db.getting(message.from_user.id, 'gender') == 'Male'):
                    await message.answer('Я знаю :)', reply_markup=types.ReplyKeyboardRemove())
                    await toMenu(message)
                elif (db.getting(message.from_user.id, 'gender') == 'Female'):
                    db.adding(message.from_user.id, 'gender', 'Male')
                    await message.answer('Хорошо! Перенаправляю тебя в главное меню.', reply_markup=types.ReplyKeyboardRemove())
                    await toMenu(message)

            elif message.text == "Я девушка" or message.text == "Я девушка 👱🏼‍♀️":
                if (db.getting(message.from_user.id, 'gender') == 'Female'):
                    await message.answer('Я знаю :)', reply_markup=types.ReplyKeyboardRemove())
                    await toMenu(message)
                elif (db.getting(message.from_user.id, 'gender') == 'Male'):
                    db.adding(message.from_user.id, 'gender', 'Female')
                    await message.answer('Хорошо! Перенаправляю тебя в главное меню.', reply_markup=types.ReplyKeyboardRemove())
                    await toMenu(message)

         # ПРИМОЧКИ ****************************************************************************************

            else:
                await message.answer('Я не знаю что ответить :(') 


### УКРАИНА ###########################################################################################################################################

    else: # Если украинский

        if(db.getting(message.from_user.id, 'gender') == None):


            if message.text == "Як справи?":
                await message.answer('Все добре, а ти як?')

            elif message.text == "Як настрій?":
                await message.answer('Супер!')

            elif message.text == "Тести":
                await message.answer('Ось список доступних тестів:', reply_markup=types.ReplyKeyboardRemove())

         # ЯЗЫК *******************************************************************************************************

            elif message.text == "Русский":
                await message.answer('Хорошо! Вы поменяли язык на русский.', reply_markup=types.ReplyKeyboardRemove())
                db.adding(message.from_user.id, 'language', 'ru')
                await toMenu(message)

            elif message.text == "Українська":
                await message.answer('Ви вже використовуєте бота на українській.', reply_markup=types.ReplyKeyboardRemove())
                db.adding(message.from_user.id, 'language', 'uk')       
                await toMenu(message)


         # ПОЛ *******************************************************************************************************

            elif message.text == "Я хлопець" or message.text == "Я хлопець 🧔🏽‍♂️":
                if (db.getting(message.from_user.id, 'gender') == 'Male'):
                    await message.answer('Я знаю :)', reply_markup=types.ReplyKeyboardRemove())
                    await toMenu(message)
                elif (db.getting(message.from_user.id, 'gender') == 'Female'):
                    db.adding(message.from_user.id, 'gender', 'Male')
                    await message.answer('Добре! Перенаправляю тебе на головне меню.', reply_markup=types.ReplyKeyboardRemove())
                    await toMenu(message)

            elif message.text == "Я дівчина" or message.text == 'Я дівчина 👱🏼‍♀️':
                if (db.getting(message.from_user.id, 'gender') == 'Female'):
                    await message.answer('Я знаю :)', reply_markup=types.ReplyKeyboardRemove())
                    await toMenu(message)
                elif (db.getting(message.from_user.id, 'gender') == 'Male'):
                    db.adding(message.from_user.id, 'gender', 'Female')
                    await message.answer('Добре! Перенаправляю тебе на головне меню.', reply_markup=types.ReplyKeyboardRemove())
                    await toMenu(message)

            else:
                await message.answer('Я не знаю що відповісти :(')

def register_uslovie(dp : Dispatcher):
    dp.register_message_handler(reaction, content_types=['text'])
    dp.register_message_handler(input_name, content_types=['man'])
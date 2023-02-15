from handlers.support.importing import *



@dp.message_handler(commands=['name'])
async def input_name(message):
    if (db.getting(message.from_user.id, 'language') == 'ru'):
        await message.answer("Как мне тебя называть?")
    else:
        await message.answer("Як мені до тебе звертатись?")

#@dp.message_handler(ChatTypeFilter(chat_type=ChatType.PRIVATE), content_types=['text'])
async def reaction(message):

    text_user = (message.text).lower()
    lang = db.getting(message.from_user.id, 'language')

    try:
        if lang in ['ru', 'uk']:

            # РАЗГОВОР ******************************************************************

            if text_user in ["как дела?", "как настроение?"]:
                await message.answer('Всё отлично, а ты как?')

            elif text_user in ["меню", "menu"]:
                await menu.toMenu(message)

            # ЯЗЫК ******************************************************************************************

            elif text_user in ['русский', 'українська']:
                lang_user = 'ru' if text_user == "русский" else 'uk'
                if lang != lang_user:
                    await bot.send_message(message.chat.id, reverse_info[f'{lang_user}_lang'])
                    db.adding(message.from_user.id, 'language', lang_user)
                    await menu.toMenu(message) 
                else:
                    await bot.send_message(message.chat.id, 'Я знаю :)')    

            # ПОЛ ******************************************************************************************

            elif text_user in ["я парень", "я девушка"]:
                gender = db.getting(message.from_user.id, 'gender')
                gender_user = 'male' if text_user == "я парень" else 'female'
                if gender != gender_user:
                    await bot.send_message(message.chat.id, reverse_info[f'{lang_user}_{gender_user}_lang'])
                    db.adding(message.from_user.id, 'gender', gender)
                    await menu.toMenu(message)
                else:
                    await bot.send_message(message.chat.id, 'Я знаю :)')

            # ПРИМОЧКИ ****************************************************************************************

            else:
                await message.answer('Я не знаю что ответить :(') 

        else:
            db.adding(message.from_user.id, 'language', 'ru')
            await reaction(message)

    except Exception as ex:
        await bot.send_message(ADMIN[1], 'uslovie.py [INFO] Неполадки в reaction: ', ex)
        print('uslovie.py [INFO] Неполадки в reaction: ', ex)

### УКРАИНА ###########################################################################################################################################

    #else: 

        # db.adding(message.from_user.id, 'language', 'ru')
        # await reaction(message)


        # if message.text == "Як справи?":
        #     await message.answer('Все добре, а ти як?')

        # elif message.text == "Як настрій?":
        #     await message.answer('Супер!')

        # elif message.text == "Тести":
        #     await message.answer('Ось список доступних тестів:', reply_markup=ReplyKeyboardRemove())

        # # ЯЗЫК *******************************************************************************************************

        # elif message.text == "Русский":
        #     await message.answer('Хорошо! Вы поменяли язык на русский.', reply_markup=ReplyKeyboardRemove())
        #     db.adding(message.from_user.id, 'language', 'ru')
        #     await toMenu(message)

        # elif message.text == "Українська":
        #     await message.answer('Ви вже використовуєте бота на українській.', reply_markup=ReplyKeyboardRemove())
        #     db.adding(message.from_user.id, 'language', 'uk')       
        #     await toMenu(message)


        #  # ПОЛ *******************************************************************************************************

        # elif message.text == "Я хлопець" or message.text == "Я хлопець 🧔🏽‍♂️":
        #     if (db.getting(message.from_user.id, 'gender') == 'Male'):
        #         await message.answer('Я знаю :)', reply_markup=ReplyKeyboardRemove())
        #         await toMenu(message)
        #     elif (db.getting(message.from_user.id, 'gender') == 'Female'):
        #         db.adding(message.from_user.id, 'gender', 'Male')
        #         await message.answer('Добре! Перенаправляю тебе на головне меню.', reply_markup=ReplyKeyboardRemove())
        #         await toMenu(message)

        # elif message.text == "Я дівчина" or message.text == 'Я дівчина 👱🏼‍♀️':
        #     if (db.getting(message.from_user.id, 'gender') == 'Female'):
        #         await message.answer('Я знаю :)', reply_markup=ReplyKeyboardRemove())
        #         await toMenu(message)
        #     elif (db.getting(message.from_user.id, 'gender') == 'Male'):
        #         db.adding(message.from_user.id, 'gender', 'Female')
        #         await message.answer('Добре! Перенаправляю тебе на головне меню.', reply_markup=ReplyKeyboardRemove())
        #         await toMenu(message)

        # else:
        #     await message.answer('Я не знаю що відповісти :(')

# def register_uslovie(dp : Dispatcher):
#     dp.register_message_handler(reaction, content_types=['text'])
#     dp.register_message_handler(input_name, content_types=['man'])
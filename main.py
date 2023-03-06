import asyncio, handlers.sign_up, handlers.callback_query
from aiogram.dispatcher.filters.builtin import CommandHelp
from handlers.support.importing import *
from aiogram import executor

# АДМИНИСТРИРОВАНИЕ ############################ - ADMIN PANEL and HELP PANEL #########################################################

@dp.message_handler(CHAT_PRIVATE, CommandHelp())                          ## ПАНЕЛЬ ПОМОЩИ ЮЗЕРУ
async def help_panel(message: Message) -> None:

    if (db.user_in_database(message.chat.id)):
        lang = db.getting(message.chat.id, 'language')
        await message.answer(general_text[f'{lang}_help_menu'], parse_mode='html')
    else:
        await message.answer('Сначала зарегистрируйся: 🙂'), await handlers.sign_up.start(message, FSMContext)
#------------------------------------------------------------------------------
@dp.message_handler(CHAT_PRIVATE, commands=['negr'])                                                    ## ПАНЕЛЬ ПОМОЩИ АДМИНУ
async def admin_panel(message: Message) -> None:
    print(message)
    try:
        if message.from_user.id in ADMIN:
            await message.answer('Hi, my lord. 🤴')
            await message.answer('Here:\n/start - Старт, общий запуск\n/cucumber - Тестирование функций\n/poh - Пнуть Админа\n/send - СообщениЕ Пользователю\n/mega_send - СообщениЯ Пользовалелям')
        else:
            await message.answer('Кудааа мы лезем? Не положено, давай в меню.')
            await menu.toMenu(message)
    except Exception as ex:
        await bot.send_message(ADMIN[1], f'main.py [INFO] Неполадки в admin_panel: {ex}')
        print(f'main.py [INFO] Неполадки в admin_panel: {ex}')

################################################### - ASK from ADMIN to USER ######################################
class TextToSend(StatesGroup):
    id_user = State()
    photo_num = State()
    photo1 = State()
    photo2 = State()
    photo3 = State()
    photo4 = State()
    photo5 = State()
    photo6 = State()
    photo7 = State()
    photo8 = State()
    photo9 = State()
    photo10 = State()
    LANG = State()
    TEXT = State()
    READY = State()

@dp.message_handler(CHAT_PRIVATE, commands=['cancel'], state=TextToSend)                                ## ОТМЕНА SEND и MEGASEND
async def send_cancel(message: Message, state: FSMContext) -> None:

    try:
        await bot.send_message(message.chat.id, 'TextToSend отменено.')
        await state.reset_data()
        await state.finish()

    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки в ask_cancel: {ex}")
        print(f"main.py [INFO] Неполадки в ask_cancel: {ex}")
#------------------------------------------------------------------------------
@dp.message_handler(CHAT_PRIVATE, commands=['mega_send'])                                               ## ГЛОБАЛЬНАЯ РАССЫЛКА СООБЩЕНИЙ
async def mega_send(message: Message, state: FSMContext) -> None:
    if message.from_user.id in ADMIN:

        try:
            await TextToSend.TEXT.set()
            await bot.send_message(message.chat.id, f"Send me text or photo")

            async with state.proxy() as data: 
                await state.reset_data()
                data['photo_num'] = 0
                data['GO_SEND'] = False
                data['id_user'] = []

        except Exception as ex:
            await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки в mega_sending: {ex}")
            print(f"main.py [INFO] Неполадки в mega_sending: {ex}")

    else:
        await message.answer('Кудааа мы лезем? Не положено, давай в меню.')
        await menu.toMenu(message)
#------------------------------------------------------------------------------
@dp.message_handler(CHAT_PRIVATE, commands=['send'])                                                    ## ЛИЧНОЕ СООБЩЕНИе ЮЗЕРУ
async def send(message: Message, state: FSMContext) -> None:
    try:
        if message.chat.id in ADMIN:
            user_id = []
            user_id.append(message.text[6:19])

            async with state.proxy() as data:
                await state.reset_data()
                data['photo_num'] = 0
                data['GO_SEND'] = False
                data['id_user'] = user_id

                if (db.user_in_database(message.text[6:19])):
                    await bot.send_message(message.chat.id, f"Message to user: <b>{db.getting(message.text[6:19], 'username')}</b>- id: {message.text[6:19]}, \
                    \nOn <b> {db.getting(message.text[6:19], 'language')} </b> Message:", parse_mode='html')
                    await TextToSend.TEXT.set()

                else:
                    await bot.send_message(message.chat.id, "This user is not in database")


        else:  await message.answer('Кудааа мы лезем? Не положено, давай в меню.'), await menu.toMenu(message)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Непладки в send: {ex}")
        print(f"main.py [INFO] Неполадки в send: {ex}")
#------------------------------------------------------------------------------
@dp.message_handler(CHAT_PRIVATE, content_types=['photo'], state=TextToSend.TEXT)                       ## ЕСЛИ В РАССЫЛКЕ ФОТО
async def toSend_photo(message: Message, state: FSMContext) -> None:
    try:
        async with state.proxy() as data:
            data['photo_num'] += 1
            data[f"photo{data['photo_num']}"] = message.photo[0].file_id
            await bot.send_message(message.chat.id, "Okay, now send text under this photo(s)")

    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки в toSend_photo: {ex}")
        print(f"main.py [INFO] Неполадки в toSend_photo: {ex}")
#------------------------------------------------------------------------------
@dp.message_handler(CHAT_PRIVATE, content_types=['text'], state=TextToSend.TEXT)                        ## ЕСЛИ В РАССЫЛКЕ ТЕКСТ
async def toSend_text(message: Message, state: FSMContext) -> None:
    try:
        async with state.proxy() as data:

            list_photo = MediaGroup()
            for num in range(1, data['photo_num']+1): 
                try: list_photo.attach_photo(data[f'photo{num}'], None)
                except: pass

            if (data['GO_SEND'] == False):

                data['TEXT'] = message.text
                
                if data['photo_num'] > 1: await bot.send_media_group(message.chat.id, media=list_photo)
                if len(data['id_user']) > 1 or len(data['id_user']) == 0:
                    await bot.send_message(message.chat.id, f"Your Message: \n\n{data['TEXT']}\n\nOkay, send? Can rewrite", reply_markup=InlineKeyboardMarkup(row_width=2)
                    .add(InlineKeyboardButton(text= 'Only Rus', callback_data='OnlyRus'))
                    .add(InlineKeyboardButton(text= 'Only Ukr', callback_data='OnlyUkr'))
                    .add(InlineKeyboardButton(text= 'SEND 🔆', callback_data='SEND')))

                else: await bot.send_message(message.chat.id, f"Message to: \n\n{data['TEXT']}\n\nOkay, send? Can rewrite", reply_markup=InlineKeyboardMarkup(row_width=2)
                    .add(InlineKeyboardButton(text= 'SEND 🔆', callback_data='SEND')))

            else: 

                if len(data['id_user']) > 1:
                    for user in data['id_user']:
                        try:
                            if data['photo_num'] > 1: await asyncio.sleep(0.1), await bot.send_media_group(user, media=list_photo), await bot.send_message(user, f"{data['TEXT']}")
                            elif data['photo_num'] == 0: await asyncio.sleep(0.1), await bot.send_message(user, f"{data['TEXT']}")
                            elif data['photo_num'] == 1: await asyncio.sleep(0.1), await bot.send_photo(user, photo= data['photo1'], caption= f"{data['TEXT']}")

                        except Exception as ex:
                            print(f"main.py [INFO] Неполадки в toSend_text в рассылке: id - {user} | Ошибка: {ex}")
                            await bot.send_message(f"main.py [INFO] Неполадки в toSend_text в общей рассылке: id - {user} | Ошибка: {ex}")

                    await bot.delete_message(message.chat.id, message.message_id)
                    await bot.send_message(message.chat.id, 'Рассылка отправлена 〽️', reply_markup=ReplyKeyboardRemove() )
                    await state.reset_data(), await state.finish()

                else: 
                    try: 
                        for user in data['id_user']:  await bot.send_message(user, f"〽️ Admin: {data['TEXT']}")
                    except: 
                        print(f"main.py [INFO] Неполадки в toSend_text в инд. рассылке: id - {user} | Ошибка: {ex}")
                        await bot.send_message(f"main.py [INFO] Неполадки в toSend_text в общей рассылке: id - {user} | Ошибка: {ex}")
                    finally:
                        await bot.delete_message(message.chat.id, message.message_id)
                        await bot.send_message(message.chat.id, 'Сообщение отправлено 〽️', reply_markup=ReplyKeyboardRemove() )
                        await state.reset_data(), await state.finish()                      

                
    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки в toSend_text: {ex}")
        print(f"main.py [INFO] Неполадки в toSend_text: {ex}")
#------------------------------------------------------------------------------
@dp.callback_query_handler(CHAT_PRIVATE, text=['OnlyRus', 'OnlyUkr', 'SEND'], state=TextToSend.TEXT)    ## ОПРЕДЕЛЕНИЕ ЯЗЫКА И ОТПРАВКИ
async def ChoiseWhoneSend(c: CallbackQuery, state: FSMContext) -> None:
    try:
        async with state.proxy() as data:

            if c.data == 'SEND':
                data['GO_SEND'] = True
                await toSend_text(c.message, state)

            elif c.data == 'OnlyRus':
                data['id_user'] = db.get_all_id('ru')
                await c.answer("Отсортировано по русскому языку")

            elif c.data == 'OnlyUkr':
                data['id_user'] = db.get_all_id('uk')
                await c.answer("Отсортировано по украинскому языку")
            
    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки в ChoiseWhoneSend: {ex}")
        print(f"main.py [INFO] Неполадки в ChoiseWhoneSend: {ex}")


#################################################### - ASK from USER to ADMIN ######################################
class AskAdmin(StatesGroup):
    ask = State()

@dp.callback_query_handler(CHAT_PRIVATE, text='go_back', state=AskAdmin)                                ## ОТМЕНА ВОПРОСА АДМИНУ
async def ask_cancel(call: CallbackQuery, state: FSMContext) -> None:

    try:
        lang = db.getting(call.message.from_user.id, 'language')
        await bot.send_message(call.message.chat.id, general_text[f'{lang}_ask_admin_no'])
        await state.reset_data()
        await state.finish()
        await menu.toMenu(call.message)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки в ask_cancel: {ex}")
        print(f"main.py [INFO] Неполадки в ask_cancel: {ex}")
#------------------------------------------------------------------------------
@dp.message_handler(CHAT_PRIVATE, commands=['ask'])                                                     ## ЗАДАТЬ ВОПРОС АДМИНУ
async def ask_user(message: Message) -> None:
    try:
        lang = db.getting(message.from_user.id, 'language')
        name = message.from_user.first_name

        if (message.text).strip() != '/ask':
            await bot.send_message(ADMIN[1], f'{name} - id: {message.chat.id}, @{message.chat.username}\nMessage: {message.text[5:]}')
            await bot.send_message(message.chat.id, general_text[f'{lang}_send_ask'])
        else:
            await bot.send_message(message.chat.id, general_text[f'{lang}_empty_ask'],
                                   reply_markup=InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Назад', callback_data='go_back')))
            await AskAdmin.ask.set()

    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки в ask_user: {ex}")
        print(f"main.py [INFO] Неполадки в ask_user: {ex}")
#------------------------------------------------------------------------------
@dp.message_handler(CHAT_PRIVATE, content_types=['text'], state=AskAdmin.ask)                           ## ОТПРАВКА ASK 
async def ask_user_text(message: Message, state: FSMContext) -> None:
    try:
        lang = db.getting(message.from_user.id, 'language')
        name = message.from_user.first_name
        await bot.send_message(ADMIN[1], f'{message.from_user.first_name} - id: {message.chat.id}, @{message.chat.username}\nMessage: {message.text}')
        await bot.send_message(message.chat.id, f"{general_text[f'{lang}_send_ask']}")
        await state.reset_data()
        await state.finish()
        await menu.toMenu(message)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки в ask_user_text: {ex}")
        print(f"main.py [INFO] Неполадки в ask_user_text: {ex}")


################################################# - FEEDBACK and TEST(pizda) and POH ###############################

@dp.message_handler(CHAT_PRIVATE, commands=["feedback"])                                                ## ОБРАТНАЯ СВЯЗЬ -> callback_querry.py (fb_yes, fb_no)
async def feedback(message: Message) -> None:
    try:
        lang = db.getting(message.chat.id, 'language')
        await message.answer(general_text[f'{lang}_feedback_yes'], reply_markup=feedback_button[lang])

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'main.py [INFO] Неполдаки в начале feedback: {ex}')
        print(f"main.py [INFO] Неполадки в начале feedback: {ex}")
#------------------------------------------------------------------------------
@dp.message_handler(CHAT_PRIVATE, commands=['poh'])                                                     ## ПРОСТО ПНУТЬ АДМИНА
async def poh(message: Message):
    try:
        lang = db.getting(message.from_user.id, 'language')
        await bot.send_message(ADMIN[1], f"@{message.chat.username}: {db.getting(message.from_user.id, 'username')}, {message.chat.id} тебя пнул :)")

        if lang == 'uk':    await message.answer('Все зроблено босс. Я його пнув 😀')
        else:               await message.answer('Всё сделано босс. Я его пнул 😀')

    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки с poh: {ex}")
        print(f"main.py [INFO] Неполадки с poh: {ex}")
#------------------------------------------------------------------------------
@dp.message_handler(CHAT_PRIVATE, commands=['cucumber'])                                                ## ДЛЯ ТЕСТА ФУНКЦИЙ
async def cucumber(message: Message):
    try:
        lang = db.getting(message.chat.id, 'language')
        await message.answer(f"{test_hopeless_beka_result[f'{lang}_0-3']}\n\n", parse_mode='html')
        await message.answer(f"{test_hopeless_beka_result[f'{lang}_4-8']}\n\n", parse_mode='html')
        await message.answer(f"{test_hopeless_beka_result[f'{lang}_9-14']}\n\n", parse_mode='html')
        await message.answer(f"{test_hopeless_beka_result[f'{lang}_15-20']}\n\n", parse_mode='html')
        await message.answer(f"{test_hopeless_beka_result[f'{lang}0-9']}\n\n", parse_mode='html')
        await message.answer(f"{test_hopeless_beka_result[f'{lang}10-15']}\n\n", parse_mode='html')
        await message.answer(f"{test_hopeless_beka_result[f'{lang}16-19']}\n\n", parse_mode='html')
        await message.answer(f"{test_hopeless_beka_result[f'{lang}20-29']}\n\n", parse_mode='html')
        await message.answer(f"{test_hopeless_beka_result[f'{lang}30-63']}\n\n", parse_mode='html')

    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки с test-panel pizda: {ex}")
        print(f"main.py [INFO] Неполадки с test-panel pizda: {ex}")
#------------------------------------------------------------------------------
async def main():                                                                        ## START POLLING
    await bot.delete_webhook(drop_pending_updates=True)
    #users = db.get_all_id()
    #print(users)
    await dp.start_polling(bot)


    # photo = open('photo_2023-02-14_14-42-31.jpg', 'rb')
    # for user in users:
    # await bot.send_message(user, f'Вітаю тебе зі святом', reply_markup=go_to_menu_safe)
    # await bot.send_message(720526928, depression_beka_result['uk20-29'], reply_markup=go_to_menu_safe)

if __name__ == '__main__':
    import handlers.reactions    
    asyncio.run(main())

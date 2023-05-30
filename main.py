from aiogram.types import Message, CallbackQuery, MediaGroup, BotCommand
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from support.querry_db import db
from aiogram import executor
from support.config import *
from handlers import *
from asyncio import sleep


################################################## - ADMIN PANEL and HELP PANEL ##########################

@dp.message_handler(CHAT_PRIVATE, CommandHelp())                                                        ## ПАНЕЛЬ ПОМОЩИ ЮЗЕРУ
async def help_panel(message: Message) -> None:
    if (db.user_in_database(message.chat.id)):
        lang = db.getting(message.chat.id, 'language')
        await message.answer(general_text[f'{lang}_help_menu'], parse_mode='html')
    else:
        await message.answer('Сначала зарегистрируйся: 🙂'), await sign_up.start(message, FSMContext)
#------------------------------------------------------------------------------
@dp.message_handler(CHAT_PRIVATE, commands=['negr'])                                                    ## ПАНЕЛЬ ПОМОЩИ АДМИНУ
async def admin_panel(message: Message) -> None:
    try:
        if message.from_user.id in ADMIN:
            await message.answer('Hi, my lord. 🤴')
            await message.answer('Here:\n/start - Старт, общий запуск\n/cucumber - Тестирование функций\n/poh - Пнуть Админа\n/send - СообщениЕ Пользователю\n/mega_send - СообщениЯ Пользовалелям')
        else:
            await message.answer('Кудааа мы лезем? Не положено, давай в меню.')
            await menu.toMenu(message)
    except Exception as ex: await exceptions("main.py", 'admin_panel', ex)
    

################################################### - ASK from ADMIN to USER - ###########################
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

    except Exception as ex: await exceptions("main.py", 'send_cancel', ex)

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

        except Exception as ex: await exceptions("main.py", 'mega_send', ex)


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
                if (message.text).strip() != '/send':
                    if (db.user_in_database(message.text[6:19])):
                        await bot.send_message(message.chat.id, f"Message to user: <b>{db.getting(message.text[6:19], 'username')}</b>- id: {message.text[6:19]}, \
                        \nOn <b> {db.getting(message.text[6:19], 'language')} </b> Message:", parse_mode='html'), await TextToSend.TEXT.set()

                    else: await bot.send_message(message.chat.id, "This user is not in database")
                else: await bot.send_message(message.chat.id, "Empty ID user. Please text: /send `1082803262`", parse_mode= "Markdown")

        else:  await message.answer('Кудааа мы лезем? Не положено, давай в меню.'), await menu.toMenu(message)

    except Exception as ex: await exceptions("main.py", 'send', ex)

#------------------------------------------------------------------------------
@dp.message_handler(CHAT_PRIVATE, content_types=['photo'], state=TextToSend.TEXT)                       ## ЕСЛИ В РАССЫЛКЕ ФОТО
async def toSend_photo(message: Message, state: FSMContext) -> None:
    try:
        async with state.proxy() as data:
            data['photo_num'] += 1
            data[f"photo{data['photo_num']}"] = message.photo[0].file_id
            await bot.send_message(message.chat.id, "Okay, now send text under this photo(s)")

    except Exception as ex: await exceptions("main.py", 'toSend_photo', ex)

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
                            if data['photo_num'] > 1: await sleep(0.1), await bot.send_media_group(user, media=list_photo), await bot.send_message(user, f"{data['TEXT']}")
                            elif data['photo_num'] == 0: await sleep(0.1), await bot.send_message(user, f"{data['TEXT']}")
                            elif data['photo_num'] == 1: await sleep(0.1), await bot.send_photo(user, photo= data['photo1'], caption= f"{data['TEXT']}")

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
                        await bot.delete_message(message.chat.id, message.message_id), await state.reset_data()
                        await bot.send_message(message.chat.id, 'Сообщение отправлено 〽️', reply_markup=ReplyKeyboardRemove() )
                        await state.finish()                      

                
    except Exception as ex: await exceptions("main.py", 'toSend_text', ex)

#------------------------------------------------------------------------------
@dp.callback_query_handler(CHAT_PRIVATE, text=['OnlyRus', 'OnlyUkr', 'SEND'], state=TextToSend.TEXT)    ## ОПРЕДЕЛЕНИЕ ЯЗЫКА И ОТПРАВКИ
async def ChoiseWhoneSend(c: CallbackQuery, state: FSMContext) -> None:
    try:
        async with state.proxy() as data:

            if c.data == 'SEND':
                data['GO_SEND'] = True
                await toSend_text(c.message, state)

            elif c.data == 'OnlyRus':
                data['GO_SEND'] = True
                data['id_user'] = db.get_all_id('ru')
                await c.answer("Отсортировано по русскому языку")

            elif c.data == 'OnlyUkr':
                data['GO_SEND'] = True
                data['id_user'] = db.get_all_id('uk')
                await c.answer("Отсортировано по украинскому языку")
            
    except Exception as ex: await exceptions("main.py", 'ChoiseWhoneSend', ex)



################################################# - TESTING - ############################################

@dp.message_handler(CHAT_PRIVATE, commands=['cucumber'])                                                ## ДЛЯ ТЕСТА ФУНКЦИЙ
async def cucumber(message: Message):
    try:
        lang = db.getting(message.chat.id, 'language')
        #await bot.send_message("459849194", f"{test_hopeless_beka_result[f'{lang}_0-3']}\n\n", parse_mode='html')
        await bot.send_message(message.chat.id, f"{test_hopeless_beka_result[f'{lang}_0-3']}\n\n", parse_mode='html')
        # await message.answer(f"{test_hopeless_beka_result[f'{lang}_0-3']}\n\n", parse_mode='html')
        # await message.answer(f"{test_hopeless_beka_result[f'{lang}_4-8']}\n\n", parse_mode='html')
        # await message.answer(f"{test_hopeless_beka_result[f'{lang}_9-14']}\n\n", parse_mode='html')
        # await message.answer(f"{test_hopeless_beka_result[f'{lang}_15-20']}\n\n", parse_mode='html')

    except Exception as ex: await exceptions("main.py", 'cucumber', ex)


##======================================================================================================##
async def set_default_command(dp):                                                                      ## DEFAULT COMMAND SET
    await bot.set_my_commands(
        [   
            BotCommand("start", "Start bot  ▶️"),
            BotCommand("menu", "Go to menu 🔅"),
            BotCommand("help", "Help-panel ❔")
        ]
    )

async def on_startup(dispatcher):                                                                       ## START POLLING
    #await bot.delete_webhook(drop_pending_updates=True)  
    await set_default_command(dispatcher)
    await bot.send_message(ADMIN, "[INFO] Bot was launched successfully.")

async def on_shutdown(dispatcher):                                                                      ## STOP POLLING
    await bot.delete_webhook()

if __name__ == '__main__': executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
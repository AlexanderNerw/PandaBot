from handlers import keyboards as kb, tests as ts, setting as st, menu
from importing import *

# Машина сострояний
class ClientStateGroup(StatesGroup):
    photo = State()
    desc = State()

@dp.message_handler(commands=['cancel'])
async def get_cancel(message: types.Message, state: FSMContext) -> None:
    await state.finish()


#№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№ БОТ БОТ БОТ БОТ БОТ №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

@dp.message_handler(commands=['start'])
async def welcome(message): ################### СТАРТ МЕНЮ ######################
    global msg
    msg = message

    try:
        if(not db.subsex(message.from_user.id)): # Пользователя нет в БД

            name_start = str(message.from_user.first_name)
            language = str(message.from_user.language_code)
            db.add_subs(message.from_user.id)
            db.adding(message.from_user.id, 'username', name_start)
            print(message)
            db.adding(message.from_user.id, 'language', language)
            await message.answer(f" {hi[language]} <b>{name_start}</b>! 😉 {hi_start[language]}" , parse_mode='html', reply_markup=kb.languageB)

        else: # Пользователь есть в БД
            global name
            name = db.getting(message.from_user.id, 'username')
            language = db.getting(message.from_user.id, 'language')
            await message.answer(f" {hi[language]} <b>{name}</b>! {again_hi_start[language]}", parse_mode='html')

    except Exception as ex:
        print('[INFO] Error of start-menu: ', ex)

#------------------------------------------------  

# @dp.message_handler(commands=['menu'])
# async def toMenu(message): #******************* ГЛАВНОЕ МЕНЮ *********************
#     global msg
#     msg = message
#     print(msg)
#     try:
#         if (db.getting(message.from_user.id, 'language') == "ru"): #            Русский язык
#             await message.answer("🔸                <b>Главное меню</b>                🔸\n\nЗдесь ты можешь пользоваться моими функциями.",
#             parse_mode='html', reply_markup=kb.board_menu)
                        
#         elif (db.getting(message.from_user.id, 'language') == "uk"): #            Украинский язык
#             await message.answer("🔸                <b>Головне меню</b>                🔸\n\nТут ти можеш користуватися моїми функціями.",
#             parse_mode='html', reply_markup = kb.board_menu)
#     except Exception as ex:
#         print('Ошибка главного меню: ', ex)

#******************************* АДМИНИСТРИРОВАНИЕ *******************************

@dp.message_handler(commands=['help'])
async def help_panel(message):
    global msg
    msg = message
    await message.answer('Here:\n/start - Старт, общий запуск\n/poh - Пнуть Админа\n/ask - Сообщение админу ( /ask text )"\n/feedback - Связь с автором')
  
#------------------------------------------------  

@dp.message_handler(commands=['negritos'])
async def admin_panel(message):
    global msg
    msg = message
    try:
        if message.from_user.id in ADMIN:
            await message.answer('Hi, my lord.')
            await message.answer('Here:\n/start - Старт, общий запуск\n/terakota - Тестирование функций\n/hyi - Пнуть Саню\n/sending - (id) (text)\n/mega_sending - (text)')
        else:
            await message.answer('Кудааа мы лезем? Не положено, давай в меню.')
            await menu.toMenu(message)
    except Exception as ex:
        print('Ошибка панели админа: ', ex)

#------------------------------------------------  

@dp.message_handler(commands=['mega_sending'])
async def mega_sending(message):
    global msg
    msg = message
    try:
        a = db.get_all('user_id')
        for i in a:
            await bot.send_message(*i, message.from_chat.text[13:])
    except Exception as ex:
        print("mega_sending не нормас: ", ex)

#------------------------------------------------  

@dp.message_handler(commands=['sending'])
async def sending(message):
    global msg
    msg = message

    try:
        await bot.send_message(message.text[9:20], f"Автор: {message.text[20:]}")
    except Exception as ex:
        print("mega_sending не нормас: ", ex)

#------------------------------------------------  

@dp.message_handler(commands=['ask'])
async def ask(message):
    global msg, name
    msg = message
    name = message.from_user.first_name
    try:
        await bot.send_message(ADMIN[0], f'{name} - id: {message.from_user.id}, @{message.from_user.username}\nMessage: {message.text[5:]}')
    except Exception as ex:
        print("mega_sending не нормас: ", ex)

#------------------------------------------------  

@dp.message_handler(commands=["feedback"])
async def feedback(message): 
    global msg
    msg = message
    try:
        if (db.getting(message.from_user.id, 'language') == "ru"):
            await message.answer("Говорят, через это меню можно поговорить с автором бота. Точно хочешь? 🙂", reply_markup=kb.fbBRu)
        else: 
            await message.answer("Кажуть, через цей відділ можна поговорити з автотором бота. Точно хочеш? 🙂", reply_markup=kb.fbBUa)

    except Exception as ex:
        print('Ошибка feedback начала: ', ex)

#------------------------------------------------  

@dp.message_handler(commands=['poh'])
async def poh(message):
    global msg
    msg = message

    try:
        user_name = message.from_user.username
        name = db.getting(message.from_user.id, 'name')
        await bot.send_message(ADMIN[0], f"@{user_name}: {name} тебя пнул :)")
        await message.answer('Всё сделано босс. Я его уложил')
    except Exception as ex:
        print("poh не нормас: ", ex)

#------------------------------------------------  

@dp.message_handler(commands=['pizda'])
async def pizda(message):
    global msg
    msg = message
    try:
        pass
    except Exception as ex:
        print("pizda не нормас: ", ex)

#------------------------------------------------  

#@dp.message_handler(commands=['restart'])
# def restart():

#     listing = db.get_update()
#     print(listing)
#     for id in listing:
#         bot.send_message(id, 'Всё нормально')
        #print(type(msg))
        #await message.answer("Обновление бота..")

#------------------------------------------------  


@dp.inline_handler()
async def inline_menu_online(inline_query: types.InlineQuery) -> None:

    text = inline_query.query or '*напиши запрос*'
    if text != None:
        procent = random.randint(0, 100)
        if procent < 10:
            how_shiza = InputTextMessageContent(message_text = f'<b>Я шизик на {procent}%!</b> 🙂', parse_mode='html')
        elif procent >= 10 and procent < 30:
            how_shiza = InputTextMessageContent(message_text = f'<b>Я шизик на {procent}%!</b> 🙄', parse_mode='html')
        elif procent >= 30 and procent < 70:
            how_shiza = InputTextMessageContent(message_text = f'<b>Я шизик на {procent}%!</b> 🫠', parse_mode='html')
        elif procent >= 70:
            how_shiza = InputTextMessageContent(message_text = f'<b>Я шизик на {procent}%!</b> 🤪', parse_mode='html')

    result_id: str = hashlib.md5(text.encode()).hexdigest()


    HowGay = InlineQueryResultArticle(
        id = str(uuid.uuid4()),
        input_message_content = InputTextMessageContent(message_text = f'<b>Я гей на {random.randint(0, 100)}%!</b> 🏳️‍🌈', parse_mode='html'),
        title = '🏳️‍🌈 Насколько % ты гей',
        description = 'Просто отправь это в чат и узнай.',
        thumb_url = 'https://kartinkof.club/uploads/posts/2022-06/1655617211_2-kartinkof-club-p-kartinki-s-nadpisyu-ti-gei-2.png'
        )
    
    HowShiza = InlineQueryResultArticle(
        id = str(uuid.uuid4()),
        input_message_content = how_shiza,
        title = '🥴 Насколько % ты шизофреник',
        description = 'Рискнёшь или боишься?',
        thumb_url = 'https://www.neurolikar.com.ua/wp-content/uploads/2017/09/bangalore-treatment-schizophrenia-symptoms.jpg'
        )

    MatNaMat = InlineQueryResultArticle(
        id = str(uuid.uuid4()),
        input_message_content = InputTextMessageContent(message_text = f'<b> {duff[random.randint(0, 42)]}!</b>', parse_mode='html'),
        title = 'Пожелать счастья собеседнику',
        description = 'Обматери его/её по полной.',
        thumb_url = 'https://psychologyjournal.ru/upload/resize_cache/iblock/710/141_113_2/7105fae3f772f4a7fe11a4d32dd217c9.jpg'
        )

    HowSex = InlineQueryResultArticle(
        id = str(uuid.uuid4()),
        input_message_content = InputTextMessageContent(message_text = f'Сегодня я пересплю с <b>{name_sex[random.randint(0, 49)]} 🥰</b>', parse_mode='html'),
        title = 'C кем я пересплю по имени',
        description = 'С кем ты переспишь ',
        thumb_url = 'https://png.pngtree.com/png-vector/20190420/ourlarge/pngtree-question-mark-vector-icon-png-image_963326.jpg'
        )

    HowDuo = InlineQueryResultArticle(
        id = str(uuid.uuid4()),
        input_message_content = InputTextMessageContent(message_text = f'Твоя совместимость с <b>{text}</b>: {random.randint(0, 100)}% 💞', parse_mode='html'),
        title = 'Проверка совместимости по имени 💞',
        description = 'Введи cюда имя и посмотрим.',
        thumb_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRw3-gg8s81qbG8genEgNX641bc2WNM9qdajA&usqp=CAU'
        )

    await bot.answer_inline_query( results = [HowGay, HowShiza, MatNaMat, HowSex, HowDuo], inline_query_id = inline_query.id, cache_time = 1 )


if __name__ == '__main__':
    executor.start_polling(dispatcher = dp, skip_updates= True)
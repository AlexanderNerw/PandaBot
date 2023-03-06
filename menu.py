from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineQuery
import hashlib, random, uuid, handlers.sign_up
from handlers.support.importing import *

######################################################################################### - ГЛАВНОЕ МЕНЮ ЛИЧНОГО ЧАТА
@dp.message_handler(CHAT_PRIVATE, commands=['menu'])                                   ##   ГЛАВНОЕ МЕНЮ
async def toMenu(message) -> None: 
    try:
        if (db.user_online_in_database(message.chat.id)):

            await bot.send_message(message.chat.id, general_text[f"{db.getting(message.chat.id, 'language')}_menu_text"],
                parse_mode='html', reply_markup = board_menu[db.getting(message.chat.id, 'language')])

        else: await message.answer('Сначала зарегистрируйся: 🙂'), await handlers.sign_up.start(message, FSMContext)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'menu.py [INFO] Неполадки в toMenu: {ex}')
        print('menu.py [INFO] Неполадки в toMenu: ', ex)

@dp.callback_query_handler(CHAT_PRIVATE, text='toMenu')                                ##   ГЛАВНОЕ МЕНЮ С ИЗМЕНЕНИЕМ
async def toMenuWithout(c: CallbackQuery) -> None:
    try:

        if (db.user_online_in_database(c.message.chat.id)):

            await bot.edit_message_text(general_text[f"{db.getting(c.message.chat.id, 'language')}_menu_text"],
                c.message.chat.id, c.message.message_id, parse_mode='html', reply_markup = board_menu[db.getting(c.message.chat.id, 'language')])

        else:
            await bot.send_message(c.message.chat.id, 'Сначала зарегистрируйся 🙂:')
            await handlers.sign_up.start(c.message, FSMContext)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'menu.py [INFO] Неполадки в toMenuInline: {ex}')
        print('menu.py [INFO] Неполадки в toMenuInline: ', ex)


######################################################################################### - ГЛАВНОЕ МЕНЮ ГРУППОВОГО ЧАТА
@dp.message_handler(CHAT_PRIVATE, commands=['menu'])                                   ##   ГЛАВНОЕ МЕНЮ ГРУППОВОГО ЧАТА
async def toMenu_group(message) -> None: 
    try:
        print(message)
        if (db.user_online_in_database(message.chat.id)):

            await bot.send_message(message.chat.id, general_text[f"{db.getting(message.chat.id, 'language')}_menu_text"],
                parse_mode='html', reply_markup = board_menu[db.getting(message.chat.id, 'language')])

        else: await message.answer('Сначала зарегистрируйся: 🙂'), await handlers.sign_up.start(message, FSMContext)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'menu.py [INFO] Неполадки в toMenu: {ex}')
        print('menu.py [INFO] Неполадки в toMenu: ', ex)


######################################################################################### - ИНЛАЙН РЕЖИМ
@dp.inline_handler()
async def inline_menu_inline(inline_query: InlineQuery) -> None:
    
    text = inline_query.query or '*напиши запрос*'

    procent = random.randint(0, 100)
    if procent < 10:
        how_shiza = InputTextMessageContent(message_text = f'<b>Я шизик на {procent}%!</b> 🙂', parse_mode='html')
        how_gay = InputTextMessageContent(message_text = f'<b>Я гей на {procent}%!</b> 🤥', parse_mode='html')
    elif procent >= 10 and procent < 30:
        how_shiza = InputTextMessageContent(message_text = f'<b>Я шизик на {procent}%!</b> 🙄', parse_mode='html')
        how_gay = InputTextMessageContent(message_text = f'<b>Я гей на {procent}%!</b> 🙂', parse_mode='html')
    elif procent >= 30 and procent < 70:
        how_shiza = InputTextMessageContent(message_text = f'<b>Я шизик на {procent}%!</b> 🫠', parse_mode='html')
        how_gay = InputTextMessageContent(message_text = f'<b>Я гей на {procent}%!</b> 🤫', parse_mode='html')
    elif procent >= 70:
        how_shiza = InputTextMessageContent(message_text = f'<b>Я шизик на {procent}%!</b> 🤪', parse_mode='html')
        how_gay = InputTextMessageContent(message_text = f'<b>Я гей на {procent}%!</b> 🏳️‍🌈', parse_mode='html')

    result_id: str = hashlib.md5(text.encode()).hexdigest()


    HowGay = InlineQueryResultArticle(
        id = str(uuid.uuid4()),
        input_message_content = how_gay,
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

    NameRandom = InlineQueryResultArticle(
        id = str(uuid.uuid4()),
        input_message_content = InputTextMessageContent(message_text = f'<b> {duff[random.randint(0, 42)]}!</b>', parse_mode='html'),
        title = 'Пожелать счастья собеседнику',
        description = 'Обматери его/её по полной.',
        thumb_url = 'https://psychologyjournal.ru/upload/resize_cache/iblock/710/141_113_2/7105fae3f772f4a7fe11a4d32dd217c9.jpg'
        )


    HowSex = InlineQueryResultArticle(
        id = str(uuid.uuid4()),
        input_message_content = InputTextMessageContent(message_text = f'Сегодня я пересплю с <b>{name_sex[random.randint(0, 47)]} 🥰</b>', parse_mode='html'),
        title = 'C кем я сегодня пересплю?',
        description = 'С кем ты сегодня переспишь.',
        thumb_url = 'https://png.pngtree.com/png-vector/20190420/ourlarge/pngtree-question-mark-vector-icon-png-image_963326.jpg'
        )

    empty_how_duo = InputTextMessageContent(message_text = f'<b>Ты даун тупой введи имя сука 🥰</b>', parse_mode='html')
    full_how_duo = InputTextMessageContent(message_text = f'Твоя совместимость с <b>{text}</b>: {random.randint(0, 100)}% 💞', parse_mode='html')
    how_duo = empty_how_duo if text in ['*напиши запрос*', 'c cобой', 'cобой'] else full_how_duo

    HowDuo = InlineQueryResultArticle(
        id = str(uuid.uuid4()),
        input_message_content = how_duo,
        title = 'Проверка совместимости по имени 💞',
        description = 'Введи cюда имя и посмотрим.',
        thumb_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRw3-gg8s81qbG8genEgNX641bc2WNM9qdajA&usqp=CAU'
        )

    await bot.answer_inline_query( results = [HowGay, HowShiza, MatNaMat, HowSex, HowDuo], inline_query_id = inline_query.id, cache_time = 1 )
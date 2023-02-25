from handlers.support.importing import *

@dp.message_handler(commands=['name'])
async def input_name(message):
    if (db.getting(message.from_user.id, 'language') == 'ru'):
        await message.answer("Как мне тебя называть?")
    else:
        await message.answer("Як мені до тебе звертатись?")

@dp.message_handler(ChatTypeFilter(chat_type=ChatType.PRIVATE), content_types=['text'])
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

            # ПРИМОЧКИ ****************************************************************************************

            else:
                await message.answer('Я не знаю что ответить :(') 

        else:
            db.adding(message.from_user.id, 'language', 'ru')
            await reaction(message)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'uslovie.py [INFO] Неполадки в reaction: {ex}')
        print(f'uslovie.py [INFO] Неполадки в reaction: {ex}')

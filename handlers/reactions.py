from handlers.support.importing import *
from bs4 import BeautifulSoup
import requests, random

@dp.message_handler(CHAT_PRIVATE, commands=['name'])
async def input_name(message):
    if (db.getting(message.from_user.id, 'language') == 'ru'):
        await message.answer("Как мне тебя называть?")
    else:
        await message.answer("Як мені до тебе звертатись?")

@dp.message_handler(CHAT_PRIVATE, content_types=['text'])
async def reaction(message):

    text_user = (message.text).lower()
    lang = db.getting(message.from_user.id, 'language')

    try:
        if lang in ['ru', 'uk']:

            # РАЗГОВОР ******************************************************************
            if text_user[:4] in ["вики", "wiki"]:
                url = "https://ru.wikipedia.org/w/index.php?go=Перейти&search=" + message.text[5:]
                request = requests.get(url)
                soup = BeautifulSoup(request.text, "html.parser")

                links = soup.find_all("div", class_ = "mw-search-result-heading")

                if len(links) > 0:
                    url = "https://ru.wikipedia.org" + links[0].find("а")["href"]
                    bot.send_message(message.chat.id, url)

                await bot.send_message(message.chat.id, request)
            
            #---------------------------------------------------
            if text_user in ["как дела?", "как настроение?"]:
                await message.answer('Всё отлично, а ты как?')

            #---------------------------------------------------
            if "анекдот" in text_user:
                

                await bot.send_message(message.chat.id, general_text[f"{lang}_joke_for_like"] + all_jokes[random.randint(0,888)], parse_mode='html')

            #---------------------------------------------------
            elif text_user in ["меню", "menu"]:
                await menu.toMenu(message)

            # ПРИМОЧКИ ****************************************************************************************

            else:
                await message.answer('Я не знаю что ответить :(') 

        else:
            db.adding(message.from_user.id, 'language', 'ru')
            await reaction(message)

    except Exception as ex: await exceptions("reactions.py", 'reaction', ex)

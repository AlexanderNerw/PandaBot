from aiogram.dispatcher.filters.builtin import ChatTypeFilter, ChatType
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
import logging, time, os
from dotenv import load_dotenv
from support.keyboards import *
from support.dialogs import *

# Уровень логов
logging.basicConfig(level=logging.INFO, format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s')
storage = MemoryStorage()
load_dotenv()

#===================================================================#   INFO

TOKEN = os.getenv("TOKEN")
ADMIN = os.getenv('ADMIN')

CHAT_PRIVATE = ChatTypeFilter(chat_type=ChatType.PRIVATE)
CHAT_GROUP = ChatTypeFilter(chat_type=ChatType.GROUP)

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')
WEBAPP_PORT = os.getenv("PORT", 8000)

WEBHOOK_HOST = 'https://pandabot.herokuapp.com/'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'
#====================================================================================================#   ERRORS  
#    
async def exceptions(file: str, func: str, exception: str):            
    try:                                    
        await bot.send_message(ADMIN, f"[INFO] File: {file} | Func: {func}() \nError: {exception}")
        print(f"[INFO] [{time.asctime()}] File: {file} | Func: {func}: \nError: {exception}")         
   
    except Exception as ex:
        await bot.send_message(ADMIN, f"[INFO] File: config.py | Func: exceptions() \nError: {ex}")
        print(f"[INFO] [{time.asctime()}] File: config.py | Func: exceptions() \nError: {ex}")

#====================================================================================================#   BOT INFO

bot = Bot(token = TOKEN)
dp = Dispatcher(bot, storage = storage)
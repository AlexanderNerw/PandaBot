from aiogram.dispatcher.filters.builtin import ChatTypeFilter, ChatType
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
import logging, time, os

# Уровень логов
logging.basicConfig(level=logging.INFO, format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s')
storage = MemoryStorage()

#===================================================================#   INFO

ADMIN = [1082803262, 5287350422]
CHAT_PRIVATE = ChatTypeFilter(chat_type=ChatType.PRIVATE)
CHAT_GROUP = ChatTypeFilter(chat_type=ChatType.GROUP)

#====================================================================================================#   ERRORS  
#    
async def exceptions(file: str, func: str, exception: str):            
    try:                                                                                               
        await bot.send_message(ADMIN[0], f"[INFO] File: {file} | Func: {func}() \nError: {exception}")
        print(f"[INFO] [{time.asctime()}] File: {file} | Func: {func}: \nError: {exception}")         
   
    except Exception as ex:
        await bot.send_message(ADMIN[0], f"[INFO] File: config.py | Func: exceptions() \nError: {ex}")
        print(f"[INFO] [{time.asctime()}] File: config.py | Func: exceptions() \nError: {ex}")

#====================================================================================================#   BOT INFO

Token = ['6147145237:AAE5qAmLI-dnL5cKf7yo9yhhHL_-_x2vRM8']
bot = Bot(token = '6147145237:AAE5qAmLI-dnL5cKf7yo9yhhHL_-_x2vRM8')
dp = Dispatcher(bot, storage = storage)

#====================================================================#     SERVER DATABSE INFO   
#   
host = 'localhost' # localhost - 109.94.209.115 - nerw-studio.pp.ua.org
user = 'alexnerw'
password = 'nerviothink5'
db_name = 'pandabase' # subscribers
port = 3306
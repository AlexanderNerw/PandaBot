from aiogram.dispatcher.filters.builtin import ChatTypeFilter, ChatType
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
import logging, time

# Уровень логов
logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()

#===================================================================#   INFO

ADMIN = [1082803262, 5287350422]
CHAT_PRIVATE = ChatTypeFilter(chat_type=ChatType.PRIVATE)
CHAT_GROUP = ChatTypeFilter(chat_type=ChatType.GROUP)

#====================================================================================================#   ERRORS  
#    
async def exceptions(file: str, func: str, exception: str):            
    try:                                                                                               
        await bot.send_message(ADMIN[1], f"[INFO] File: {file} | Func: {func}() \nError: {exception}")
        print(f"[INFO] [{time.asctime()}] File: {file} | Func: {func}: \nError: {exception}")         
   
    except Exception as ex:
        await bot.send_message(ADMIN[1], f"[INFO] File: config.py | Func: exceptions() \nError: {ex}")
        print(f"[INFO] [{time.asctime()}] File: config.py | Func: exceptions() \nError: {ex}")

#====================================================================================================#   BOT INFO

Token = ['6147145237:AAE5qAmLI-dnL5cKf7yo9yhhHL_-_x2vRM8']
bot = Bot(token = '6147145237:AAE5qAmLI-dnL5cKf7yo9yhhHL_-_x2vRM8')
dp = Dispatcher(bot, storage = storage)

#====================================================================#     SERVER DATABSE INFO   
#   
host = '127.0.0.1' # localhost - 127.0.0.1
user = 'root'
password = 'sanik888'
db_name = 'pandabase' # subscribers
port = 3306
from aiogram.dispatcher.filters.builtin import ChatTypeFilter, ChatType
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
import logging, time, os
from dotenv import load_dotenv
from support.keyboards import *
from support.dialogs import *
from flask import Flask, request

# Уровень логов
logging.basicConfig(level=logging.INFO, format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s')
storage = MemoryStorage()
load_dotenv()

#===================================================================#   INFO

TOKEN = os.getenv("TOKEN")
PORT = os.getenv("PORT", 5000)
ADMIN = os.getenv('ADMIN')
APP_URL = os.getenv('APP_URL')
CHAT_PRIVATE = ChatTypeFilter(chat_type=ChatType.PRIVATE)
CHAT_GROUP = ChatTypeFilter(chat_type=ChatType.GROUP)

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
server = Flask(__name__)
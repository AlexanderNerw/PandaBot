from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

# Уровень логов
logging.basicConfig(level=logging.INFO)

# TIMEZONE
TIMEZONE = 'Europe/Kiev'
TIMEZONE_COMMON_NAME = 'Kiev'
ADMIN = [1082803262, 459849194]

storage = MemoryStorage()

Token = ['6147145237:AAE5qAmLI-dnL5cKf7yo9yhhHL_-_x2vRM8']

bot = Bot(token = '6147145237:AAE5qAmLI-dnL5cKf7yo9yhhHL_-_x2vRM8')
dp = Dispatcher(bot, storage = storage)

host = '127.0.0.1' # localhost - 127.0.0.1
user = 'root'
password = 'sanik888'
db_name = 'pandabase' # subscribers
port = 3306

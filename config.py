from querry_db import QuerryDB
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from importing import *

# Cоединение с БД
db = QuerryDB()

# Уровень логов
logging.basicConfig(level=logging.INFO)

# TIMEZONE
TIMEZONE = 'Europe/Kiev'
TIMEZONE_COMMON_NAME = 'Kiev'
ADMIN = [1082803262, 459849194]

storage = MemoryStorage()

Token = ['5644119718:AAG4QKyUab3V7HrjabmcR1r-NtX2IWmOH7Y']

bot = Bot(token = '5644119718:AAG4QKyUab3V7HrjabmcR1r-NtX2IWmOH7Y')
dp = Dispatcher(bot, storage = storage)

host = '127.0.0.1' # localhost - 127.0.0.1
user = 'root'
password = 'sanik888'
db_name = 'pandabase' # subscribers
port = 3306

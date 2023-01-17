import main
from aiogram import Bot, Dispatcher, executor, types
from config import dp

async def setting(message):
   await message.answer(' ⚙️ Настройки:\nПошёл нахер')
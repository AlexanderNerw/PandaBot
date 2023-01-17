from aiogram import Bot, Dispatcher, executor, types
from config import dp

async def tests(message):
   await message.answer('Вот cписок доступных тестов:\nНихуя нема')

def register_uslovie(dp : Dispatcher):
    dp.register_message_handler(tests, commands=['tests'])
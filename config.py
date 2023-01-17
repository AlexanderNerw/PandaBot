from aiogram import Bot, Dispatcher

TIMEZONE = 'Europe/Kiev'
TIMEZONE_COMMON_NAME = 'Kiev'
ADMIN = [1082803262, 459849194]

Token = ['5357393783:AAEz0T0qhn-Ph6YD-NdQQFxB_NhxCt7vXUk']

bot = Bot(token='5357393783:AAEz0T0qhn-Ph6YD-NdQQFxB_NhxCt7vXUk')
dp = Dispatcher(bot)

host = 'arn:aws:rds:eu-north-1:490943922602:db:pandabase'
user = 'alexnerw'
password = 'alexnerw'
db_name = 'pandabase'
port = 3306

from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup
import logging, handlers.uslovie, handlers.callback_querry, hashlib, random, uuid
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import executor, types, Dispatcher
from config import dp, bot, ADMIN, storage, db
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from handlers.dialogs import *
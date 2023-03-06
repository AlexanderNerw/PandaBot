from aiogram.types import Message, ChatType, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ContentType, MediaGroup, Chat
from aiogram.dispatcher.filters.builtin import ChatTypeFilter, Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from handlers.support.config import *
from aiogram.dispatcher import FSMContext, Dispatcher
from handlers.support.querry_db import db
from handlers.support.keyboards import *
from handlers.support.dialogs import *


CHAT_PRIVATE = ChatTypeFilter(chat_type=ChatType.PRIVATE)
CHAT_GROUP = ChatTypeFilter(chat_type=ChatType.GROUP)

import menu
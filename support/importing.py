from aiogram.types import Message, ChatType, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ContentType, MediaGroup, Chat
from aiogram.dispatcher.filters.builtin import ChatTypeFilter, Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from support.config import *
from aiogram.dispatcher import FSMContext, Dispatcher
from support.querry_db import db
from support.keyboards import *
from support.dialogs import *

CHAT_PRIVATE = ChatTypeFilter(chat_type=ChatType.PRIVATE)
CHAT_GROUP = ChatTypeFilter(chat_type=ChatType.GROUP)

import menu
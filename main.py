import asyncio, handlers.sign_up, handlers.callback_query
from aiogram.dispatcher.filters.builtin import CommandHelp
from handlers.support.importing import *
from aiogram import executor

# АДМИНИСТРИРОВАНИЕ ################################### ADMIN PANEL and SEND MESSAGE to USER/S

@dp.message_handler(CommandHelp(), ChatTypeFilter(chat_type=ChatType.PRIVATE))
async def help_panel(message: Message) -> None:

    if (db.user_in_database(message.chat.id)):
        lang = db.getting(message.chat.id, 'language')
        await message.answer(general_text_answer[f'{lang}_help_menu'], parse_mode='html')
    else: await message.answer('Сначала зарегистрируйся: 🙂'), await handlers.sign_up.start(message, FSMContext)
# ----------------------------------------------------------------------------


@dp.message_handler(ChatTypeFilter(chat_type=ChatType.PRIVATE), commands=['negr'])
async def admin_panel(message: Message) -> None:

    try:
        if message.from_user.id in ADMIN:
            await message.answer('Hi, my lord.')
            await message.answer('Here:\n/start - Старт, общий запуск\n/pizda - Тестирование функций\n/poh - Пнуть Саню\n/sending - (id) (text)\n/mega_sending - (text)')
        else:
            await message.answer('Кудааа мы лезем? Не положено, давай в меню.')
            await menu.toMenu(message)
    except Exception as ex:
        await bot.send_message(ADMIN[1], f'main.py [INFO] Неполадки в admin_panel: {ex}')
        print(f'main.py [INFO] Неполадки в admin_panel: {ex}')
# --------------------------------------------------------------------------------

##################################################################################### - ASK from USER to ADMIN

class TextToSend(StatesGroup):
    id_user = State()
    text = State()


@dp.callback_query_handler(ChatTypeFilter(chat_type=ChatType.PRIVATE), text='go_back', state=TextToSend)
async def send_cancel(call: CallbackQuery, state: FSMContext) -> None:

    try:
        await bot.send_message(call.message.chat.id, 'TextToSend отменено.')
        await state.reset_data()
        await state.finish()

    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки в ask_cancel: {ex}")
        print(f"main.py [INFO] Неполадки в ask_cancel: {ex}")


@dp.message_handler(ChatTypeFilter(chat_type=ChatType.PRIVATE), commands=['mega_send'])
async def mega_send(message: Message) -> None:

    if message.from_user.id in ADMIN:
        
        try:
            user_dict = {}
            users = db.get_all_id()

            for user_id in users:
                print(user_id)
                user_dict[user_id['user_id']] = db.getting(user_id['user_id'], 'language')

            print(user_dict)
            #await bot.send_message(user_dict['user_id'], f'Вітаю тебе зі святом',
            #reply_markup=InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Назад', callback_data='go_back')))

        except Exception as ex:
            await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки в mega_sending: {ex}")
            print(f"main.py [INFO] Неполадки в mega_sending: {ex}")
    else:
        await message.answer('Кудааа мы лезем? Не положено, давай в меню.')
        await menu.toMenu(message)
# --------------------------------------------------------------------------------


@dp.message_handler(ChatTypeFilter(chat_type=ChatType.PRIVATE), commands=['send'])
async def send(message: Message) -> None:

    if message.chat.id in ADMIN:
        try:
            await bot.send_message(message.text[9:20], f"〽️ Автор: {message.text[20:]}")
        except Exception as ex:
            await bot.send_message(ADMIN[1], f"main.py [INFO] Непладки в sending: {ex}")
            print(f"main.py [INFO] Неполадки в sending: {ex}")
    else:
        await message.answer('Кудааа мы лезем? Не положено, давай в меню.')
        await menu.toMenu(message)
# --------------------------------------------------------------------------------


@dp.message_handler(ChatTypeFilter(chat_type=ChatType.PRIVATE), content_types=['text'], state=TextToSend.id_user)
async def toSend_user_id(message: Message, state: FSMContext) -> None:

    try:
        if (db.user_in_database(message.chat.id)):

            lang = db.getting(message.from_user.id, 'language')

            await bot.send_message(message.chat.id, f"Message to user: {message.from_user.first_name} - id: {message.chat.id}, @{message.chat.username}\nMessage:")
            await TextToSend.next()

        else:
            await bot.send_message(message.chat.id, "This user is not in database", reply_markup=InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Назад', callback_data='go_back')))

    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки в ask_user_text: {ex}")
        print(f"main.py [INFO] Неполадки в ask_user_text: {ex}")


####################################################################################################### - ASK from USER to ADMIN

class AskAdmin(StatesGroup):
    ask = State()


@dp.callback_query_handler(ChatTypeFilter(chat_type=ChatType.PRIVATE), text='go_back', state=AskAdmin)
async def ask_cancel(call: CallbackQuery, state: FSMContext) -> None:

    try:
        lang = db.getting(call.message.from_user.id, 'language')
        await bot.send_message(call.message.chat.id, general_text_answer[f'{lang}_ask_admin_no'])
        await state.reset_data()
        await state.finish()
        await menu.toMenu(call.message)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки в ask_cancel: {ex}")
        print(f"main.py [INFO] Неполадки в ask_cancel: {ex}")


@dp.message_handler(ChatTypeFilter(chat_type=ChatType.PRIVATE), commands=['ask'])
async def ask_user(message: Message) -> None:
    try:
        lang = db.getting(message.from_user.id, 'language')
        name = message.from_user.first_name

        if (message.text).strip() != '/ask':
            await bot.send_message(ADMIN[1], f'{name} - id: {message.chat.id}, @{message.chat.username}\nMessage: {message.text[5:]}')
            await bot.send_message(message.chat.id, general_text_answer[f'{lang}_send_ask'])
        else:
            await bot.send_message(message.chat.id, general_text_answer[f'{lang}_empty_ask'],
            reply_markup=InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Назад', callback_data='go_back')))
            await AskAdmin.ask.set()

    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки в ask_user: {ex}")
        print(f"main.py [INFO] Неполадки в ask_user: {ex}")


@dp.message_handler(ChatTypeFilter(chat_type=ChatType.PRIVATE), content_types=['text'], state=AskAdmin.ask)
async def ask_user_text(message: Message, state: FSMContext) -> None:
    try:
        lang = db.getting(message.from_user.id, 'language')
        name = message.from_user.first_name
        await bot.send_message(ADMIN[1], f'{message.from_user.first_name} - id: {message.chat.id}, @{message.chat.username}\nMessage: {message.text}')
        await bot.send_message(message.chat.id, f"{general_text_answer[f'{lang}_send_ask']}")
        await state.finish()
        await menu.toMenu(message)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки в ask_user_text: {ex}")
        print(f"main.py [INFO] Неполадки в ask_user_text: {ex}")


# -   FEEDBACK and TEST and POH


@dp.message_handler(ChatTypeFilter(chat_type=ChatType.PRIVATE), commands=["feedback"])
async def feedback(message: Message) -> None:

    try:
        lang = db.getting(message.chat.id, 'language')
        await message.answer(general_text_answer[f'{lang}_feedback_yes'], reply_markup=f'feedback_button_{lang}')

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'main.py [INFO] Неполдаки в начале feedback: {ex}')
        print(f"main.py [INFO] Неполадки в начале feedback: {ex}")

# ------------------------------------------------


@dp.message_handler(ChatTypeFilter(chat_type=ChatType.PRIVATE), commands=['poh'])
async def poh(message: Message):
    lang = db.getting(message.from_user.id, 'language')

    try:
        name = db.getting(message.from_user.id, 'username')
        await bot.send_message(ADMIN[1], f"@{message.chat.username}: {name}, {message.chat.id} тебя пнул :)")
        if lang == 'ru':
            await message.answer('Всё сделано босс. Я его пнул 😀')
        elif lang == 'uk':
            await message.answer('Все зроблено босс. Я його пнув 😀')

    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки с poh: {ex}")
        print(f"main.py [INFO] Неполадки с poh: {ex}")

# ------------------------------------------------


@dp.message_handler(commands=['pizda'])
async def pizda(message: Message):
    lang = 'ru'
    try:
        await message.answer(f"{test_depression_beka_result[f'{lang}0-9']}\n\n", parse_mode='html')
        await message.answer(f"{test_depression_beka_result[f'{lang}10-15']}\n\n", parse_mode='html')
        await message.answer(f"{test_depression_beka_result[f'{lang}16-19']}\n\n", parse_mode='html')
        await message.answer(f"{test_depression_beka_result[f'{lang}20-29']}\n\n", parse_mode='html')
        await message.answer(f"{test_depression_beka_result[f'{lang}30-63']}\n\n", parse_mode='html')
        print(message.chat.first_name)
    except Exception as ex:
        await bot.send_message(ADMIN[1], f"main.py [INFO] Неполадки с test-panel pizda: {ex}")
        print(f"main.py [INFO] Неполадки с test-panel pizda: {ex}")


# - START POLLING

#def register(dp : Dispatcher):
#     dp.register_message_handler(help_panel, CommandHelp(), ChatTypeFilter(chat_type=ChatType.PRIVATE))
#     dp.register_message_handler(admin_panel, ChatTypeFilter(chat_type=ChatType.PRIVATE), commands=['negr'])
#     dp.register_message_handler(send_cancel, ChatTypeFilter(chat_type=ChatType.PRIVATE), text='go_back', state=TextToSend)
#     dp.register_message_handler(mega_send, ChatTypeFilter(chat_type=ChatType.PRIVATE), commands=['mega_send'])
#     dp.register_message_handler(send, ChatTypeFilter(chat_type=ChatType.PRIVATE), commands=['send'])
#     dp.register_message_handler(toSend_user_id, ChatTypeFilter(chat_type=ChatType.PRIVATE), content_types=['text'], state=TextToSend.id_user)
#     dp.register_message_handler(ask_cancel, ChatTypeFilter(chat_type=ChatType.PRIVATE), text='go_back', state=AskAdmin)
#     dp.register_message_handler(ask_user, ChatTypeFilter(chat_type=ChatType.PRIVATE), commands=['ask'])
#     dp.register_message_handler(ask_user_text, ChatTypeFilter(chat_type=ChatType.PRIVATE), content_types=['text'], state=AskAdmin.ask)
#     dp.register_message_handler(feedback, ChatTypeFilter(chat_type=ChatType.PRIVATE), commands=["feedback"])
#     dp.register_message_handler(pizda, commands=['pizda'])

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    # users = db.get_all()
    # photo = open('photo_2023-02-14_14-42-31.jpg', 'rb')
    # print(users)
    # for user in users:
    # await bot.send_message(user['user_id'], f'Вітаю тебе зі святом', reply_markup=go_to_menu)
    # await bot.send_photo(720526928, photo=photo)
    # await bot.send_message(720526928, depression_beka_result['uk20-29'], reply_markup=go_to_menu)

if __name__ == '__main__':
    import handlers.reactions
    asyncio.run(main())

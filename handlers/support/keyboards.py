from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

"""Добавить обычную кнопку"""
# tst.kld = ReplyKeyboardMarkup(resize_keyboard=True)
# buttons = ["Тесты", "Календарь"]
# keyboard.add(*buttons)

"""Удалить кнопку"""
# await message.answer( reply_markup=ReplyKeyboardRemove())

"""Добавить обычную кнопку исчезающую"""
# keyboard = .ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# buttons = ["Тесты", "Календарь"]
# keyboard.add(*buttons)

# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№ КНОПКИ МЕНЮ №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

board_menu = { # МЕНЮ ГЛАВНОГО МЕНЮ Хе-Хе

        'ru':   InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)
        .add(   InlineKeyboardButton('Тесты 📊', callback_data='menu_test'),
                InlineKeyboardButton('Игры 🎮', callback_data='menu_game'))
        .add(   InlineKeyboardButton('Настроки ⚙️', callback_data='menu_setting'))
,
        'uk':   InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)
        .add(   InlineKeyboardButton('Тести 📊', callback_data='menu_test'),
                InlineKeyboardButton('Ігри 🎮', callback_data='menu_game'))
        .add(   InlineKeyboardButton('Налаштування ⚙️', callback_data='menu_setting'))}

menu_all_test = { # МЕНЮ ТЕСТОВ

        'ru':   InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)
        .add(   InlineKeyboardButton('Тест депрессии Бека 🫥', callback_data='test_depression_beka'))
        .add(   InlineKeyboardButton('Тест тревожности Бека 🫥', callback_data='test_depression_beka'))
        .add(   InlineKeyboardButton('Тест безнадёжности Бека 🫥', callback_data='test_depression_beka'))
        .add(   InlineKeyboardButton('⬅️', callback_data='back_list_test'),
                InlineKeyboardButton('➡️', callback_data='back_list_test'))
        .add(   InlineKeyboardButton('🔙 Назад в меню', callback_data='toMenu'))
,
        'uk':   InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)
        .add(   InlineKeyboardButton('Тест депресії Бека 🫥', callback_data='test_depression_beka'))
        .add(   InlineKeyboardButton('Тест тривожності Бека 🫥', callback_data='test_depression_beka'))
        .add(   InlineKeyboardButton('Тест безнадійності Бека 🫥', callback_data='test_depression_beka'))
        .add(   InlineKeyboardButton('⬅️', callback_data='back_list_test'),
                InlineKeyboardButton('➡️', callback_data='back_list_test'))
        .add(   InlineKeyboardButton('🔙 Назад до меню', callback_data='toMenu'))}

# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№ КНОПКИ ОБЩЕГО ВЫБОРА №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

feedback_button = {  # CВЯЗАТЬСЯ С АВТОРОМ ИЛИ ЖЕ НЕТ?

        'ru': InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)
        .add(InlineKeyboardButton('Ecтееественно 😏', callback_data='fb_yes'))
        .add(InlineKeyboardButton('Лучше потом 👋', callback_data='fb_no'))
        ,
        'uk': InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)
        .add(InlineKeyboardButton('Ну звісно ж 😏', callback_data='fb_yes'))
        .add(InlineKeyboardButton('Краще потiм 👋', callback_data='fb_no'))
}

one_two_three_four = InlineKeyboardMarkup(row_width=2, one_time_keyboard=True) \
.add(   InlineKeyboardButton(text='1', callback_data='1'),
        InlineKeyboardButton(text='2', callback_data='2')) \
.add(   InlineKeyboardButton(text='3', callback_data='3'),
        InlineKeyboardButton(text='4', callback_data='4')) \
.add(   InlineKeyboardButton(text='❌', callback_data='back_menu_test'))

button_test = InlineKeyboardMarkup(row_width=2) \
.add(   InlineKeyboardButton(text='Да, вперед', callback_data='yes_test')) \
.add(   InlineKeyboardButton( text='🔙 Назад', callback_data='back_menu_test'))

go_to_menu = InlineKeyboardMarkup(row_width=2) \
.add(   InlineKeyboardButton(text='🔸 Меню 🔸', callback_data='toMenu'))

# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№ КНОПКИ ГЛУБОКИХ НАСТРОЕК №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

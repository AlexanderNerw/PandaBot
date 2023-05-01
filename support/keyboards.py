from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№ КНОПКИ МЕНЮ №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

board_menu       = {            # КЛАВ-А МЕНЮ ГЛАВНОГО МЕНЮ Хе-Хе

        'ru':   InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)
        .add(   InlineKeyboardButton('Тесты 📊', callback_data='menu_test'),
                InlineKeyboardButton('Игры 🎮', callback_data='menu_game'))
        .add(   InlineKeyboardButton('Настроки ⚙️', callback_data='menu_setting'))
,
        'uk':   InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)
        .add(   InlineKeyboardButton('Тести 📊', callback_data='menu_test'),
                InlineKeyboardButton('Ігри 🎮', callback_data='menu_game'))
        .add(   InlineKeyboardButton('Налаштування ⚙️', callback_data='menu_setting'))}

board_menu_group = {            # КЛАВ-А МЕНЮ ГЛАВНОГО МЕНЮ В ГРУППЕ
    'ru':   InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)
        .add(   InlineKeyboardButton('Игры 🎮', callback_data='menu_game'))
        .add(   InlineKeyboardButton('Настроки ⚙️', callback_data='menu_setting'))
,
        'uk':   InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)
        .add(   InlineKeyboardButton('Ігри 🎮', callback_data='menu_game'))
        .add(   InlineKeyboardButton('Налаштування ⚙️', callback_data='menu_setting'))}

menu_all_test    = {            # КЛАВ-А ПОЛНОГО МЕНЮ ТЕСТОВ

        'ru':   InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)
        .add(   InlineKeyboardButton('Тест депрессии Бека 🫥', callback_data='test_depression_beka'))
        .add(   InlineKeyboardButton('Тест тревожности Бека 😬', callback_data='test_worry_beka'))
        .add(   InlineKeyboardButton('Тест безнадёжности Бека 😔', callback_data='test_hopeless_beka'))
        #.add(   InlineKeyboardButton('⬅️', callback_data='back_list_test'),
        #        InlineKeyboardButton('➡️', callback_data='next_list_test'))
        .add(   InlineKeyboardButton('🔙 Назад в меню', callback_data='toMenu')),

        'uk':   InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)
        .add(   InlineKeyboardButton('Тест депресії Бека 🫥', callback_data='test_depression_beka'))
        .add(   InlineKeyboardButton('Тест тривожності Бека 😬', callback_data='test_worry_beka'))
        .add(   InlineKeyboardButton('Тест безнадійності Бека 😔', callback_data='test_hopeless_beka'))
        #.add(   InlineKeyboardButton('⬅️', callback_data='back_list_test'),
        #        InlineKeyboardButton('➡️', callback_data='next_list_test'))
        .add(   InlineKeyboardButton('🔙 Назад до меню', callback_data='toMenu'))}

# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№ КНОПКИ ОБЩЕГО ВЫБОРА №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

feedback_button        = {      # КЛАВ-А CВЯЗАТЬСЯ С АВТОРОМ ИЛИ ЖЕ НЕТ?

        'ru':   InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)
        .add(   InlineKeyboardButton('Ecтееественно 😏', callback_data='fb_yes'))
        .add(   InlineKeyboardButton('Лучше потом 👋', callback_data='fb_no'))
        ,
        'uk':   InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)
        .add(   InlineKeyboardButton('Ну звісно ж 😏', callback_data='fb_yes'))
        .add(   InlineKeyboardButton('Краще потiм 👋', callback_data='fb_no'))
}

one_two_three_four_TTB = {      # КЛАВ-А ДЛЯ ТЕСТА ТРЕВОЖНОСТИ БЕКА
        'ru':
                InlineKeyboardMarkup(row_width=1, one_time_keyboard=True) \
        .add(   InlineKeyboardButton(text='▫️ 1. Нет, меня это не беспокоило', callback_data='1'),
                InlineKeyboardButton(text='▫️ 2. Как и обычно       ', callback_data='2')) \
        .add(   InlineKeyboardButton(text='▫️ 3. Не очень сильно (неприятно, но я справляюсь)', callback_data='3'),
                InlineKeyboardButton(text='▫️ 4. Очень сильно            ', callback_data='4')) \
        .add(   InlineKeyboardButton(text='❌', callback_data='back_menu_test')),
        
        'uk':
                InlineKeyboardMarkup(row_width=2, one_time_keyboard=True) \
        .add(   InlineKeyboardButton(text='▫️ 1. Ні, це мене не турбувало', callback_data='1'),
                InlineKeyboardButton(text='▫️ 2. Як завжди       	', callback_data='2')) \
        .add(   InlineKeyboardButton(text='▫️ 3. Не дуже сильно (неприємно, але я впораюся)', callback_data='3'),
                InlineKeyboardButton(text='▫️ 4. Дуже сильно             ', callback_data='4')) \
        .add(   InlineKeyboardButton(text='❌', callback_data='back_menu_test')) }

one_two_three_four_TBB = {      # КЛАВ-А ДЛЯ ТЕСТА БЕЗНАДЁЖНОСТИ БЕКА
        'ru':
                InlineKeyboardMarkup(row_width=2, one_time_keyboard=True) \
        .add(   InlineKeyboardButton(text='🔹 Нет, неверно', callback_data='1'),
                InlineKeyboardButton(text='Да, верно 🔸', callback_data='2'))
        .add(   InlineKeyboardButton(text='❌', callback_data='back_menu_test')),


        'uk':
                InlineKeyboardMarkup(row_width=2, one_time_keyboard=True) \
        .add(   InlineKeyboardButton(text='🔹 Нi, невiрно', callback_data='1'),
                InlineKeyboardButton(text='Так, вiрно 🔸', callback_data='2'))
        .add(   InlineKeyboardButton(text='❌', callback_data='back_menu_test')),}

go_to_menu = InlineKeyboardMarkup(row_width=2)                              \
.add(   InlineKeyboardButton(text='🔸 Меню 🔸', callback_data='toMenu'))
go_to_menu_safe = InlineKeyboardMarkup(row_width=2)                          \
.add(   InlineKeyboardButton(text='🔸 Меню 🔸', callback_data='toMenuSafe'))

button_test = InlineKeyboardMarkup(row_width=2)                                \
.add(   InlineKeyboardButton(text='Да, вперед', callback_data='yes_test')) \
.add(   InlineKeyboardButton( text='🔙 Назад', callback_data='back_menu_test'))
one_two_three_four =  InlineKeyboardMarkup(row_width=1, one_time_keyboard=True) \
        .add(         InlineKeyboardButton(text='1', callback_data='1'),
                      InlineKeyboardButton(text='2', callback_data='2')) \
        .add(         InlineKeyboardButton(text='3', callback_data='3'),
                      InlineKeyboardButton(text='4', callback_data='4')) \
        .add(         InlineKeyboardButton(text='❌', callback_data='back_menu_test'))

# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№ ПОДСКАЗКИ ЧИСТО №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

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

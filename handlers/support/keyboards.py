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

board_menu_ru = InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)
"""Меню главного меню. Хе-хе."""
menu_btn_1 = InlineKeyboardButton('Тесты 📊', callback_data='menu_test')
menu_btn_2 = InlineKeyboardButton('Календарь 📅', callback_data='menu_calendar')
menu_btn_3 = InlineKeyboardButton('Игры 🎮', callback_data='menu_game')
menu_btn_4 = InlineKeyboardButton('Настроки ⚙️', callback_data='menu_setting')
board_menu_ru.add(menu_btn_1, menu_btn_2, menu_btn_3)
board_menu_ru.row(menu_btn_4)

board_menu_uk = InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)
"""Меню главного меню. Только на укр. Хе-хе."""
menu_btn_1 = InlineKeyboardButton('Тести 📊', callback_data='menu_test')
menu_btn_2 = InlineKeyboardButton('Календар 📅', callback_data='menu_calendar')
menu_btn_3 = InlineKeyboardButton('Ігри 🎮', callback_data='menu_game')
menu_btn_4 = InlineKeyboardButton('Налаштування ⚙️', callback_data='menu_setting')
board_menu_uk.add(menu_btn_1, menu_btn_2, menu_btn_3)
board_menu_uk.row(menu_btn_4)

sing_up_start1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
sing_up_start1.add(KeyboardButton('Начать работу'))

sing_up_start_cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
sing_up_start_cancel.add(KeyboardButton('Завершить'))

# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№ КНОПКИ ОБЩЕЙ НАСТРОЙКИ №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

feedback_button_ru = InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)
"""Согласие\Несогласие связаться с автором на русском"""
feedback_button_ru.add(InlineKeyboardButton('Ecтееественно 😏', callback_data='fb_yes'))
feedback_button_ru.add(InlineKeyboardButton('Лучше потом 👋', callback_data='fb_no'))


feedback_button_uk = InlineKeyboardMarkup(row_width=2, one_time_keyboard=True).add(InlineKeyboardButton('Ну звісно ж 😏', callback_data='fb_yes'))
"""Согласие\Несогласие связаться с автором на украинском"""
feedback_button_uk.add(InlineKeyboardButton('Ну звісно ж 😏', callback_data='fb_yes'))
feedback_button_uk.add(InlineKeyboardButton('Краще потiм 👋', callback_data='fb_no'))


languageB = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
"""Выбор языка для бота"""
languageB.add(*["Русский", "Українська"])


start_gender_butt_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
"""Выбор пола на русском"""
start_gender_butt_ru.add(*["Я парень 🧔🏽‍♂️", "Я девушка 👱🏼‍♀️"])

start_gender_butt_uk = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
"""Выбор пола на украинском"""
start_gender_butt_uk.add(*["Я хлопець 🧔🏽‍♂️", "Я дівчина 👱🏼‍♀️"])

one_two_three_four = InlineKeyboardMarkup(row_width=3, one_time_keyboard=True)
one_two_three_four.add(InlineKeyboardButton(text='1', callback_data='1'), InlineKeyboardButton(text='2', callback_data='2'))
one_two_three_four.add(InlineKeyboardButton(text='3', callback_data='3'), InlineKeyboardButton(text='4', callback_data='4'))
one_two_three_four.add(InlineKeyboardButton(text='❌', callback_data='back_menu_test'))

button_test = InlineKeyboardMarkup(row_width=2)
button_test.add(InlineKeyboardButton(text='Да, вперед', callback_data='yes_test'))
button_test.add(InlineKeyboardButton( text='🔙 Назад', callback_data='back_menu_test'))

menu_all_test = InlineKeyboardMarkup(row_width=2)
menu_all_test.add(InlineKeyboardButton( text='Тест депрессии Бека 🫥', callback_data='test_depression_beka'))
menu_all_test.add(InlineKeyboardButton(text='🔙 Назад', callback_data='toMenu'))


go_to_menu = InlineKeyboardMarkup(row_width=2)
go_to_menu.add(InlineKeyboardButton(text='🔸 Меню 🔸', callback_data='toMenu'))

# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№ КНОПКИ ГЛУБОКИХ НАСТРОЕК №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

setting_button_ru_men = InlineKeyboardMarkup(row_width=2)
setting_button_ru_men.add(InlineKeyboardButton(text='🔙 Назад', callback_data='toMenu'))
setting_button_ru_men.add(InlineKeyboardButton(text='  ✅  Я парень 👨  ✅  ||   Я девушка 👩   ', callback_data='setting_gender_ru'))
setting_button_ru_men.add(InlineKeyboardButton(text='  ✅  Русский  ✅  ||   Українська    ', callback_data='setting_language_uk'))

setting_button_uk_men = InlineKeyboardMarkup(row_width=2)
setting_button_uk_men.add(InlineKeyboardButton(text='🔙 Назад', callback_data='toMenu'))
setting_button_uk_men.add(InlineKeyboardButton(text='  ✅  Я хлопець 👨  ✅  ||   Я дівчина 👩   ', callback_data='setting_gender_uk'))
setting_button_uk_men.add(InlineKeyboardButton(text='   Русский   ||   ✅  Українська  ✅ ', callback_data='setting_language_ru'))

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

setting_button_ru_women = InlineKeyboardMarkup(row_width=2)
setting_button_ru_women.add(InlineKeyboardButton(text='🔙 Назад', callback_data='toMenu'))
setting_button_ru_women.add(InlineKeyboardButton(text='   Я парень 👨   ||  ✅ Я девушка 👩 ✅  ', callback_data='setting_gender_ru'))
setting_button_ru_women.add(InlineKeyboardButton(text='  ✅  Русский  ✅  ||   Українська    ', callback_data='setting_language_uk'))

setting_button_uk_women = InlineKeyboardMarkup(row_width=2)
setting_button_uk_women.add(InlineKeyboardButton(text='🔙 Назад', callback_data='toMenu'))
setting_button_uk_women.add(InlineKeyboardButton(text='  Я хлопець 👨   ||  ✅ Я дівчина 👩 ✅ ', callback_data='setting_gender_uk'))
setting_button_uk_women.add(InlineKeyboardButton(text='   Русский   ||   ✅  Українська  ✅ ', callback_data='setting_language_ru'))

from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

"""Добавить обычную кнопку"""
#tst.kld = ReplyKeyboardMarkup(resize_keyboard=True)
#buttons = ["Тесты", "Календарь"]
#keyboard.add(*buttons)

"""Удалить кнопку"""
#await message.answer( reply_markup=ReplyKeyboardRemove())

"""Добавить обычную кнопку исчезающую"""
#keyboard = .ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#buttons = ["Тесты", "Календарь"]
#keyboard.add(*buttons)

#№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№ КНОПКИ МЕНЮ №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

board_menu = InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)
"""Меню главного меню. Хе-хе."""
menu_btn_1 = InlineKeyboardButton('Тесты 📊', callback_data='menu_test')
menu_btn_2 = InlineKeyboardButton('Календарь 📅', callback_data='menu_calendar')
menu_btn_3 = InlineKeyboardButton('Игры 🎮', callback_data='menu_game')
menu_btn_4 = InlineKeyboardButton('Настроки ⚙️', callback_data='menu_setting')
#menu_btn_5 = InlineKeyboardButton('кнопка 5', callback_data='btn5')
board_menu.add(menu_btn_1, menu_btn_2, menu_btn_3)
board_menu.row(menu_btn_4)


#№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№ КНОПКИ ОБЩЕЙ НАСТРОЙКИ №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

fbBRu = InlineKeyboardMarkup(row_width=2, one_time_keyboard=True).add(InlineKeyboardButton('Ecтееественно 😏', callback_data='fb_yes'))
"""Согласие\Несогласие связаться с автором на русском"""
fbBRu.add(InlineKeyboardButton('Лучше потом 👋', callback_data='fb_no'))

fbBUa = InlineKeyboardMarkup(row_width=2, one_time_keyboard=True).add(InlineKeyboardButton('Ну звісно ж 😏', callback_data='fb_yes'))
"""Согласие\Несогласие связаться с автором на украинском"""
fbBUa.add(InlineKeyboardButton('Краще потiм 👋', callback_data='fb_no'))


languageB = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
"""Выбор языка для бота"""
language_buttons = ["Русский", "Українська"]
languageB.add(*language_buttons)

start_gender_butt_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
"""Выбор пола на русском"""
start_gender_butt_uk = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
"""Выбор пола на украинском"""
    
#start_gender_butt_ru = ["Я парень 🧔🏽‍♂️", "Я девушка 👱🏼‍♀️"]
#start_gender_butt_uk = ["Я хлопець 🧔🏽‍♂️", "Я дівчина 👱🏼‍♀️"]

start_gender_butt_ru.add(*["Я парень 🧔🏽‍♂️", "Я девушка 👱🏼‍♀️"])
start_gender_butt_uk.add(*["Я хлопець 🧔🏽‍♂️", "Я дівчина 👱🏼‍♀️"])

#№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№ КНОПКИ ГЛУБОКИХ НАСТРОЕК №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

setting_button_ru_men = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='  ✅  Я парень 👨  ✅  ||   Я девушка 👩   ', callback_data='setting_gender_ru'))
setting_button_ru_men.add(InlineKeyboardButton(text='  ✅  Русский  ✅  ||   Українська    ', callback_data='setting_language_uk'))

setting_button_uk_men = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='  ✅  Я хлопець 👨  ✅  ||   Я дівчина 👩   ', callback_data='setting_gender_uk'))
setting_button_uk_men.add(InlineKeyboardButton(text='   Русский   ||   ✅  Українська  ✅ ', callback_data='setting_language_ru'))

#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

setting_button_ru_women = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='   Я парень 👨   ||  ✅ Я девушка 👩 ✅  ', callback_data='setting_gender_ru'))
setting_button_ru_women.add(InlineKeyboardButton(text='  ✅  Русский  ✅  ||   Українська    ', callback_data='setting_language_uk'))

setting_button_uk_women = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(text='  Я хлопець 👨   ||  ✅ Я дівчина 👩 ✅ ', callback_data='setting_gender_uk'))
setting_button_uk_women.add(InlineKeyboardButton(text='   Русский   ||   ✅  Українська  ✅ ', callback_data='setting_language_ru'))
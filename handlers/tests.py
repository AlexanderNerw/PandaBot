from handlers.support.importing import *

class AnswerTest(StatesGroup):  # МАШИНА СОСТРОЯНИЙ ДЛЯ ТЕСТОВ
    answerNum = State()
    answerLang = State()
    answerEnd = State()
    text = State()
    TDB = State()
    TBB = State()
    TTB = State()

@dp.callback_query_handler(text='back_menu_test', state='*')   # ВОЗВРАТ НАЗАД
async def question_back(call: CallbackQuery, state: FSMContext):
    try:
        await state.reset_data()
        await state.finish()
        db.adding(call.message.chat.id, 'notice', 1)
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(call.message.chat.id, f"Добре, назад до меню:", parse_mode='html')
        await tests(call.message.chat.id, call.message.message_id+1)

    except Exception as ex: 
        await bot.send_message(ADMIN[1], f'tests.py [INFO] Неполадки в question_back: {ex}')
        print(f'tests.py [INFO] Неполадки в question_back: {ex}')


try: # TEST DEPRESSION BEKA 

    # МЕНЮ ТЕСТ ДЕПРЕССИИ ТЕСТА ДЕПРЕССИИ БЕКА
    @dp.callback_query_handler(text='test_depression_beka')
    async def menu_test_depression_beka(call: CallbackQuery) -> None:
        
        await bot.edit_message_text(test_depression_beka_result[db.getting(call.message.chat.id, 'language')],
        call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=button_test)
        db.adding(call.message.chat.id, 'notice', 0)
        await AnswerTest.TDB.set()
        
    # ВОПРОС 1
    @dp.callback_query_handler(text='yes_test', state=AnswerTest.TDB)
    async def question1_TDB(call: CallbackQuery, state: FSMContext):

        async with state.proxy() as data:
            state.reset_data()
            data['answerLang'] = db.getting(call.message.chat.id, 'language')
            data['answerNum'] = 1 
            data['answerEnd'] = 0

        db.adding(call.message.chat.id, 'TDBeka', 'TDBeka: ', database='answer_test')

        await bot.edit_message_text(test_depression_beka[f"answer_{data['answerNum']}_{data['answerLang']}"],
        call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
 
    # ОБЩАЯ ФОРМА ДЛЯ ВОПРОСОВ БЕКА
    @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTest.TDB)
    async def questions_TDB(call: CallbackQuery, state: FSMContext): 
        try:

            async with state.proxy() as data:
                data['answerEnd'] += int(call.data)-1
                await bot.delete_message(call.message.chat.id, call.message.message_id), await call.answer()
                db.addingEndStart(call.message.chat.id, 'TDBeka', f", answr{str(data['answerNum'])}: {str(int(call.data)-1)}")

                if data['answerNum'] < 21:
                    data['answerNum'] += 1
                    await bot.send_message(call.message.chat.id, test_depression_beka[f"answer_{data['answerNum']}_{data['answerLang']}"],
                                        parse_mode='html', reply_markup=one_two_three_four)

                else: 

                    if data['answerEnd'] < 10:                               data["text"] = '0-9'
                    elif data['answerEnd'] >= 10 and data['answerEnd'] < 16: data["text"] = '10-15'
                    elif data['answerEnd'] >= 16 and data['answerEnd'] < 20: data["text"] = '16-19'
                    elif data['answerEnd'] >= 20 and data['answerEnd'] < 30: data["text"] = '20-29'
                    elif data['answerEnd'] >= 30:                            data["text"] = '30-63'

                    await bot.send_message(call.message.chat.id, f"<b>Ваш результат: {data['answerEnd']} {'из 63 баллов' if data['answerLang'] == 'ru' else 'з 63 балів'}</b>\n\n"
                    + test_depression_beka_result[f"{data['answerLang']}{data['text']}"], reply_markup=go_to_menu_safe, parse_mode='html')
                    
                    db.addingEndStart(call.message.chat.id, 'TDB', f"{data['answerEnd']} ")
                    db.adding(call.message.chat.id, 'notice', 1)
                    await state.reset_data()
                    await state.finish()

        except Exception as ex:
            if str(ex) != 'Message to delete not found':
                print(f'tests.py [INFO] Неполадки в {data["answerNum"]} questions_TDB Теста Депрессии Бека: {ex}')
except Exception as ex: # TEST DEPRESSION BEKA 
    print(f'tests.py [INFO] Неполадки в Тесте Депрессии Бека: {ex}')


try:  # ТЕСТ ТРЕВОЖНОСТИ БЕКА

    # МЕНЮ ТЕСТ ТРЕВОЖНОСТИ БЕКА
    @dp.callback_query_handler(text='test_worry_beka')
    async def menu_test_worry_beka(call: CallbackQuery) -> None:
        
        await bot.edit_message_text(test_worry_beka_result[db.getting(call.message.chat.id, 'language')],
        call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=button_test)
        db.adding(call.message.chat.id, 'notice', 0)
        await AnswerTest.TTB.set()

    # ВОПРОС 1
    @dp.callback_query_handler(text='yes_test', state=AnswerTest.TTB)
    async def question1_TTB(call: CallbackQuery, state: FSMContext):
        async with state.proxy() as data:

            await state.reset_data()
            data['answerLang'] = db.getting(call.message.chat.id, 'language')
            data['answerNum'] = 1 
            data['answerEnd'] = 0
        
        db.adding(call.message.chat.id, 'TTBeka', 'TTBeka: ', database='answer_test')
        await bot.edit_message_text(    test_worry_beka[f"answer_start_{data['answerLang']}"]
                                    +   test_worry_beka[f"answer_{data['answerNum']}_{data['answerLang']}"],
        call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four_TTB[data['answerLang']])
 
    # ОБЩАЯ ФОРМА ДЛЯ ВОПРОСОВ ТЕСТА ТРЕВОЖНОСТИ БЕКА
    @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTest.TTB)
    async def questions_TTB(call: CallbackQuery, state: FSMContext): 
        try:

            async with state.proxy() as data:
                data['answerEnd'] += int(call.data)-1
                await bot.delete_message(call.message.chat.id, call.message.message_id), await call.answer()
                db.addingEndStart(call.message.chat.id, 'TTBeka', f", answr{str(data['answerNum'])}: {str(int(call.data)-1)}")

                if data['answerNum'] < 21:
                    data['answerNum'] += 1
                    await bot.send_message(call.message.chat.id, test_worry_beka[f"answer_start_{data['answerLang']}"]
                                                               + test_worry_beka[f"answer_{data['answerNum']}_{data['answerLang']}"],
                                                                 parse_mode='html', reply_markup=one_two_three_four_TTB[data['answerLang']])

                else: 

                    if data['answerEnd'] < 10:                                  data['text'] = '0-9'
                    elif data['answerEnd'] >= 10 and data['answerEnd'] < 22:    data['text'] = '10-21'
                    elif data['answerEnd'] >= 22 and data['answerEnd'] < 36:    data['text'] = '22-35'
                    elif data['answerEnd'] >= 36 and data['answerEnd'] < 30:    data['text'] = '36-63'

                    await bot.send_message(call.message.chat.id, f"<b>Ваш результат: {data['answerEnd']} {'из 63 баллов' if data['answerLang'] == 'ru' else 'з 63 балів'}</b>\n\n"
                                        + test_worry_beka_result[f"{data['answerLang']}{data['text']}"], reply_markup=go_to_menu_safe, parse_mode='html')
                    db.adding(call.message.chat.id, 'notice', 1)
                    db.addingEndStart(call.message.chat.id, 'TTBeka', f"{data['answerEnd']} ")
                    await state.reset_data()
                    await state.finish()

        except Exception as ex:
            if str(ex) != 'Message to delete not found':
                print(f'tests.py [INFO] Неполадки в questions_TDB Теста Тревожности Бека: {ex}')

        finally: await call.answer()
except Exception as ex: # TEST DEPRESSION BEKA 
    print(f'tests.py [INFO] Неполадки в Тесте Тревожности Бека: {ex}')


try:  # ТЕСТ БЕЗНАДЁЖНОСТИ БЕКА

    # МЕНЮ ТЕСТ БЕЗНАДЁЖНОСТИ БЕКА
    @dp.callback_query_handler(text='test_hopeless_beka')
    async def menu_test_hopeless_beka(call: CallbackQuery) -> None:
        
        await bot.edit_message_text(test_depression_beka_result[db.getting(call.message.chat.id, 'language')],
        call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=button_test)
        db.adding(call.message.chat.id, 'notice', 0)
        await AnswerTest.TBB.set()

    # ВОПРОС 1
    @dp.callback_query_handler(text='yes_test', state=AnswerTest.TBB)
    async def question1_TBB(call: CallbackQuery, state: FSMContext):

        async with state.proxy() as data:
            await state.reset_data()
            data['answerLang'] = db.getting(call.message.chat.id, 'language')
            data['answerNum'] = 1 
            data['answerEnd'] = 0

        db.adding(call.message.chat.id, 'TBBeka', 'TBBeka: ', database='answer_test')
        await bot.edit_message_text(test_worry_beka[f"answer_{data['answerNum']}_{data['answerLang']}"],
        call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four_TBB[data['answerLang']])
 
    # ОБЩАЯ ФОРМА ДЛЯ ВОПРОСОВ ТЕСТА БЕЗНАДЁЖНОСТИ БЕКА
    @dp.callback_query_handler(text=['1', '2'], state=AnswerTest.TBB)
    async def questions_TBB(call: CallbackQuery, state: FSMContext): 
        try:
            print(type(call.data))
            async with state.proxy() as data:
                if data['answerNum'] in [2, 4, 7, 9, 11, 12, 15, 16, 17, 18, 20]:
                    if call.data == '2': data['answerEnd'] += 1

                elif data['answerNum'] in [1, 3, 5, 6, 8, 10, 13, 15, 19]:
                    if call.data == '1': data['answerEnd'] += 1

                await bot.delete_message(call.message.chat.id, call.message.message_id), await call.answer()
                db.addingEndStart(call.message.chat.id, 'TBBeka', f", answr{str(data['answerNum'])}: {str(int(call.data)-1)}")

                if data['answerNum'] < 20:
                    data['answerNum'] += 1
                    await bot.send_message( call.message.chat.id, test_hopeless_beka[f"answer_{data['answerNum']}_{data['answerLang']}"],
                                            parse_mode='html', reply_markup=one_two_three_four_TBB[data['answerLang']])

                else: 
                    if data['answerEnd'] < 4:                                   data['text'] = '0–3'
                    elif data['answerEnd'] >= 4 and data['answerEnd'] < 9:      data['text'] = '4–8'
                    elif data['answerEnd'] >= 9 and data['answerEnd'] < 15:     data['text'] = '9–14'
                    elif data['answerEnd'] >= 15:                               data['text'] = '15–20'

                    await bot.send_message(call.message.chat.id, f"<b>Ваш результат: {data['answerEnd']} {'из 20 баллов' if data['answerLang'] == 'ru' else 'з 20 балів'}</b>\n\n"
                                        + test_worry_beka_result[f"{data['answerLang']}_{data['text']}"], reply_markup=go_to_menu_safe, parse_mode='html')
                    db.addingEndStart(call.message.chat.id, 'TBB', f"{data['answerEnd']} ")
                    db.adding(call.message.chat.id, 'notice', 1)
                    await state.reset_data()
                    await state.finish()

        except Exception as ex:
            if str(ex) != 'Message to delete not found':
                print(f'tests.py [INFO] Неполадки в questions_TDB Теста Депрессии Бека: {ex}')

        finally: await call.answer()
except Exception as ex: # TEST DEPRESSION BEKA 
    print(f'tests.py [INFO] Неполадки в Тесте Безнадёжности Бека: {ex}')


async def tests(chat_id, message_id):
    try:
        
        await bot.delete_message(chat_id, message_id)
        await bot.send_message(chat_id, f"🧾 " + general_text[f"{db.getting(chat_id, 'language')}_list_tests"],
        parse_mode='html', reply_markup=menu_all_test[db.getting(chat_id, 'language')])

    except Exception as ex: 
        bot.send_message(ADMIN[1], f'tests.py [INFO] Неполадки в Меню Тестов: {ex}' )
        print(f'tests.py [INFO] Неполадки в Меню Тестов: {ex}')
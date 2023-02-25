from handlers.support.importing import *

class AnswerTest(StatesGroup):  # МАШИНА СОСТРОЯНИЙ ДЛЯ ТЕСТОВ
    answerNum = State()
    answerLang = State()
    answerEnd = State()
    answerDict = State()


@dp.callback_query_handler(text='back_menu_test', state='*')   # ВОЗВРАТ НАЗАД
async def question_back(call: CallbackQuery, state: FSMContext):
    try:
        await state.reset_data()
        await state.finish()
        db.adding(call.message.chat.id, 'notice', 1)
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(call.message.chat.id, f"Добре, назад до меню:", parse_mode='html')
        await tests(call.message.chat.id, call.message.message_id+1)
        print(f"Id: {call.message.chat.id} | Закончил проходить тест")

    except Exception as ex: 
        await bot.send_message(ADMIN[1], f'tests.py [INFO] Неполадки в question_back: {ex}')
        print(f'tests.py [INFO] Неполадки в question_back: {ex}')


try: # TEST DEPRESSION BEKA 

    # МЕНЮ ТЕСТ ДЕПРЕССИИ ТЕСТА ДЕПРЕССИИ БЕКА
    @dp.callback_query_handler(text='test_depression_beka')
    async def menu_test_depression_beka(call: CallbackQuery) -> None:
        
        lang = db.getting(call.message.chat.id, 'language')
        await bot.edit_message_text(test_depression_beka_result[lang],
        call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=button_test)
        db.adding(call.message.chat.id, 'notice', 0)
        await AnswerTest.answerNum.set()
        
    # ВОПРОС 1
    @dp.callback_query_handler(text='yes_test', state=AnswerTest.answerNum)
    async def question1(call: CallbackQuery, state: FSMContext):

        async with state.proxy() as data:
            data['answerLang'] = db.getting(call.message.chat.id, 'language')
            data['answerNum'] = 1 
            data['answerEnd'] = 0

        print(f"Id: {call.message.chat.id} | Начал проходить тест")
        await bot.edit_message_text(test_depression_beka[f"answer_{data['answerNum']}_{data['answerLang']}"],
        call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
 
    # ОБЩАЯ ФОРМА ДЛЯ ВОПРОСОВ БЕКА
    @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTest.answerNum)
    async def questions_TDB(call: CallbackQuery, state: FSMContext): 

        try:

            async with state.proxy() as data: data['answerEnd'] += int(call.data)-1

            await bot.delete_message(call.message.chat.id, call.message.message_id), await call.answer()

            if data['answerNum'] < 21:
                async with state.proxy() as data:data['answerNum'] += 1

                db.addingInEnd(call.message.chat.id, 'TDBeka', f", answr{str(data['answerNum'])}: {str(int(call.data)-1)}")
                await bot.send_message(call.message.chat.id, test_depression_beka[f"answer_{data['answerNum']}_{data['answerLang']}"],
                                       parse_mode='html', reply_markup=one_two_three_four)

            else: 

                result_point = 'из 63 баллов' if data['answerLang'] == 'ru' else 'з 63 балів'

                if data['answerEnd'] < 10:                               text = '0-9'
                elif data['answerEnd'] >= 10 and data['answerEnd'] < 16: text = '10-15'
                elif data['answerEnd'] >= 16 and data['answerEnd'] < 20: text = '16-19'
                elif data['answerEnd'] >= 20 and data['answerEnd'] < 30: text = '20-29'
                elif data['answerEnd'] >= 30:                            text = '30-63'

                await bot.send_message(call.message.chat.id, f"<b>Ваш результат: {data['answerEnd']} {result_point}</b>\n\n"
                + test_depression_beka_result[f"{data['answerLang']}{text}"], reply_markup=go_to_menu, parse_mode='html')

                print(f"Id: {call.message.chat.id} | Закончил проходить тест")
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
    @dp.callback_query_handler(text='test_depression_beka')
    async def menu_test_depression_beka(call: CallbackQuery) -> None:
        
        await bot.edit_message_text(test_worry_beka_result[db.getting(call.message.chat.id, 'language')],
        call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=button_test)
        await AnswerTest.answerNum.set()
        db.adding(call.message.chat.id, 'notice', 0)

    # ВОПРОС 1
    @dp.callback_query_handler(text='yes_test', state=AnswerTest.answerNum)
    async def question1(call: CallbackQuery, state: FSMContext):

        async with state.proxy() as data:
            data['answerLang'] = db.getting(call.message.chat.id, 'language')
            data['answerNum'] = 1 
            data['answerEnd'] = 0

        print(f"Id: {call.message.chat.id} | Начал проходить тест")
        
        await bot.edit_message_text(    test_worry_beka[f"answer_start_{data['answerLang']}"]
                                    +   test_worry_beka[f"answer_{data['answerNum']}_{data['answerLang']}"]
                                    +   test_worry_beka[f"answer_{data['answerLang']}"],
        call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
 
    # ОБЩАЯ ФОРМА ДЛЯ ВОПРОСОВ ТЕСТА ТРЕВОЖНОСТИ БЕКА
    @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTest.answerNum)
    async def questions_TWB(call: CallbackQuery, state: FSMContext): 

        try:

            async with state.proxy() as data: data['answerEnd'] += int(call.data)-1
            await bot.delete_message(call.message.chat.id, call.message.message_id), await call.answer()

            if data['answerNum'] < 21:
                async with state.proxy() as data: data['answerNum'] += 1

                db.addingInEnd(call.message.chat.id, 'TTBeka', f", answr{str(data['answerNum'])}: {str(int(call.data)-1)}")
                await bot.send_message(call.message.chat.id, test_worry_beka[f"answer_start_{data['answerLang']}"]
                                                           + test_worry_beka[f"answer_{data['answerNum']}_{data['answerLang']}"]
                                                           + test_worry_beka[f"answer_{data['answerLang']}"], parse_mode='html', reply_markup=one_two_three_four)

            else: 

                result_point_text = 'из 63 баллов' if data['answerLang'] == 'ru' else 'з 63 балів'

                if data['answerEnd'] < 10:
                    text = '0-9'
                elif data['answerEnd'] >= 10 and data['answerEnd'] < 16:
                    text = '10-15'
                elif data['answerEnd'] >= 16 and data['answerEnd'] < 20:
                    text = '16-19'
                elif data['answerEnd'] >= 20 and data['answerEnd'] < 30:
                    text = '20-29'
                elif data['answerEnd'] >= 30:
                    text = '30-63'

                await bot.send_message(call.message.chat.id, f"<b>Ваш результат: {data['answerEnd']} {result_point_text}</b>\n\n" + test_worry_beka_result[f"{data['answerLang']}{text}"],
                                reply_markup=go_to_menu, parse_mode='html')
                print(f"Id: {call.message.chat.id} | Закончил проходить тест")
                db.adding(call.message.chat.id, 'notice', 1)
                await state.reset_data()
                await state.finish()

        except Exception as ex:
            if str(ex) != 'Message to delete not found':
                print(f'tests.py [INFO] Неполадки в questions_TDB Теста Депрессии Бека: {ex}')

        finally: await call.answer()
except Exception as ex: # TEST DEPRESSION BEKA 
    print(f'tests.py [INFO] Неполадки в Тесте Тревожности Бека: {ex}')


try:  # ТЕСТ БЕЗНАДЁЖНОСТИ БЕКА

    # МЕНЮ ТЕСТ БЕЗНАДЁЖНОСТИ БЕКА
    @dp.callback_query_handler(text='test_depression_beka')
    async def menu_test_depression_beka(call: CallbackQuery) -> None:
        
        lang = db.getting(call.message.chat.id, 'language')
        await bot.edit_message_text(test_depression_beka_result[lang],
        call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=button_test)
        db.adding(call.message.chat.id, 'notice', 0)
        await AnswerTest.answerNum.set()

    # ВОПРОС 1
    @dp.callback_query_handler(text='yes_test', state=AnswerTest.answerNum)
    async def question1(call: CallbackQuery, state: FSMContext):

        async with state.proxy() as data:
            data['answerLang'] = db.getting(call.message.chat.id, 'language')
            data['answerNum'] = 1 
            data['answerEnd'] = 0

        print(f"Id: {call.message.chat.id} | Начал проходить тест")

        await bot.edit_message_text(test_worry_beka[f"answer_{data['answerNum']}_{data['answerLang']}"],
        call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
 
    # ОБЩАЯ ФОРМА ДЛЯ ВОПРОСОВ ТЕСТА БЕЗНАДЁЖНОСТИ БЕКА
    @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTest.answerNum)
    async def questions_TWB(call: CallbackQuery, state: FSMContext): 
        try:

            async with state.proxy() as data:data['answerEnd'] += int(call.data)-1
            await bot.delete_message(call.message.chat.id, call.message.message_id), await call.answer()

            if data['answerNum'] < 21:
                async with state.proxy() as data: data['answerNum'] += 1
                
                db.addingInEnd(call.message.chat.id, 'TBBeka', f", answr{str(data['answerNum'])}: {str(int(call.data)-1)}")
                await bot.send_message(call.message.chat.id, f"Насколько сильно Вас беспокоило данное ощущение за последнюю неделю:\n\n{1}",
                parse_mode='html', reply_markup=one_two_three_four)

            else: 

                result_point_text = 'из 63 баллов' if data['answerLang'] == 'ru' else 'з 63 балів'

                if data['answerEnd'] < 10:
                    text = '0-9'
                elif data['answerEnd'] >= 10 and data['answerEnd'] < 16:
                    text = '10-15'
                elif data['answerEnd'] >= 16 and data['answerEnd'] < 20:
                    text = '16-19'
                elif data['answerEnd'] >= 20 and data['answerEnd'] < 30:
                    text = '20-29'
                elif data['answerEnd'] >= 30:
                    text = '30-63'

                lang = data['answerLang']
                await bot.send_message(call.message.chat.id, f"<b>Ваш результат: {data['answerEnd']} {result_point_text}</b>\n\n{test_worry_beka_result[f'{lang}{text}']}",
                                reply_markup=go_to_menu, parse_mode='html')
                db.adding(call.message.chat.id, 'notice', 1)
                print(f"Id: {call.message.chat.id} | Закончил проходить тест")
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
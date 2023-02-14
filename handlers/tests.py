from aiogram.dispatcher.filters.state import State, StatesGroup
from handlers.config import dp, bot, Dispatcher, ADMIN
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from handlers.querry_db import db
from handlers.keyboards import *
from handlers.dialogs import *
import menu


try:  # TEST DEPRESSION BEKA 

    class AnswerTDB(StatesGroup):
        answerNum = State()
        answerLang = State()

    # МЕНЮ ТЕСТ ДЕПРЕССИИ БЕКА
    @dp.callback_query_handler(text='test_depression_beka')
    async def menu_test_depression_beka(call: CallbackQuery) -> None:
        
        lang = db.getting(call.message.chat.id, 'language')
        await bot.edit_message_text(test_depression_beka_entry[lang],
        call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=button_test)
        await AnswerTDB.answerNum.set()

    # ВОЗВРАТ НАЗАД
    @dp.callback_query_handler(text='back_menu_test', state=AnswerTDB)
    async def question_back(call: CallbackQuery, state: FSMContext):

        await state.finish()
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(call.message.chat.id, f"Добре, назад до меню:", parse_mode='html')
        await tests(call.message.chat.id, call.message.message_id+1)
        print(f"Id: {call.message.chat.id} | Закончил проходить тест")
        
    # ВОПРОС 1
    @dp.callback_query_handler(text='yes_test', state=AnswerTDB.answerNum)
    async def question1(call: CallbackQuery, state: FSMContext):

        async with state.proxy() as data:
            data['answerLang'] = db.getting(call.message.chat.id, 'language')
            data['answerNum'] = 1 
            data['answerEnd'] = 0

        print(f"Id: {call.message.chat.id} | Начал проходить тест")
        await bot.edit_message_text(test_depression_beka[f"answer_{data['answerNum']}_{data['answerLang']}"],
        call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
 
    # ОБЩАЯ ФОРМА ДЛЯ ВОПРОСОВ БЕКА
    @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answerNum)
    async def questions_TDB(call: CallbackQuery, state: FSMContext): 

        try:
            await call.answer()

            async with state.proxy() as data:
                data['answerEnd'] += int(call.data)-1
                lang = data['answerLang']

            await bot.delete_message(call.message.chat.id, call.message.message_id)

            if data['answerNum'] < 21:
                async with state.proxy() as data:
                    data['answerNum'] += 1
                
                await bot.send_message(call.message.chat.id, test_depression_beka[f"answer_{data['answerNum']}_{lang}"],
                parse_mode='html', reply_markup=one_two_three_four)

            else: 

                result_point = 'из 63 баллов' if lang == 'ru' else 'з 63 балів'
                lang = data['answerLang']

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

                await bot.send_message(call.message.chat.id, f"<b>Ваш результат: {data['answerEnd']} {result_point}</b>\n\n{test_depression_beka_result[f'{lang}{text}']}",
                                reply_markup=go_to_menu, parse_mode='html')
                print(f"Id: {call.message.chat.id} | Закончил проходить тест")
                await state.finish()

        except Exception as ex:
            if str(ex) != 'Message to delete not found':
                print(f'tests.py [INFO] Неполадки в questions_TDB Теста Депрессии Бека: {ex}')

        finally: await call.answer()

except Exception as ex: # TEST DEPRESSION BEKA 
    print(f'tests.py [INFO] Неполадки в Тесте Депрессии Бека: {ex}')


async def tests(chat_id, message_id):
    lang = db.getting(chat_id, 'language')
    await bot.delete_message(chat_id, message_id)
    await bot.send_message(chat_id, f"🧾 {general_text_answer[f'{lang}_list_tests']}\n",
    parse_mode='html', reply_markup=menu_all_test)

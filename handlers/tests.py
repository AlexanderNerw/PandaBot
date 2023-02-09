from aiogram.dispatcher.filters.state import State, StatesGroup
from handlers.config import dp, bot, Dispatcher, ADMIN
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from handlers.keyboards import *
from handlers.dialogs import *

class AnswerTDB(StatesGroup):
   answer1 = State()
   answer2 = State()
   answer3 = State()
   answer4 = State()
   answer5 = State()
   answer6 = State()
   answer7 = State()
   answer8 = State()
   answer9 = State()
   answer10 = State()
   answer11 = State()
   answer12 = State()
   answer13 = State()
   answer14 = State()
   answer15 = State()
   answer16 = State()
   answer17 = State()
   answer18 = State()
   answer19 = State()
   answer20 = State()
   answer21 = State()


@dp.message_handler(commands=['cancel'], state='*')
async def get_cancel_depression_beka(message: Message, state: FSMContext) -> None:

    try:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await tests(message)

    except Exception as ex:
        await bot.send_message(ADMIN[1], 'tests.py [INFO] Неполадки в get_cancel_depression_beka: ', ex)
        print('tests.py [INFO] Неполадки в get_cancel_depression_beka: ', ex)

#@dp.message_handler(text=['text'], state=AnswerTDB.answer1)
async def test_depression_beka(message: Message) -> None:
   await bot.send_message(message.chat.id, "Готовы пройти тест?", reply_markup=button_test)
   await AnswerTDB.answer1.set()

@dp.callback_query_handler(text='Да, вперед', state=AnswerTDB.answer1) 
async def question1(call: CallbackQuery):
   await bot.send_message(call.message.chat.id, f"Вопрос 1/21:\n{depression_beka1['0']}\n\n{depression_beka1['1']}\n\n{depression_beka1['2']}\n\n{depression_beka1['3']}", 
   parse_mode='html', reply_markup=one_two_three_four)
   await AnswerTDB.next()

@dp.callback_query_handler(text='🔙 Назад', state=AnswerTDB)
async def question_back(call: CallbackQuery):
   await bot.send_message(call.message.chat.id,f"Добре",parse_mode='html', reply_markup=ReplyKeyboardRemove())
   await tests(call.message)

@dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer2)
async def question2(call: CallbackQuery, state: FSMContext):

   await bot.send_message(call.message.chat.id,f"Вопрос 2/21:\n{depression_beka2['0']}\n\n{depression_beka2['1']}\n\n{depression_beka2['2']}\n\n{depression_beka2['3']}", 
   parse_mode='html', reply_markup=one_two_three_four)
   print(call.message)
   async with state.proxy() as data:
      data['answer1'] = 0

@dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer3)
async def question3(message: Message, state: FSMContext):
    await message.answer(f"Вопрос 3/21:\n{depression_beka3['0']}\n\n{depression_beka3['1']}\n\n{depression_beka3['2']}\n\n{depression_beka3['3']}", parse_mode='html')

@dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer4)
async def question4(message: Message, state: FSMContext):
    await message.answer(f"Вопрос 4/21:\n{depression_beka4['0']}\n\n{depression_beka4['1']}\n\n{depression_beka4['2']}\n\n{depression_beka4['3']}", parse_mode='html')

@dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer5)
async def question5(message: Message, state: FSMContext):
    await message.answer(f"Вопрос 5/21:\n{depression_beka5['0']}\n\n{depression_beka5['1']}\n\n{depression_beka5['2']}\n\n{depression_beka5['3']}", parse_mode='html')

@dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer6)
async def question6(message: Message, state: FSMContext):
    await message.answer(f"Вопрос 6/21:\n{depression_beka6['0']}\n\n{depression_beka6['1']}\n\n{depression_beka6['2']}\n\n{depression_beka6['3']}", parse_mode='html')

@dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer7)
async def question7(message: Message, state: FSMContext):
    await message.answer(f"Вопрос 7/21:\n{depression_beka7['0']}\n\n{depression_beka7['1']}\n\n{depression_beka7['2']}\n\n{depression_beka7['3']}", parse_mode='html')

@dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer8)
async def question8(message: Message, state: FSMContext):
    await message.answer(f"Вопрос 8/21:\n{depression_beka8['0']}\n\n{depression_beka8['1']}\n\n{depression_beka8['2']}\n\n{depression_beka8['3']}", parse_mode='html')

@dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer9)
async def question9(message: Message, state: FSMContext):
    await message.answer(f"Вопрос 9/21:\n{depression_beka9['0']}\n\n{depression_beka9['1']}\n\n{depression_beka9['2']}\n\n{depression_beka9['3']}", parse_mode='html')

@dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer10)
async def question10(message: Message, state: FSMContext):
    await message.answer(f"Вопрос 10/21:\n{depression_beka10['0']}\n\n{depression_beka10['1']}\n\n{depression_beka10['2']}\n\n{depression_beka10['3']}", parse_mode='html')

@dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer11)
async def question11(message: Message, state: FSMContext):
    await message.answer(f"Вопрос 11/21:\n{depression_beka11['0']}\n\n{depression_beka11['1']}\n\n{depression_beka11['2']}\n\n{depression_beka11['3']}", parse_mode='html')

@dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer12)
async def question12(message: Message, state: FSMContext):
    await message.answer(f"Вопрос 12/21:\n{depression_beka12['0']}\n\n{depression_beka12['1']}\n\n{depression_beka12['2']}\n\n{depression_beka12['3']}", parse_mode='html')

@dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer13)
async def question13(message: Message, state: FSMContext):
    await message.answer(f"Вопрос 13/21:\n{depression_beka13['0']}\n\n{depression_beka13['1']}\n\n{depression_beka13['2']}\n\n{depression_beka13['3']}", parse_mode='html')

@dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer14)
async def question14(message: Message, state: FSMContext):
    await message.answer(f"Вопрос 14/21:\n{depression_beka14['0']}\n\n{depression_beka14['1']}\n\n{depression_beka14['2']}\n\n{depression_beka14['3']}", parse_mode='html')

@dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer15)
async def question15(message: Message, state: FSMContext):
    await message.answer(f"Вопрос 15/21:\n{depression_beka15['0']}\n\n{depression_beka15['1']}\n\n{depression_beka15['2']}\n\n{depression_beka15['3']}", parse_mode='html')

@dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer16)
async def question16(message: Message, state: FSMContext):
    await message.answer(f"Вопрос 16/21:\n{depression_beka16['0']}\n\n{depression_beka16['1']}\n\n{depression_beka16['2']}\n\n{depression_beka16['3']}", parse_mode='html')

@dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer17)
async def question17(message: Message, state: FSMContext):
    await message.answer(f"Вопрос 17/21:\n{depression_beka17['0']}\n\n{depression_beka17['1']}\n\n{depression_beka17['2']}\n\n{depression_beka17['3']}", parse_mode='html')

@dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer18)
async def question18(message: Message, state: FSMContext):
    await message.answer(f"Вопрос 18/21:\n{depression_beka18['0']}\n\n{depression_beka18['1']}\n\n{depression_beka18['2']}\n\n{depression_beka18['3']}", parse_mode='html')

@dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer19)
async def question19(message: Message, state: FSMContext):
    await message.answer(f"Вопрос 19/21:\n{depression_beka19['0']}\n\n{depression_beka19['1']}\n\n{depression_beka19['2']}\n\n{depression_beka19['3']}", parse_mode='html')

@dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer20)
async def question20(message: Message, state: FSMContext):
    await message.answer(f"Вопрос 20/21:\n{depression_beka20['0']}\n\n{depression_beka20['1']}\n\n{depression_beka20['2']}\n\n{depression_beka20['3']}", parse_mode='html')

@dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer21)
async def question21(message: Message, state: FSMContext):
    await message.answer(f"Вопрос 21/21:\n{depression_beka21['0']}\n\n{depression_beka21['1']}\n\n{depression_beka21['2']}\n\n{depression_beka21['3']}", parse_mode='html')




async def tests(message):
   await bot.send_message(message.chat.id, 'Вот cписок доступных тестов:\nНичего нет')
   await test_depression_beka(message)

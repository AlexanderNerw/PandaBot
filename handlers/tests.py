from aiogram.dispatcher.filters.state import State, StatesGroup
from handlers.config import dp, bot, Dispatcher, ADMIN
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from handlers.querry_db import db
from handlers.keyboards import *
from handlers.dialogs import *



try: # TEST DEPRESSION BEKA

  class AnswerTDB(StatesGroup):
    answerLang = State()
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
    answerEnd = State()

  # ОТМЕНА
  @dp.message_handler(commands=['cancel'], state=AnswerTDB)
  async def get_cancel_depression_beka(message: Message, state: FSMContext) -> None:
    try:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await tests(message)

    except Exception as ex:
        await bot.send_message(ADMIN[1], f'tests.py [INFO] Неполадки в get_cancel_depression_beka: {ex}')
        print('tests.py [INFO] Неполадки в get_cancel_depression_beka: ' + ex)

  # ТЕСТ ДЕПРЕССИИ БЕКА
  @dp.callback_query_handler(text='test_depression_beka') 
  async def test_depression_beka(call: Message) -> None:
    await bot.edit_message_text("Депрессия зачастую воспринимается как самими людьми, так и окружающими как проявление плохого характера,"
                                "лени и эгоизма, распущенности или природного пессимизма.\n\nСледует помнить, что депрессия - не просто плохое настроение,"
                                "а заболевание, которое требует вмешательства специалистов и достаточно хорошо поддается лечению.",
                                call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=button_test)
    await AnswerTDB.answer1.set()

  # ВОЗВРАТ НАЗАД
  @dp.callback_query_handler(text='back_menu_test', state=AnswerTDB)
  async def question_back(call: CallbackQuery, state: FSMContext):

    await state.finish()
    await bot.send_message(call.message.chat.id, f"Добре", parse_mode='html', reply_markup=ReplyKeyboardRemove())
    await tests(call.message)

  # ВОПРОС 1
  @dp.callback_query_handler(text='yes_test', state=AnswerTDB.answer1)
  async def question1(call: CallbackQuery, state: FSMContext):

      async with state.proxy() as data:
          data['answerLang'] = db.getting(call.message.chat.id, 'language')

      await bot.edit_message_text(depression_beka1[data['answerLang']], call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
      await AnswerTDB.next()

  # ВОПРОС 2
  @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer2)
  async def question2(call: CallbackQuery, state: FSMContext):
      async with state.proxy() as data:
          data['answer1'] = int(call.data)-1

      await bot.edit_message_text(depression_beka2[data['answerLang']], call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
      await AnswerTDB.next()

  # ВОПРОС 3
  @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer3)
  async def question3(call: CallbackQuery, state: FSMContext):
      async with state.proxy() as data:
          data['answer2'] = int(call.data)-1

      await bot.edit_message_text(depression_beka3[data['answerLang']], call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
      await AnswerTDB.next()

  # ВОПРОС 4
  @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer4)
  async def question4(call: CallbackQuery, state: FSMContext):
      async with state.proxy() as data:
          data['answer3'] = int(call.data)-1

      await bot.edit_message_text(depression_beka4[data['answerLang']], call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
      await AnswerTDB.next()

  # ВОПРОС 5
  @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer5)
  async def question5(call: CallbackQuery, state: FSMContext):
      async with state.proxy() as data:
          data['answer4'] = int(call.data)-1

      await bot.edit_message_text(depression_beka5[data['answerLang']], call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
      await AnswerTDB.next()

  # ВОПРОС 6
  @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer6)
  async def question6(call: CallbackQuery, state: FSMContext):
      async with state.proxy() as data:
          data['answer5'] = int(call.data)-1

      await bot.edit_message_text(depression_beka6[data['answerLang']], call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
      await AnswerTDB.next()

  # ВОПРОС 7
  @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer7)
  async def question7(call: CallbackQuery, state: FSMContext):
      async with state.proxy() as data:
          data['answer6'] = int(call.data)-1

      await bot.edit_message_text(depression_beka7[data['answerLang']], call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
      await AnswerTDB.next()


  # ВОПРОС 8
  @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer8)
  async def question8(call: CallbackQuery, state: FSMContext):
      async with state.proxy() as data:
          data['answer7'] = int(call.data)-1

      await bot.edit_message_text(depression_beka8[data['answerLang']], call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
      await AnswerTDB.next()

  # ВОПРОС 9
  @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer9)
  async def question9(call: CallbackQuery, state: FSMContext):
      async with state.proxy() as data:
          data['answer8'] = int(call.data)-1
      await bot.edit_message_text(depression_beka9[data['answerLang']], call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
      await AnswerTDB.next()

  # ВОПРОС 10
  @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer10)
  async def question10(call: CallbackQuery, state: FSMContext):
      async with state.proxy() as data:
          data['answer9'] = int(call.data)-1
      await bot.edit_message_text(depression_beka10[data['answerLang']], call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
      await AnswerTDB.next()

  # ВОПРОС 11
  @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer11)
  async def question11(call: CallbackQuery, state: FSMContext):
      async with state.proxy() as data:
          data['answer10'] = int(call.data)-1
      await bot.edit_message_text(depression_beka11[data['answerLang']], call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
      await AnswerTDB.next()

  # ВОПРОС 12
  @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer12)
  async def question12(call: CallbackQuery, state: FSMContext):
      async with state.proxy() as data:
          data['answer11'] = int(call.data)-1
      await bot.edit_message_text(depression_beka12[data['answerLang']], call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
      await AnswerTDB.next()

  # ВОПРОС 13
  @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer13)
  async def question13(call: CallbackQuery, state: FSMContext):
      async with state.proxy() as data:
          data['answer12'] = int(call.data)-1

      await bot.edit_message_text(depression_beka13[data['answerLang']], call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
      await AnswerTDB.next()

  # ВОПРОС 14
  @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer14)
  async def question14(call: CallbackQuery, state: FSMContext):
      async with state.proxy() as data:
          data['answer13'] = int(call.data)-1

      await bot.edit_message_text(depression_beka14[data['answerLang']], call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
      await AnswerTDB.next()

  # ВОПРОС 15
  @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer15)
  async def question15(call: CallbackQuery, state: FSMContext):
      async with state.proxy() as data:
          data['answer14'] = int(call.data)-1
      await bot.edit_message_text(depression_beka15[data['answerLang']], call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
      await AnswerTDB.next()

  # ВОПРОС 16
  @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer16)
  async def question16(call: CallbackQuery, state: FSMContext):
      async with state.proxy() as data:
          data['answer15'] = int(call.data)-1

      await bot.edit_message_text(depression_beka16[data['answerLang']], call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
      await AnswerTDB.next()

  # ВОПРОС 17
  @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer17)
  async def question17(call: CallbackQuery, state: FSMContext):
      async with state.proxy() as data:
          data['answer16'] = int(call.data)-1
      await bot.edit_message_text(depression_beka17[data['answerLang']], call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
      await AnswerTDB.next()

  # ВОПРОС 18
  @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer18)
  async def question18(call: CallbackQuery, state: FSMContext):
      async with state.proxy() as data:
          data['answer17'] = int(call.data)-1
      await bot.edit_message_text(depression_beka18[data['answerLang']], call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
      await AnswerTDB.next()

  # ВОПРОС 19
  @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer19)
  async def question19(call: CallbackQuery, state: FSMContext):
      async with state.proxy() as data:
          data['answer18'] = int(call.data)-1
      await bot.edit_message_text(depression_beka19[data['answerLang']], call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
      await AnswerTDB.next()

  # ВОПРОС 20
  @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer20)
  async def question20(call: CallbackQuery, state: FSMContext):
      async with state.proxy() as data:
          data['answer19'] = int(call.data)-1
      await bot.edit_message_text(depression_beka20[data['answerLang']], call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
      await AnswerTDB.next()

  # ВОПРОС 21
  @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answer21)
  async def question21(call: CallbackQuery, state: FSMContext):
      async with state.proxy() as data:
          data['answer20'] = int(call.data)-1
      await bot.edit_message_text(depression_beka21[data['answerLang']], call.message.chat.id, call.message.message_id, parse_mode='html', reply_markup=one_two_three_four)
      await AnswerTDB.next()


  # ВОПРОС END
  @dp.callback_query_handler(text=['1', '2', '3', '4'], state=AnswerTDB.answerEnd)
  async def questionEndTDB(call: CallbackQuery, state: FSMContext):
      async with state.proxy() as data:
        data['answer21'] = int(call.data)-1
        data['answerEnd'] = 0
        for num in range(1, 22):
            result = f'answer{num}'
            data['answerEnd'] += data[result] 

      await bot.edit_message_text(f"<b>Ваш результат: {data['answerEnd']} из 63 баллов</b>\n\n", call.message.chat.id, call.message.message_id, parse_mode='html')
      await state.finish()

except Exception as ex:
    print(f'tests.py [INFO] Неполадки в Вопросах Теста Депрессии Бека: {ex}')

async def tests(message: Message):
    await bot.edit_message_text('🧾 Вот cписок доступных тестов:\n', message.chat.id, message.message_id, reply_markup=menu_all_test)
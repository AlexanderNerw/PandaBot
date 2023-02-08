from importing import *
import keyboards as kb

@dp.message_handler(commands=['menu'])
async def toMenu(message): #******************* ГЛАВНОЕ МЕНЮ *********************
    global msg
    msg = message
    print(msg)
    try:
        if (db.getting(message.from_user.id, 'language') == "ru"): #            Русский язык
            await message.answer("🔸                <b>Главное меню</b>                🔸\n\nЗдесь ты можешь пользоваться моими функциями.",
            parse_mode='html', reply_markup=kb.board_menu)
                        
        elif (db.getting(message.from_user.id, 'language') == "uk"): #            Украинский язык
            await message.answer("🔸                <b>Головне меню</b>                🔸\n\nТут ти можеш користуватися моїми функціями.",
            parse_mode='html', reply_markup = kb.board_menu)
    except Exception as ex:
        print('Ошибка главного меню: ', ex)
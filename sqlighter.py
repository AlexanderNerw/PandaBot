import sqlite3
from config import dp, bot

class SQLighter:

    #try:
        def __init__(self, database_file):
            """Подключаемся к БД и сохраняем соединение"""
            self.connection = sqlite3.connect(database_file)
            self.cursor = self.connection.cursor()
    #except Exception as ex:
        #print("Ошибка в открытии бд: ", ex)
        
#ПОЛУЧЕНИЕ ДАННЫХ*************************************************************************************************

        def get_name(self, user_id):
            """Получаем имя"""
            with self.connection:
                result = self.cursor.execute('SELECT `name` FROM `subscriptions` WHERE `user_id` = ?', (user_id, )).fetchall()
                return result[0][0]

        def subs_exists(self, user_id):
            """Проверяем есть ли уже юзер в базе"""
            with self.connection:
                result = self.cursor.execute('SELECT * FROM `subscriptions` WHERE `user_id` = ?', (user_id,)).fetchall()
                #print("РЕЗУЛЬТАТ: ", result, len(result), bool(len(result)))
                return bool(len(result))

        def get_mf(self, user_id):
            """Получаем сравнение парень или девушка"""
            with self.connection:
                result = self.cursor.execute('SELECT `gender` FROM `subscriptions` WHERE `user_id` = ?', (user_id, )).fetchall()
                #print(result, result[0][0])
                return result[0][0]
    
        def get_lang(self, user_id):
            """Получаем сравнение русский или украинский"""
            with self.connection:
                result = self.cursor.execute('SELECT `language` FROM `subscriptions` WHERE `user_id` = ?', (user_id, )).fetchall()
                #print(result, result[0][0])
                return result[0][0]

        def get_msg(self, user_id):
            """Получаем сравнение русский или украинский"""
            with self.connection:
                result = self.cursor.execute('SELECT `last_msg` FROM `subscriptions` WHERE `user_id` = ?', (user_id, )).fetchall()
                print(result, result[0], result[0][0])
                return result[0][0]

    #except Exception as ex:
        #print("Ошибка в получении данных от бд: ", ex)

## ДОБАВЛЕНИЕ КУДА-ТО*************************************************************
    #try:
        def add_language(self, user_id, language):
            """Добавляем русский или украинский язык пользователю"""
            with self.connection:
                return self.cursor.execute("UPDATE `subscriptions` SET `language` = ? WHERE `user_id` = ?", (language, user_id))

        def add_mf(self, user_id, gender):
            """Добавляем пол пользователю"""
            with self.connection:
                return self.cursor.execute("UPDATE `subscriptions` SET `gender` = ? WHERE `user_id` = ?", (gender, user_id))

        def add_subs(self, user_id, status = True):
            """Добавляем нового подписчика"""
            with self.connection:
                return self.cursor.execute("INSERT INTO `subscriptions` (`user_id`, `status`) VALUES (?,?)", (user_id, status))

        def add_name(self, user_id, name):
            """Добавляем имя пользователю"""
            with self.connection:
                return self.cursor.execute("UPDATE `subscriptions` SET `name` = ? WHERE `user_id` = ?", (name, user_id))
                
        def update_subs(self, user_id, status):
            """Обновляем статус подписки"""
            return self.cursor.execute("UPDATE `subscriptions` SET `status` = ? WHERE `user_id` = ?", (status, user_id))

        def add_msg(self, user_id, last_msg):
            """Добавляем имя пользователю"""
            with self.connection:
                return self.cursor.execute("UPDATE `subscriptions` SET `last_msg` = ? WHERE `user_id` = ?", (last_msg, user_id))    

    #except Exception as ex:
    #    print("Ошибка в добавлении данных от бд: ", ex)

#################### ЗАКРЫТИЕ ############################
    #try:
        def close(self):
            """Закрываем соединение с БД"""
            self.connecction.close()
    #except Exception as ex:
    #    print("Ошибка в закрытии бд: ", ex)
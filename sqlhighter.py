import pymysql
from config import host, user, password, db_name

class SQHighter:

    try:
        def __init__(self):
            """ Произошёл коннект """
            try:
                self.connection = pymysql.connect(
                host = host,
                user = user,
                password = password,
                database = db_name,
                port = 3306
                )
                self.connection.ping()
                self.cursor = self.connection.cursor()
            except Exception as ex:
                print("[INFO] Problems in Database Connection:", ex)
        
####################### ДОБАВЛЕНИЕ #################################

        def add_subs(self, user_id, status = True):
            """Добавление нового подписчика"""
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(f"INSERT INTO `users` (`user_id`, `status`) VALUES ({user_id},{status})")
                self.connection.commit()
                self.close()
                return

        def adding(self, user_id, info, inform):
            """Добавление какой-то херни"""
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(f'UPDATE `users` SET `{info}` = "{inform}" WHERE `user_id` = {user_id}')
                self.connection.commit()
                self.close()
                return


####################### ПОЛУЧЕНИЕ ###################################

        def getting(self, user_id, info):
            """Получение какой-то херни"""
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(f'SELECT `{info}` FROM `users` WHERE `user_id` = {user_id}')
                result = cursor.fetchall()
                self.close()
                try:
                    return result[0][0]
                except:
                    print(f"Ошибка снова, {user_id} пытался взять {info}")
                    return result


        def subsex(self, user_id):
            """Проверяем есть ли уже юзер в базе"""
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(f'SELECT * FROM `users` WHERE `user_id` = {user_id}')
                result = cursor.fetchall()
                self.close()
                return bool(len(result))

        def get_all(self, info):
            """ Получение всех записей user_id """
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(f'SELECT `{info}` FROM `users`')    
                result = cursor.fetchall()
                self.close()
                return list(result)

###################### ЗАКРЫТИЕ #####################################

    except Exception as ex:
        print("[ОШИБ_ОЧКА] Ошибка с бд:", ex)

    finally:
        def close(self):
            """Закрываем соединение с БД"""
            self.connection.close()


a = SQHighter()
# try:
#     a = a.get_all('user_id')
#     for i in a:
#         print(*i)
# except Exception as ex:
#     print("Ошиб_Очка с тестом", ex)

# print("Конец")
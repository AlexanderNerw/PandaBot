import pymysql
from handlers.support.config import *
#from config import *

class QuerryDB:

    def __init__(self):
        """ Connection to DataBase """

        try:

            self.connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor)

            self.database_table_name = 'testbase'

            # : , self.connection)
            print("querry_db.py [INFO] Database Succes Connection")

            try:

                with self.connection.cursor() as cursor:
                    querry = f"CREATE TABLE IF NOT EXISTS pandabase.{self.database_table_name} \
                                   (id INT NOT NULL AUTO_INCREMENT, \
                                    user_id VARCHAR(12) NOT NULL, \
                                    status TINYINT(1) NOT NULL DEFAULT 0, \
                                    username VARCHAR(30) NULL, \
                                    gender VARCHAR(6) NULL, \
                                    language VARCHAR(3) NULL, \
                                    text_to_send VARCHAR(500) DEFAULT 0, PRIMARY KEY (id))"

                    cursor.execute(querry)

            finally:
                self.connection.commit()
                self.connection.close()

        except Exception as ex:

            print(f"querry_db.py [INFO] Problems in Database Connection: {ex}")

####################### ДОБАВЛЕНИЕ #################################

    def add_subs(self, user_id, status = False):
        """Добавление нового подписчика"""
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(
                    f"INSERT INTO `{self.database_table_name}` (`user_id`, `status`) VALUES ({user_id}, {status});")

        except Exception as ex:
            print(f"querry_db.py [INFO] Error Database (add_subs): {ex}")

        finally:
            self.connection.commit()
            self.connection.close()
            return

    def add_subs_online(self, user_id, status = True):
        """Добавление нового подписчика в поток"""
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(
                    f"UPDATE`{self.database_table_name}` SET `status` = '{status}' WHERE `user_id` = {user_id}")

        except Exception as ex:
            print(f"querry_db.py [INFO] Error Database (add_subs): {ex}")

        finally:
            self.connection.commit()
            self.connection.close()
            return
# ------------------------------------------------

    def adding(self, user_id, info1, info2):
        """Добавление какой-то херни"""

        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(
                    f'UPDATE `{self.database_table_name}` SET `{info1}` = "{info2}" WHERE `user_id` = {user_id}')

        except Exception as ex:
            print(f"querry_db.py [INFO] Error Database (adding): {ex}")

        finally:
            self.connection.commit()
            self.connection.close()
            return

    def addingInEnd(self, user_id, info1, info2):
        """Добавление какой-то херни"""

        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(
                    f'UPDATE `{self.database_table_name}` SET `{info1}` = `{info1}` + "{info2}"  WHERE `user_id` = {user_id}')

        except Exception as ex:
            print(f"querry_db.py [INFO] Error Database (adding): {ex}")

        finally:
            self.connection.commit()
            self.connection.close()
            return    

####################### ПОЛУЧЕНИЕ ###################################

    def getting(self, user_id, info):
        """Получение какой-то херни"""

        try:
            self.connection.ping()

            with self.connection.cursor() as cursor:
                cursor.execute(
                    f'SELECT `{info}` FROM `{self.database_table_name}` WHERE `user_id` = {user_id} LIMIT 1')
            result = cursor.fetchone()

        except Exception as ex:
            print(f"querry_db.py [INFO] Error Database (getting): {ex}")

        finally:
            self.connection.commit()
            self.connection.close()
            return result[info]
# ------------------------------------------------

    def user_in_database(self, user_id):
        """Проверяем есть ли уже юзер в базе"""
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(
                    f'SELECT `status` FROM `{self.database_table_name}` WHERE `user_id` = {user_id}')
                result = cursor.fetchone()
                return bool(result['status'])

        except Exception as ex:
            print(
                f"querry_db.py [INFO] Error Database (user_in_database): {ex}")

        finally:
            self.connection.commit()
            self.connection.close()

###################### АДМИНИСТРИРОВАНИЕ ###########################

    def get_all_id(self):  # <= info
        """ Получение всех записей user_id """
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                # <= `{info}`
                cursor.execute(
                    f'SELECT user_id FROM {self.database_table_name}')
                result = cursor.fetchall()

        except Exception as ex:
            print(f"querry_db.py [INFO] Error Database (get_all): {ex}")

        finally:
            self.connection.commit()
            self.connection.close()
            return result

    def get_all_info(self):  # <= info
        """ Получение всех записей user_id """
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                # <= `{info}`
                cursor.execute(
                    f'SELECT user_id, username, gender, language FROM {self.database_table_name}')
                result = cursor.fetchall()

        except Exception as ex:
            print(f"querry_db.py [INFO] Error Database (get_all_info): {ex}")

        finally:
            self.connection.commit()
            self.connection.close()
            return result

    def get_person(self, user_id):
        """ Получение всех записей user_id """
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(
                    f'SELECT * FROM `{self.database_table_name}` WHERE `user_id` = {user_id}')
                result = cursor.fetchall()

        except Exception as ex:
            print(f"querry_db.py [INFO] Error Database (get_person): {ex}")

        finally:
            self.connection.commit()
            self.connection.close()
            return list(result)

    def delete_person(self, user_id):
        """ Получение всех записей user_id """
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(
                    f'DELETE FROM `{self.database_table_name}` WHERE `user_id` = {user_id}')

        except Exception as ex:
            print(f"querry_db.py [INFO] Error Database (get_all): {ex}")

        finally:
            self.connection.commit()
            self.connection.close()

# ------------------------------------------------

    def get_update(self):
        """ Получение всех записей user_id """
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                # <= `{info}`
                cursor.execute(
                    f'SELECT `user_id` FROM `{self.database_table_name}`')
                result = cursor.fetchall()
                users = []
                for a in result:
                    users.append(a['user_id'])

        except Exception as ex:
            print(f"querry_db.py [INFO] Error Database (get_all): {ex}")

        finally:
            self.connection.commit()
            self.connection.close()
            return users







# Cоединение с БД
db = QuerryDB()

#db.addingInEnd(1082803262, 'text_to_send', 5)

# print(a.get_update())
# print(a.get_update())

# a.delete_person('1082803262')

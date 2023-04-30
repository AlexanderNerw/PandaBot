import pymysql,  os, time
from dotenv import load_dotenv

class QuerryDB:

    def __init__(self):
        """ Connection to DataBase """

        try:
            load_dotenv()
            self.connection = pymysql.connect(
                host=       os.getenv('host'),
                port=       3306,
                user=       os.getenv('user'),
                password=   os.getenv('password'),
                database=   'pandabase',
                cursorclass=pymysql.cursors.DictCursor)

            self.database_table_name = 'testbase'

            print("querry_db.py [INFO] Database Succes Connection")

            with self.connection.cursor() as cursor:

                querry1 = f"CREATE TABLE IF NOT EXISTS pandabase.answer_test \
                                (id INT NOT NULL AUTO_INCREMENT, \
                                user_id VARCHAR(12) NOT NULL, \
                                TDBeka VARCHAR(255) DEFAULT 'TDBeka', \
                                TTBeka VARCHAR(255) DEFAULT 'TTBeka', \
                                TBBeka VARCHAR(255) DEFAULT 'TBBeka', PRIMARY KEY (id));"

                querry = f"CREATE TABLE IF NOT EXISTS pandabase.{self.database_table_name} \
                                (id INT NOT NULL AUTO_INCREMENT, \
                                user_id VARCHAR(12) NOT NULL, \
                                status TINYINT(1) DEFAULT 0, \
                                notice TINYINT(1) DEFAULT 1, \
                                username VARCHAR(30) NULL, \
                                gender VARCHAR(6) DEFAULT 'man', \
                                language VARCHAR(3) DEFAULT 'ru', PRIMARY KEY (id));"

                cursor.execute(querry1)
                cursor.execute(querry)
                try:
                    self.connection.commit()
                    self.connection.close()
                except Exception as ex: print(ex)

        except Exception as ex:
            print(f"querry_db.py [INFO] [{time.asctime()}] Problems in Database Connection: {ex}")

####################### ДОБАВЛЕНИЕ #################################

    def add_subs(self, user_id):
        """Добавление нового подписчика"""
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(f'SELECT * FROM {self.database_table_name} WHERE user_id = {user_id};')
                result = cursor.fetchone()                
                if (True if result == None else False):
                    cursor.execute(f"INSERT INTO pandabase.{self.database_table_name} (user_id) VALUES ({user_id});")
                    cursor.execute(f"INSERT INTO pandabase.answer_test (user_id) VALUES ({user_id});")
                    return True

        except Exception as ex:
            print(f"querry_db.py [INFO] [{time.asctime()}] Error Database (add_subs): {ex}")
            return False

# ------------------------------------------------

    def adding(self, user_id, info1: str, info2: str, database = 'testbase'):
        """Добавление какой-то херни"""
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(
                    f'UPDATE pandabase.{database} SET {info1} = "{info2}" WHERE `user_id` = {user_id};')
                return True

        except Exception as ex:
            print(f"querry_db.py [INFO] [{time.asctime()}] Error Database (adding): {ex}")
            return False

    def addingEndStart(self, user_id, info1: str, info2: str, reserse = False):
        """Добавление какой-то херни"""
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:

                if (not reserse): cursor.execute(f"UPDATE pandabase.answer_test SET {info1} = CONCAT({info1}, '{info2}')  WHERE user_id = {user_id};")
                else: cursor.execute(f"UPDATE pandabase.answer_test SET {info1} = CONCAT('{info2}', {info1})  WHERE user_id = {user_id};")
                return True

        except Exception as ex:
            print(f"querry_db.py [INFO] [{time.asctime()}] Error Database (addingEndStart): {ex}")
            return False

####################### ПОЛУЧЕНИЕ ###################################

    def getting(self, user_id, info, database = 'testbase'):
        """Получение какой-то херни"""
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(f'SELECT {info} FROM {database} WHERE user_id = {user_id} LIMIT 1') # self.database_table_name
            result = cursor.fetchone()
            return result[info]
            
        except Exception as ex: print(f"querry_db.py [INFO] [{time.asctime()}] Error Database (getting): {ex}")

# ------------------------------------------------

    def user_in_database(self, user_id):
        """Проверяем есть ли уже юзер в базе"""
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(f'SELECT * FROM `{self.database_table_name}` WHERE `user_id` = {user_id};')
                result = cursor.fetchone()              
                return False if result == None else True

        except Exception as ex: print(f"querry_db.py [INFO] [{time.asctime()}] Error Database (user_in_database): {ex}")


    def user_online_in_database(self, user_id):
        """Проверяем есть ли уже юзер в базе"""
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute( f'SELECT status FROM `{self.database_table_name}` WHERE `user_id` = {user_id};')
                result = cursor.fetchone()                
                return False if result == None else bool(result['status'])

        except Exception as ex:
            print( f"querry_db.py [INFO] [{time.asctime()}] Error Database (user_online_in_database): {ex}")


    def user_notice(self, user_id):
        """Проверяем есть ли уже юзер в базе"""
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(f'SELECT notice FROM `{self.database_table_name}` WHERE `user_id` = {user_id};')
                result = cursor.fetchone()                
                return False if result == None else bool(result['notice'])

        except Exception as ex:
            print( f"querry_db.py [INFO] [{time.asctime()}] Error Database (user_notice): {ex}")

###################### АДМИНИСТРИРОВАНИЕ ###########################

    def get_all_id(self, language = 'all'):
        """ Получение всех записей user_id """
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                if language in ['uk', 'ru']:    cursor.execute(f"SELECT user_id FROM {self.database_table_name} WHERE (notice = 1) AND (language = '{language}')")
                else:                           cursor.execute(f'SELECT user_id FROM {self.database_table_name} WHERE (notice = 1)')
                result = cursor.fetchall()
                users = set()
                
                for i in result:
                    if str(i['user_id']).startswith('-'): continue
                    users.add(i['user_id'])
                return users

        except Exception as ex: print(f"querry_db.py [INFO] [{time.asctime()}] Error Database (get_all_id): {ex}")


    def get_all_info(self):
        """ Получение всех записей user_id """
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(
                    f'SELECT user_id, username, gender, language FROM {self.database_table_name};')
                result = cursor.fetchall()

        except Exception as ex:print(f"querry_db.py [INFO] [{time.asctime()}] Error Database (get_all_info): {ex}")
        finally: return result

    def get_person(self, user_id, database = 'testbase'):
        """ Получение всех записей user_id """
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(f'SELECT * FROM {database} WHERE user_id = {user_id};')
                result = cursor.fetchall()

        except Exception as ex: print(f"querry_db.py [INFO] [{time.asctime()}] Error Database (get_person): {ex}")
        finally: return list(result)

    def delete_person(self, user_id):
        """ Получение всех записей user_id """
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(
                    f'DELETE FROM {self.database_table_name} WHERE user_id = {user_id};')

        except Exception as ex:
            print(f"querry_db.py [INFO] [{time.asctime()}] Error Database (delete_person): {ex}")

# ------------------------------------------------

# Cоединение с БД
db = QuerryDB()

#print(db.get_all_info())
#db.addingInEnd(1082803262, 'text_to_send', 5)
# a.delete_person('1082803262')

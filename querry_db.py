import pymysql
from config import host, user, password, db_name

class QuerryDB: 

    def __init__(self):
        """ Connection to DataBase """

        try:

            self.connection = pymysql.connect( 
                    host = host,
                    port = 3306, 
                    user = user,
                    password = password,
                    database = db_name,
                    cursorclass = pymysql.cursors.DictCursor)

            print("[INFO] Database Succes Connection" ) # : , self.connection)

            try:

                with self.connection.cursor() as cursor:
                    querry = "CREATE TABLE IF NOT EXISTS pandabase.subscribers \
                                   (id INT NOT NULL AUTO_INCREMENT, \
                                    user_id INT NOT NULL, \
                                    status TINYINT(1) NOT NULL DEFAULT 0, \
                                    username VARCHAR(30) NULL, \
                                    gender VARCHAR(6) NULL, \
                                    language VARCHAR(3) NULL, PRIMARY KEY (id))"    

                    #cursor.execute(querry) 

            finally:
                self.connection.commit()
                self.connection.close()

        except Exception as ex:

            print("[INFO] Problems in Database Connection:", ex)

####################### ДОБАВЛЕНИЕ #################################

    def add_subs(self, user_id, status = True):
            """Добавление нового подписчика"""
            try:
                self.connection.ping()
                with self.connection.cursor() as cursor:
                    cursor.execute(f"INSERT INTO `subscribers` (`user_id`, `status`) VALUES ({user_id},{status})")

            except Exception as ex:
                print("[Info] Error Database (add_subs): ", ex)

            finally:
                self.connection.commit()
                self.connection.close()
                return

#------------------------------------------------       

    def adding(self, user_id, info1, inform2):
            """Добавление какой-то херни"""

            try:
                self.connection.ping()
                with self.connection.cursor() as cursor:
                    cursor.execute(f'UPDATE `subscribers` SET `{info1}` = "{inform2}" WHERE `user_id` = {user_id}')

            except Exception as ex:
                print("[Info] Error Database (adding): ", ex)

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
                    cursor.execute(f'SELECT `{info}` FROM `subscribers` WHERE `user_id` = {user_id}')
                result = cursor.fetchall()

            except Exception as ex:
                print("[Info] Error Database (getting): ", ex)

            finally:
                self.connection.commit()
                self.connection.close()
                return result[0][info]

#------------------------------------------------ 

    def subsex(self, user_id):
        """Проверяем есть ли уже юзер в базе"""
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(f'SELECT * FROM `subscribers` WHERE `user_id` = {user_id}')
                result = cursor.fetchall()
                return bool(len(result))

        except Exception as ex:
            print("[Info] Error Database (subsex): ", ex)

        finally:
            self.connection.commit()
            self.connection.close()

###################### АДМИНИСТРИРОВАНИЕ ########################### 

    def get_all(self):  # <= info
        """ Получение всех записей user_id """
        try:    
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(f'SELECT * FROM `subscribers`')  # <= `{info}`
                result = cursor.fetchall()

        except Exception as ex:
                print("[Info] Error Database (get_all): ", ex)

        finally:
            self.connection.commit()
            self.connection.close()
            return result[0]['language']
  
#------------------------------------------------ 

    def get_person(self, user_id):
        """ Получение всех записей user_id """
        try:    
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(f'SELECT * FROM `subscribers` WHERE `user_id` = {user_id}')
                result = cursor.fetchall()

        except Exception as ex:
                print("[Info] Error Database (get_person): ", ex)

        finally:
            self.connection.commit()
            self.connection.close()
            return list(result)

#------------------------------------------------ 

    def delete_person(self, user_id):
        """ Получение всех записей user_id """
        try:    
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(f'DELETE FROM `subscribers` WHERE `user_id` = {user_id}')

        except Exception as ex:
            print("[Info] Error Database (get_all): ", ex)

        finally:
            self.connection.commit()
            self.connection.close()


#a = QuerryDB()
#print(a.delete_person(1082803262))

#a.delete_person('1082803262')
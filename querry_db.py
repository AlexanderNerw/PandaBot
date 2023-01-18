from mysql.connector import connect, Error
from config import host, user, password, db_name

class SQHighter: 

    def __init__(self):
        """ Произошёл коннект """
        try:

            with connect(  host = host,
                           user = user,
                           password = password,
                           #database = db_name,
                           #port = 3306          
                           
                        ) as self.connection:

                with self.connection.cursor() as self.cursor:

                    self.cursor.execute("CREATE DATABASE panda_info")
                    self.connection.ping()
                    print("[INFO] Database Succes Connection: ", self.connection)

        except Exception as ex:
            print("[INFO] Problems in Database Connection:", ex)


a = SQHighter()
import pymysql
from config import host, user, password, db_name

class SQHighter: 

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
                    querry = "CREATE TABLE `pandabase` (id int AUTO_INCREMENT, \
                                                        user_id int, status tinyint,\
                                                        username varchar(40), \
                                                        password varchar(40), \
                                                        gender varchar(5), language varchar(3), PRIMARY KEY(id));"                                   
                    #cursor.execute(que) 

            finally:
                self.connection.ping()
                self.connection.close()

        except Exception as ex:

            print("[INFO] Problems in Database Connection:", ex)

    def add_subs(self, user_id, status = True):
            """Добавление нового подписчика"""

            try:
                self.connection.ping()
                with self.connection.cursor() as cursor:
                    cursor.execute(f"INSERT INTO `pandabase` (`user_id`, `status`) VALUES ({user_id},{status})")

            finally:
                self.connection.commit()
                self.connection.close()
                return

a = SQHighter()
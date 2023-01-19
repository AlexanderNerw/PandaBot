import pymysql
from config import host, user, password, db_name

class SQHighter: 

    #def __init__(self):
        """ Connection to DataBase """

        try:

            connection = pymysql.connect( 
                    host = host,
                    port = 3306, 
                    user = user,
                    password = password,
                    database = db_name,
                    cursorclass = pymysql.cursors.DictCursor)
                
            print("[INFO] Database Succes Connection: ", connection)

            try:

                with connection.cursor() as cursor:
                    exsd = "CREATE TABLE `pandabase` (id int AUTU_INCREMENT, \
                                                      user_id int \
                                                      status tinyint \
                                                      username varchar(40) \
                                                      password varchar(40) \
                                                      gender varchar(5) PRIMARY KEY(id));" 
                    cursor.execute(exsd)
                    

            finally:
                connection.close()

        except Exception as ex:
            print("[INFO] Problems in Database Connection:", ex)


a = SQHighter()
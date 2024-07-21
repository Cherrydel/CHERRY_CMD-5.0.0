import pymysql
from Cors.Conf.Cherryofl.Modulsys.dbdel.Nemdatabase.config import host, user, password, db_name
import time

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    
    print("Соединение устоновлено успешно...")
    time.sleep (0.1)
    print("#" * 100)

    try:
        cursor = connection.cursor()
        tblice = input( " Введите название таблици " )

        # Создание таблици
        with connection.cursor() as cursor:
            create_table_query = "CREATE TABLE `" + tblice + "` (id int AUTO_INCREMENT," \
                                 " idlog varchar(32)," \
                                 " codeufx varchar(32), PRIMARY KEY (id));"
            cursor.execute(create_table_query)
            print(" Таблица успешно создана... ")
            print("#" * 50)
            input ( " Продолжить ? " )

    finally:
        connection.close()

except Exception as ex:
    print("Ошибка подключения к базе данных, проверте ваши данные...")
    print(ex)

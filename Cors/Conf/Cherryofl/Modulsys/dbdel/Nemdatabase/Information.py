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
        tblice = input( " Введите название таблици из которой необходимо взять файлы " )

        # Вывод информации
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `" + tblice + "`"
            cursor.execute(select_all_rows)
            # cursor.execute("SELECT * FROM `" + tblice + "`")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("#" * 50)

    finally:
        connection.close()

except Exception as ex:
    print("Ошибка подключения к базе данных, проверте ваши данные...")
    print(ex)

import pymysql
from colorama import Fore
import time

from tqdm import tqdm
import os
from requests import *
from pyfiglet import *
from threading import *
import sys
import sounddevice as sd

try:
    from Cors.Conf.Cherryofl.Modulsys.dbdel.Nemdatabase.config import host, user, password, db_name

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
            tblice = input( " Введите название таблици в которой необходимо удалить пользователя " )
            deluser = input( " Введите НОМЕР ID пользователя которого нудно удалить " )

            # Удоление пользователя
            with connection.cursor() as cursor:
                delete_query = "DELETE FROM `" + tblice + "` WHERE id = " + deluser + ";"
                cursor.execute(delete_query)
                connection.commit()
                print (" Пользователь удолён успешно ")
                print("#" * 50)
                input ( " Продолжить ? " )

        finally:
            connection.close()

    except Exception as ex:
        print("Ошибка подключения к базе данных, проверте ваши данные...")
        print(ex)
except:
    print (Fore.RED + "ERROR_DEL \n Cors/Conf/Cherryofl/Modulsys/dbdel/Nemdatabase/config \n Не найден файл config.py. \n Обратитесь к Администратору. " )
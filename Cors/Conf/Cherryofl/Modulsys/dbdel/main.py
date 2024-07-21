try:
    import os
    import mysql.connector as mysqlconnector
    from colorama import Fore, Back, Style
    from tqdm import tqdm
    from requests import *
    from pyfiglet import *
    from threading import *
    import sys

    while True:
        print (Style.BRIGHT)
        osdelsystemog = input ( Fore.RED + "\n [ HELP -MYSQL ] \n />  :" + Fore.GREEN + "  " )
        
        if osdelsystemog == 'NEM_TBL':
            # Создание таблицы
            from Cors.Conf.Cherryofl.Modulsys.dbdel.Nemdatabase.Tablsys import *
            
        elif osdelsystemog == 'NEM_USER':
            # Создание пользователя
            from Cors.Conf.Cherryofl.Modulsys.dbdel.Nemdatabase.Usersys import *
            
        elif osdelsystemog == 'UPDATE_USER_PSS':
            # Обновление информации пользователя
            from Cors.Conf.Cherryofl.Modulsys.dbdel.Nemdatabase.Restartuserpasswd import *
            
        elif osdelsystemog == 'INFO_DATABASE':
            # Вывод данных
            from Cors.Conf.Cherryofl.Modulsys.dbdel.Nemdatabase.Information import *
            
        elif osdelsystemog == 'DELIT_USER_ID':
            # Удоление пользователя
            from Cors.Conf.Cherryofl.Modulsys.dbdel.Nemdatabase.delituser import *
            
        elif osdelsystemog == 'DELIT_TABL':
            # Удоление таблицы
            from Cors.Conf.Cherryofl.Modulsys.dbdel.Nemdatabase.delittablsys import *

        elif osdelsystemog == 'clear':
            # clear
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            
        elif osdelsystemog == 'CONNECTING':
            # Подключение к базе данных
            try:
                from Cors.Conf.Cherryofl.Modulsys.dbdel.Nemdatabase.connecting import *
            except:
                print(Fore.RED + " Вам необходимо загрузить файл 'config.py'." + Fore.YELLOW + "\n Обратитесь в поддержку SYS_DEL" + Fore.CYAN + " [ https://t.me/logdeliex_bot ] > (Support.DEL 24/7) " )
            
        # Информация и выход   =======================================================================================================================================
        elif osdelsystemog == 'HELP -MYSQL':
            
            print ( Fore.GREEN +    "|\n|          [ Команда ]                  ( Цель команды ) " )
            print ( Fore.YELLOW +   "|          [ CONNECTING ]               ( Подключение к базе данных ) \n|" )
            print ( Fore.CYAN +    "|          [ NEM_TBL ]                  ( Создание таблицы ) " )
            print ( Fore.CYAN +    "|          [ NEM_USER ]                 ( Создание пользователя ) " )
            print ( Fore.CYAN +    "|          [ UPDATE_USER_PSS ]          ( Обновление информации пользователя ) " )
            print ( Fore.CYAN +    "|          [ INFO_DATABASE ]            ( Вывод данных ) " )
            print ( Fore.CYAN +    "|          [ DELIT_USER_ID ]            ( Удоление пользователя ) " )
            print ( Fore.CYAN +    "|          [ DELIT_TABL ]               ( Удоление таблицы ) " )
            print ( Fore.YELLOW +   "|          [ EXIT ]                     ( НАЗАД ) \n|" )
            
        elif osdelsystemog == 'EXIT':
            print ( Fore.RED + " Вход в систему SYS-CMD " )
            time.sleep (1.0)
            break
        
        else:
            print ( Fore.RED + " Нет такого условия [ ERROR-SYS ] " )
except:
    input ( " [!] NO IMPORT DB " )

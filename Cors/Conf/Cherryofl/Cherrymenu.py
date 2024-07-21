#====================================================================================================================================================================================
# Работа клиента 
# CHERRY ( 5.0.0 )
from colorama import Fore, Back, Style
from tqdm import tqdm
import os
from requests import *
from pyfiglet import *
from threading import *
import sys
import sounddevice as sd
from Cors.Setingdel.GRF_DEL import *
from Cors.Setingdel.Coming import *
from Cors.system import *
os.system('cls' if os.name == 'nt' else 'clear')
# Приветствие
time.sleep (2.6)
try:
    while True:
        from Cors.log.USER import *
        print (Style.BRIGHT)
        cherrycom = input(GRFMECH)
        # SETINGS
        if cherrycom == LKC1 : # Администраторы
            time.sleep (0.1)
            print (Fore.GREEN + " [!] Проверка файловой системы CMD " )
            time.sleep (0.1)
            print (Fore.GREEN + " [#] Попытка импорта модульной системы " )
            time.sleep (0.1)
            print (Fore.GREEN + " [LOG] Проверка LOG_DEL " )
            time.sleep(5.0)
            from Cors.log.USER import *

        elif cherrycom == CL1:
            import os
            os.system('cls' if os.name == 'nt' else 'clear')

        elif cherrycom == EX2:
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        elif cherrycom == "COM":
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            setcom()

        # MODUL STARTING
        elif cherrycom == GM1:
            print ( Fore.RED + " [+] Выполнение... \n" )
            time.sleep (0.7)
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            gamesdel()

        elif cherrycom == SER1:
            print ( Fore.RED + " [+] Выполнение... \n" )
            time.sleep (0.7)
            print("IN")
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            serverdel()

        elif cherrycom == MSD1:
            print ( Fore.RED + " [+] Выполнение... \n" )
            time.sleep (0.7)
            print("IS")
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            dbdel()

        elif cherrycom == HEL:
            print ( " [/SLOT] > Запуск сторонего модуля. " )

        elif cherrycom == SLO:
            print ( Fore.RED + " [+] Выполнение... SLOT \n" )
            time.sleep (0.7)
            print("SSS")
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                print (" system.py ")
                slot()
            except:
                print (" Модуль не найден...")

        elif cherrycom == "LS -M":
            print ( Fore.YELLOW + " [+] Выполнение..." )
            time.sleep (0.1)
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            print(" [!] AI")
            print (Fore.WHITE + FLM)
            import os
            folder="Cors/Conf/Cherryofl/Modulsys"
            for file in os.listdir(folder):
                print(os.path.join("   [>] "+file))
            flm1()
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            
        else:
            print (Fore.RED + " [?] Модуль не встроен в систему. " + Fore.YELLOW)
except:
    print (Fore.RED + " [X] Ошибка выполнения программного обеспечения. [ CHERRY_OFFL ] " )
    
# Конечная работа КЛИЕНТА
#====================================================================================================================================================================================

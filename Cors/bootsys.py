# BOOT_MENU CHERRY_DEL

from colorama import Fore, Back, Style
from tqdm import tqdm
import os
from requests import *
from pyfiglet import *
from threading import *
import sys
import sounddevice as sd
from Cors.Setingdel.Coming import *
from Cors.Setingdel.Coming import *
from Cors.Setingdel.GRF_DEL import *
from Cors.Setingdel.GRF_DEL import *
print (Style.BRIGHT)
from Cors.Setingdel.Coming import *

# BOOT SYS
time.sleep(2.0)
print (Fore.WHITE + " [!] Starting bootsys... " )
time.sleep(1.0)

try:
    while True:
        insysbot = input(GRFBOOT)

        if insysbot == ST2:
            print (Fore.GREEN + " [+] Подключено, необходимо проверить наличие прав пользователя! [ START_LOG ] ")
            import time
            from colorama import Fore
            import os
            print(Fore.YELLOW + " [#] ОЖИДАНИЕ [ ? CHERRY_CMD ] ")
            time.sleep(1.0)
            print(Fore.GREEN + " [?] Проверка LOG SYS [ ? Выполнение ] ")
            print(Fore.CYAN)

            while True:
                from Cors.log.logsys import *
                time.sleep (2.6)
                try:
                    # CHERRY SYS 5.0.0
                    while True:
                        cherrycom = input (GRFCHME)
                            
                        if cherrycom == CL1:
                            import os
                            os.system('cls' if os.name == 'nt' else 'clear')

                        elif cherrycom == EX2:
                            print ( Fore.RED + "|--> BOOT \n" )
                            print (" [!] Выключение системы через 0.05 ")
                            for i in tqdm (range (100),
                                    desc=  "Выключение [>] ",
                                    ascii=False, ncols=75):
                                time.sleep(0.05)
                            os.abort()

                        elif cherrycom == LIC:
                            import os
                            os.system('cls' if os.name == 'nt' else 'clear')
                            licenziondelpin()
                                
                        elif cherrycom == MEN:
                            prcmenu()
                        elif cherrycom == HEL:
                            prchelp()
                        elif cherrycom == INF:
                            prcinfo()
                            
                        elif cherrycom == CHD:
                            print("IN")
                            import os
                            os.system('cls' if os.name == 'nt' else 'clear')
                            from Cors.Conf.Cherryofl.Cherrymenu import *
                                
                        elif cherrycom == SRD:
                            print("IN")
                            import os
                            os.system('cls' if os.name == 'nt' else 'clear')
                            from Cors.Conf.Cherryonlin.Cherryonsys import *

                        elif cherrycom == "COM":
                            import os
                            os.system('cls' if os.name == 'nt' else 'clear')
                            setcom()
                                
                        elif cherrycom == "":
                            print (Fore.RED + " [X] ERROR-SYS [ " + MEN + " ] " )
                                
                        else:
                            print (Fore.RED + " [X] Введено не верное значение." + Fore.YELLOW + " [ "+ cherrycom + " ]" + Fore.CYAN + " > [ " + HEL + " ] ")
                except:
                    print (Fore.RED + " [X] Ошибка выполнения программного обеспечения. " )

        # BOOT SYS
        elif insysbot == EX2:
            print ( Fore.RED + "|--> BOOT \n" )
            print (" [!] Выключение системы через 0.05 ")
            for i in tqdm (range (100),
                    desc=  "Выключение [>] ",
                    ascii=False, ncols=75):
                time.sleep(0.05)
            os.abort()

        elif insysbot == "COM":
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            setcom()

        elif insysbot == CL1:
            import os
            os.system('cls' if os.name == 'nt' else 'clear')

        else:
            print (Fore.RED + " [X] Введено не верное значение. [ " + ST2 + " ] ")
except:
    print ( Fore.RED + " [X] Не найдены файлы LOG_DEL [ ADMIN_DEL_LOG_FIELS ] " )
    time.sleep(0.1)
    input ( " [!] Для повтора введите [ ENTER ] " )

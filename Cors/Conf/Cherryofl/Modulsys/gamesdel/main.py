# GAMES_DEL CHERRY_DEL
try:
    from colorama import Fore
    import time
    from tqdm import tqdm
    import os
    from requests import *
    from pyfiglet import *
    from threading import *
    import sys
    from Cors.Setingdel.GRF_DEL import *
    from Cors.Setingdel.Coming import *

    print ( " [+] Starting Gamesys... " )
    time.sleep(1.0)
    from Cors.log.GAMES_SYS import *

    try:
        print  (Style.BRIGHT)
        time.sleep (2.6)
        try:
            while True:
                print (Style.BRIGHT)
                cherrycom = input (GRGAMEMENU)

                if cherrycom == CL1:
                    import os
                    os.system('cls' if os.name == 'nt' else 'clear')

                elif cherrycom == EX2:
                    print ( Fore.YELLOW + " [!] Ожидайте -> BOOT/ ")
                    import os
                    os.system('cls' if os.name == 'nt' else 'clear')
                    time.sleep(1.0)
                    break
                elif cherrycom == MEN:
                    gmmenu()
                elif cherrycom == INF:
                    gminfo()

                elif cherrycom == GDM:
                    print("IN")
                    import os
                    os.system('cls' if os.name == 'nt' else 'clear')
                    from Cors.Conf.Cherryofl.Modulsys.gamesdel.gamescmd.menu import *

                elif cherrycom == "COM":
                    import os
                    os.system('cls' if os.name == 'nt' else 'clear')
                    setcom()

                elif cherrycom == GRFG:
                    print("IN")
                    import os
                    os.system('cls' if os.name == 'nt' else 'clear')
                    # from Conf.sysserver.serversys import *

                elif cherrycom == "":
                    print (Fore.RED + " [X] ERROR-SYS [ " + MEN + " ] [ GAMES_CMD ] " )

                else:
                    print (Fore.RED + " [X] Введено не верное значение." + Fore.YELLOW + " [ "+ cherrycom + " ]" + Fore.CYAN + " > [ " + MEN + " ] ")
        except:
            print (Fore.RED + " [X] Ошибка выполнения программного обеспечения. [ GAMES_CMD ] " )
    except:
        print ( Fore.RED + " [X] Не найдены файлы LOG_DEL [ ADMIN_DEL_LOG_FIELS ] [ GAMES_CMD ] " )
        time.sleep(0.1)
        input ( " [!] Для повтора введите [ ENTER ] [ GAMES_CMD ] " )
except:
    input ( " [!] NO IMPORT GAMES " )
# MENU SERVER CHERRY_DEL
try:
    import os
    from tqdm import tqdm
    from colorama import Fore, Back, Style
    import time
    from threading import *
    from requests import *
    from pyfiglet import *
    from Cors.Setingdel.GRF_DEL import *
    from Cors.Setingdel.Coming import *
    print ( " [+] Starting Serversys... " )
    time.sleep(1.0)
    from Cors.log.IPLOG import *
    
    try:
        print  (Style.BRIGHT)
        time.sleep (2.6)
        try:
            while True:
                print (Style.BRIGHT)
                cherrycom = input (GRSERMENU)

                if cherrycom == CL1:
                    import os
                    os.system('cls' if os.name == 'nt' else 'clear')

                elif cherrycom == EX2:
                    print ( Fore.YELLOW + " [#] Ожидайте -> BOOT/ ")
                    import os
                    os.system('cls' if os.name == 'nt' else 'clear')
                    time.sleep(1.0)
                    break
                elif cherrycom == MEN:
                    sermenu()
                elif cherrycom == INF:
                    serinfo()

                elif cherrycom == "COM":
                    import os
                    os.system('cls' if os.name == 'nt' else 'clear')
                    setcom()
                    
                elif cherrycom == SE5:
                    print("IN")
                    import os
                    os.system('cls' if os.name == 'nt' else 'clear')
                    erword()

                    while True:
                        sys = input (PRAVASER)
                        if sys == YE1:
                            print("IN")
                            import os
                            os.system('cls' if os.name == 'nt' else 'clear')
                            from Cors.Conf.Cherryofl.Modulsys.serverdel.Newserver.server import *
                        elif sys == NO1:
                            print ( " [X] NO SYSTING DEL " )
                            break
                        elif sys == CL1:
                            import os
                            os.system('cls' if os.name == 'nt' else 'clear')
                        else:
                            print ( " [X] NO COMMAND " )

                elif cherrycom == SV5:
                    print("IN")
                    import os
                    os.system('cls' if os.name == 'nt' else 'clear')
                    from Cors.Conf.Cherryofl.Modulsys.serverdel.Virtualserver.SERVER_VIR.SYS_SERVER.virsystem import *

                elif cherrycom == "":
                    print (Fore.RED + " [X] ERROR-SYS [ " + MEN + " ] [ SERVER_DEL ] " )

                else:
                    print (Fore.RED + " [X] Введено не верное значение." + Fore.YELLOW + " [ "+ cherrycom + " ]" + Fore.GREEN + " > [ " + MEN + " ] ")
        except:
            print (Fore.RED + " [X] Ошибка выполнения программного обеспечения. [ SERVER_DEL ] " )
    except:
        print ( Fore.RED + " [X] Не найдены файлы LOG_DEL [ ADMIN_DEL_LOG_FIELS ] [ SERVER_DEL ] " )
        time.sleep(0.1)
        input ( " [!] Для повтора введите [ ENTER ] [ SERVER_DEL ] " )
except:
    input ( " [X] NO IMPORT SERVER " )

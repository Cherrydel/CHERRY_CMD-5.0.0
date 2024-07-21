import time
time.sleep(1.0)
import os
os.system('cls' if os.name == 'nt' else 'clear')

def scrolsys():
    try:
        from Cors.Setingdel.GRF_DEL import licenziondelpin
        licenziondelpin()
        from Cors.bootsys import time
    except:
        print ( " NO SYS-GRF CMD " )

def redactors():
    try:
        from Cors.Setingdel.Rencom import time
    except:
        print ( " NO TK MODUL / ON SYS FILE " )

try:
    import time
    print ("\n Проверка системы PIP... ")
    import time
    time.sleep(3.05)
    from colorama import Fore, Back, Style
    from tqdm import tqdm
    import os
    from threading import *
    from requests import *
    from pyfiglet import *
    from Cors.Setingdel.Coming import *
    from Cors.Setingdel.Coming import *
    from Cors.Setingdel.GRF_DEL import *
    import sys
    import sounddevice as sd
    # import openai.error
    print (Fore.GREEN + " SCRLIC CMD 5.0.0. INTROUND 1244321 Instans log.")
    print (Fore.GREEN + " Успешно... \n")

    while True:
        bootstart = input ( Fore.RED + " SYS/ [ " + ST1 + " [COM] ] ")
        if bootstart == ST1:
            print (" Проверка файлов SYS-CMD. ")
            for i in tqdm (range (100),
                    desc=  " Проверка [>] ",
                    ascii=False, ncols=75):
                time.sleep(0.05)
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                from Cors.Setingdel.GRF_DEL import licenziondelpin
                licenziondelpin()
                from Cors.bootsys import *
            except:
                print ( " NO SYS-GRF CMD " )

        elif bootstart == CL1:
            import os
            os.system('cls' if os.name == 'nt' else 'clear')

        elif bootstart == "COM":
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            setcom()

        elif bootstart == "COM -R":
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            redactors()

        else:
            print (" [ NO COMAND ] \n")

except:
    from Cors.Setingdel.install import *
    print (Fore.RED + "\n ( ERROR ) ->  Не хватает файлов PIP. Или не верно указана дериктория. \n")
    input ( "\n \n [ ENTER ] -> EXIT " )

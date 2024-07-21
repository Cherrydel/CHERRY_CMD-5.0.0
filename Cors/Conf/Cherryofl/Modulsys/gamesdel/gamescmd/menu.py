# GAMES_DEL CHERRY_DEL

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

import os
os.system('cls' if os.name == 'nt' else 'clear')

try:
    while True:
        gamesinputing = input (GAMEMENUSYS)
        if gamesinputing == CL1:
            import os
            os.system('cls' if os.name == 'nt' else 'clear')

        elif gamesinputing == EX2:
            print ( Fore.YELLOW + " [#] Ожидайте -> CMD/SYS/ & BOOT/SYS & EXIT")
            break
        elif gamesinputing == HEL:
            time.sleep(1.0)
            gmsyshelp()
        elif gamesinputing == GAM:
            time.sleep(1.0)
            gmsysgames()

        elif gamesinputing == "COM":
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            setcom()

        elif gamesinputing == "":
            print (Fore.RED + " [X] ERROR-SYS [ " + MEN + " ] [ GAMES_CMD-M ] " )

        else:
            print (Fore.RED + " [X] Введено не верное значение." + Fore.MAGENTA + " [ "+ gamesinputing + " ]" + Fore.WHITE + " > [ " + HEL + " ] ")

except:
    print (Fore.RED + " [X] NO ERROR [ GAMES_CMD -M ] " )

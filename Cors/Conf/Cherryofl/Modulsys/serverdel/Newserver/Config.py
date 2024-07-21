from tqdm import tqdm
from colorama import Fore, Back, Style
from Cors.Setingdel.GRF_DEL import *
confwelc()
print ( Fore.CYAN +  "\n [?] Имя вашего проекта. " )
names = input ( Fore.GREEN + " [!] Введите значение : >>> " + Fore.YELLOW )
print ( Fore.CYAN + "\n [?] Проверка LOG и Включение защиты. " )
log = input ( Fore.GREEN + " [!] Введите значение : >>> " + Fore.YELLOW )
print ( Fore.CYAN + "\n [?] Выключение сервера со стороны пользователя " )
off = input ( Fore.GREEN + " [!] Введите значение : >>> " + Fore.YELLOW )
print ( Fore.CYAN + "\n [?] Замарозка сервера со стороны пользователя " )
zmr = input ( Fore.GREEN + " [!] Введите значение : >>> " + Fore.YELLOW )

import os
os.system('cls' if os.name == 'nt' else 'clear')

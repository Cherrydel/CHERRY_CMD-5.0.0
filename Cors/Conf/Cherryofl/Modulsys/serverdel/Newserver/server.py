# SERVER_DEL 3.5.0
from colorama import Fore
import time
from tqdm import tqdm
import os
from requests import *
from pyfiglet import *
from threading import *
import sys
import sounddevice as sd
from Cors.Conf.Cherryofl.Modulsys.serverdel.Newserver.Config import *
import socket, threading
from colorama import Fore, Back, Style
print (Fore.RED)
from Cors.Setingdel.GRF_DEL import *
print (Fore.YELLOW +  " >>> Введите локальный IP-адесс. \n >>> К этому адресу будут подключатся пользователи" )

while True:
    SERVERSYS = input (SERIPSYS)
    LOCALHOST = SERVERSYS
    PORT = 1488
    
    try:
        if SERVERSYS == SERVERSYS:
            print (Fore.YELLOW +  "|  [!] Анализация DEL... ")
            time.sleep(2.0)
            input (Fore.YELLOW +  "|  [!] Нажмите на (ENTER) для пременения настроек... " )
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            server.bind((LOCALHOST, PORT))
            print(Fore.GREEN +    "|  [+] Сервер запущен успешно! ")
            
        else:
            print (Fore.RED + "|  [X]   Не выполнимо! ")
            input ()
            
        class ClientThread(threading.Thread):
            def __init__(self,clientAddress,clientsocket):
                threading.Thread.__init__(self)
                self.csocket = clientsocket
                print (Fore.MAGENTA + "|  [+] Новое подключение: ", clientAddress)
                
            def run(self):
                print (Fore.MAGENTA + "|  [+] Подключение клиента " + Fore.GREEN + " [+] ВЫПОЛНЕНО")
                msg = ''
                try:
                    while True:
                        data = self.csocket.recv(4096)
                        msg = data.decode()
                        print(msg)
                        
                        if msg == log:
                            try:
                                from Cors.log.IPSERVER import time
                                self.csocket.send(bytes( Fore.YELLOW + "\n\n\n", 'UTF-8'))
                                self.csocket.send(bytes( Fore.YELLOW + " [/] Система зашифрована. Вы в безопасности ! \n", 'UTF-8'))
                                print ( " [!] Кто то решил проверить безопасность вашего сервера. " )
                                print ( " [!] Все файлы в идеальном состоянии. " )
                            except:
                                self.csocket.send(bytes( Fore.YELLOW + "\n\n\n", 'UTF-8'))
                                self.csocket.send(bytes( Fore.YELLOW + " Система не защищена \n Отключитесь от сервера как можно скорее. ! \n", 'UTF-8'))
                                print ( " [!] Кто то решил проверить безопасность вашего сервера. " )
                                print ( " [LOG] Загрузите файлы LOG. " )
                                print ( " [X] Ваше соеденение предстовляет угрозу клиенским системам. " )
                                print ( " [Z] Ваш сервер замарожен. Для безопасной проверки системы. " )
                                for i in tqdm (range (100),
                                        desc=  "  Проверка системы.",
                                        ascii=False, ncols=75):
                                    import time
                                    time.sleep(3.0)
                                print ( " [X] Отключение сервера. Файлы не найдены. " )
                                input (Fore.CYAN + " [ ENTER ] " )
                                os.abort()
                            
                        elif msg == '/ SYS':
                            self.csocket.send(bytes( Fore.YELLOW + "\n\n\n", 'UTF-8'))
                            self.csocket.send(bytes( Fore.YELLOW + " [!] OFF_DEL_SYS - Выключение НЕОБРАТИМО \n", 'UTF-8'))
                            self.csocket.send(bytes( Fore.YELLOW + " [!] ZMR_DEL_SYS - Замарозка НЕОБРАТИМО \n", 'UTF-8'))
                            self.csocket.send(bytes( Fore.YELLOW + " [!] Имя проекта - " + names + " \n", 'UTF-8'))
                            self.csocket.send(bytes( Fore.YELLOW + " [!] LOG_SYS_DEL - " + log + " \n", 'UTF-8'))

                        elif msg == "LS/COM":
                            import os
                            os.system('cls' if os.name == 'nt' else 'clear')
                            setcom()
                            
                        elif msg == '/ Start':
                            while True:
                                server.listen(1)
                                clientsock, clientAddress = server.accept()
                                newthread = ClientThread(clientAddress, clientsock)
                                newthread.start()
                                
                        elif msg == off:
                            self.csocket.send(bytes( Fore.YELLOW + "\n\n\n", 'UTF-8'))
                            self.csocket.send(bytes( Fore.YELLOW + " [!] Выключение сервера " + names + " через 1.10 ", 'UTF-8'))
                            print (Fore.YELLOW + " [!] Выключение системы через 1.10 ")
                            for i in tqdm (range (100),
                                    desc=  "  Попытка выключения...",
                                    ascii=False, ncols=75):
                                import time
                                time.sleep(1.10)
                            self.csocket.send(bytes( Fore.YELLOW + " [!] Выполнено выключение Сервера " + names + " [ НЕОБРАТИМО... ] ", 'UTF-8'))
                            print ( " [!] Выполнено выключение Сервера " + names + " " )
                            os.abort()
                            
                        elif msg == zmr:
                            self.csocket.send(bytes( Fore.YELLOW + "\n\n\n", 'UTF-8'))
                            self.csocket.send(bytes( Fore.YELLOW + " [Z!] Переход сервера " + names + " в систему [ замарозки ] через 0.10 ", 'UTF-8'))
                            print (" [Z] Замарозка системы через 0.10 ")
                            for i in tqdm (range (100),
                                    desc=  "  Попытка выключения...",
                                    ascii=False, ncols=75):
                                import time
                                time.sleep(0.10)
                            self.csocket.send(bytes( Fore.YELLOW + " [!] Выполнена замарозка Сервера " + names + " [ НЕОБРАТИМО... ] ", 'UTF-8'))
                            print ( " [!] Выполнена замарозка Сервера SERVER_DEL " )
                            break
                            
                        else:
                            print( Fore.YELLOW + "|")
                except ConnectionResetError:
                        print (Fore.RED + "\n   [X] Принудительное отключение: \n")
                        
        while True:
            print (Fore.YELLOW +  "|  [▓]" )
            server.listen(1)
            clientsock, clientAddress = server.accept()
            newthread = ClientThread(clientAddress, clientsock)
            newthread.start()
    except socket.gaierror:
        print (Fore.RED +  "\n   [X] Не является LOCAL-IP [ " + SERVERSYS + " ]" )
    except TypeError:
        print (Fore.RED +  "\n   [X] Не является LOCAL-IP-SYS [ " + SERVERSYS + " ]" )
    except SyntaxWarning:
            print (Fore.RED +   "\n   [X] ERROR-SYS " )
    except OSError:
            print (Fore.RED +   "\n   [X] SYS ERROR INFO-DEL SERVER SYS-SYS ERROR INFO-DEL CLIENT SYS [ " + SERVERSYS + " ]" )

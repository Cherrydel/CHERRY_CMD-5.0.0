# CHERRY_DEL 5.0.0 SER-3.5.0

from Cors.log.IPLOG import *
import socket
from threading import Thread
from colorama import Fore, Back, Style
import os
from Cors.Setingdel.GRF_DEL import *
from Cors.Setingdel.Coming import *

while True:
    SERVERSYS = input (CHONLINEIN)
    SERVER = SERVERSYS
    PORT = 1488
    
    try:
        if SERVERSYS == SERVERSYS:
            print (Fore.GREEN + "|__>   Попытка подключения... ")
            print ( Fore.YELLOW )
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((SERVER, PORT))
            
        else:
            print (Fore.RED +  "\n \n >>> Не верен IP-SYSTEM CMD " )
            
        client.sendall(bytes(Fore.CYAN + "|  [INFO] -> CHERRY_CMD 5.0.0 CMD <-> IP - [" + SERVERSYS + "]", "UTF-8\n"))
        print (Fore.RED)
        
        def task():
            try:
                while True:
                    in_data =  client.recv(4096)
                    print(in_data.decode())
                    
            except ConnectionResetError:
                offserver()
                import os
                os.system('cls' if os.name == 'nt' else 'clear')
                
        def task2():
            try:
                while True:
                    out_data = input (Fore.CYAN + GRF6 + "| " + Fore.GREEN + " >   "+ SERVERSYS +"                            " + Fore.CYAN + "\n" + Fore.CYAN + "|__>   [/] : " + Fore.WHITE)
                    client.sendall(bytes( Fore.RED + "\n|  [!] -> ( " + Fore.GREEN + SERVERSYS + Fore.RED + " ) -> [▓] > [/] " + Fore.YELLOW,'UTF-8'))
                    client.sendall(bytes(out_data,'UTF-8'))
                    
                    if out_data == CL1:
                        import os
                        os.system('cls' if os.name == 'nt' else 'clear')
                        
                    elif out_data == NOT:
                        import os
                        os.system('cls' if os.name == 'nt' else 'clear')

                    elif out_data == "LS/COM":
                        import os
                        os.system('cls' if os.name == 'nt' else 'clear')
                        setcom()
                        
                    elif out_data == '':
                        print ( Fore.YELLOW + " [0]")
                        
                    else:
                        print ( Fore.RED + " [S] > "  + Fore.YELLOW + "[" + str(out_data) + "]")
            except:
                print (Fore.RED + "[X] Упс что то не так. ERROR-6548 task2\n[X] Возможно сервер к которому вы были подключены,\n[>] оборвал соеденение с вашим IP-адресом\n" )
                
        t1 = Thread(target=task2)
        t2 = Thread(target=task)
        
        t1.start()
        t2.start()
        
        t1.join()
        t2.join()
        
    except socket.gaierror:
        print (Fore.RED +       "[X] Не является IP - Адрессом... [" + SERVERSYS + "]" )
    except SyntaxWarning:
            print (Fore.RED +   "[X]  ERROR-SYS \n" )
    except OSError:
            print (Fore.RED +   "[X] IP - Адресс не найден [" + SERVERSYS + "]" )

from colorama import Fore, init
import socket

init(autoreset=True)

def reverse_shell(param):
    s = socket.socket()
    print(Fore.RED+ "[+] En attende de connection...")
    try:
        s.bind((param['RHOST'],param['RPORT']))
        s.listen()
    except Exception as e:
        return e

    print(Fore.GREEN+ f"[+] Connecter à {param['RHOST']} {param['RPORT']}")
    return s


    
def bind_shell(param):
    s = socket.socket()
    try:
        s.connect(param['RHOST'],param['PORT'])
    except Exception as e:
        return e

    print(Fore.GREEN+ f"[+] Connecter à {param['RHOST']} {param['RPORT']}")
    return s
    

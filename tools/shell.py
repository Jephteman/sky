import socket

def reverse(ip:str,port:int):
    s = socket.socket()
    s.bind((ip,port))
    s.listen()

    
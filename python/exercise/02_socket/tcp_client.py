"""
tcp client progress
"""
from socket import *

sockfd = socket()

server_addr = ('127.0.0.1',8888)
sockfd.connect(server_addr)

msg = input(">>")
sockfd.send(msg.encode())

data = sockfd.recv(1024)

print("From server:",data.decode())

sockfd.close()

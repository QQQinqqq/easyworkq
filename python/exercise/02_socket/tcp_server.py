"""
for tcp server progress
"""

import socket

sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sockfd.bind(('14.18.111.162',8889))

sockfd.listen(3)

print("Waiting for connect ...")
connfd,addr = sockfd.accept()
print("Connect from",addr)

data = connfd.recv(1024)
print("Receive:",data.decode())
n = connfd.send(b'Thanks')

connfd.close()
sockfd.close()


from socket import socket
s = socket()
s.connect(("www.google.com",80))
print(s.recv(1024))

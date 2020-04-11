#
# This program comes in pair with webserver.py
#

from socket import socket

def main():
  t = socket()
  t.connect(('172.20.46.156',8080))
  print("trying to get file 'message.txt' from server...")
  t.send("GET /message.txt".encode())
  content = t.recv(1024)
  print("here is what we've got: \n",content.decode())

main()  

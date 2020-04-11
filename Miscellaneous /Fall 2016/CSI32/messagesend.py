from socket import socket
echo = socket()
echo.connect(('172.20.46.166',9000))
message = 'Hey Yo All, lol'
echo.send(message.encode())

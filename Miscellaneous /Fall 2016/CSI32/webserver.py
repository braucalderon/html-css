# Program: webserver.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 16 of the book
# Object-Oriented Programming in Python
#
from socketserver import TCPServer, BaseRequestHandler

class WebHandler(BaseRequestHandler):
  """ Server
      sends file upon request
      self.request is a socket for the connection,initialized by TCPServer """
  
  def handle(self):
    command = self.request.recv(1024).decode('utf-8')
    if command[:3] == 'GET':
      pagename = command.split()[1][1:]           # remove leading '/' for filename
      print("requested file: ",pagename)
      try:
        requestedFile = open(pagename, 'r')
        content = requestedFile.read()
        requestedFile.close()
        header = 'HTTP/1.0 200 OK\r\n'
        header += 'Content-Length: %d\r\n\r\n' % len(content)
        #self.request.send(header.encode())
        self.request.send(content.encode())
        print("file was found and sent")
      except IOError:                             # could not open the file
        self.request.send('HTTP/1.0 404 Not Found\r\n\r\n'.encode())

webServer = TCPServer( ('localhost', 8080), WebHandler)
print("Web server is ready")
webServer.serve_forever()

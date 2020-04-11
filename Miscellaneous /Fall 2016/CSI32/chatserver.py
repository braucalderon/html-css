# Program: chatserver.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 16 of the book
# Object-Oriented Programming in Python
#
from socketserver import ThreadingTCPServer, BaseRequestHandler

# dictionary of users, id: username, value: socket dedicated to this user
_socketLookup = dict()        # intentionally shared as global

def _broadcast(announcement):
  print("broadcasting...")
  for connection in _socketLookup.values(): # uses the global dictionary
    connection.send(announcement)
  print("finished broadcasting")
  

class ChatHandler(BaseRequestHandler):
  def handle(self):
    username = 'Unknown'
    active = True
    while active:
      transmission = self.request.recv(1024).decode()  # wait for something to happen
      print("\nincoming transmission:",transmission)
      if transmission: # if transmission is not empty
        command = transmission.split()[0]
        data = transmission[1+len(command): ] # the rest

        if command == 'ADD':
          username = data.strip()
          print("Adding the new user:",username)
          _socketLookup[username] = self.request
          toSend = 'NEW %s\n' % username
          _broadcast(toSend.encode())
          
        elif command == 'MESSAGE':
          toSend = 'MESSAGE %s\n%s\n' % (username,data)
          print(username, " sends message: ", data)
          _broadcast(toSend.encode())
          
        elif command == 'PRIVATE':
          rcpt = data.split('\n')[0]
          if rcpt in _socketLookup:
            content = data.split('\n')[1]
            toSend = 'PRIVATE %s\n%s\n'%(username,content)
            print(username, " sends PRIVATE message to ", rcpt)
            _socketLookup[rcpt].send(toSend.encode())
        elif command == 'QUIT':
          
          active = False
          self.request.send('GOODBYE\n'.encode()) # acknowledge
          
      else: # if transmission is empty, the connection failed
          active = False        # socket failed
    
    self.request.close()        # close the controlling socket
    _socketLookup.pop(username) # remove the username from the list of "chatters"
    toSend = 'LEFT %s\n' % username
    _broadcast(toSend.encode())         # inform others

myServer = ThreadingTCPServer( ('localhost', 9000), ChatHandler)
print("Chat server is ready.")
myServer.serve_forever()

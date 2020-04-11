# Program: chatclient.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 16 of the book
# Object-Oriented Programming in Python
#
from socket import socket
from threading import Thread

class IncomingThread(Thread):
  def run(self):
    stillChatting = True
    while stillChatting:                     # wait for more incoming data
      transmission = server.recv(1024).decode() # 'server' will be defined
                                                # globally later in the code
      #print("\n incoming transmission:",transmission)
      
      lines = transmission.split('\n')[:-1]
      i = 0
      while i < len(lines):
        command = lines[i].split()[0]        # first keyword
        param = lines[i][len(command)+1: ]   # remaining information
        if command == 'GOODBYE':
          stillChatting = False
        elif command == 'NEW':
          message = '==>' + param + ' has joined the chat room'
          print(message)
        elif command == 'LEFT':
          message = '==>' + param + ' has left the chat room'
          print(message)
        elif command == 'MESSAGE':
          i += 1    # need next line for content
          message = '==>' + param + ': ' + lines[i]
          print(message)
        elif command == 'PRIVATE':
          i += 1    # need next line for content
          message = '==>' + param + ' [private]: ' + lines[i]
          print(message)
        i += 1

instructions = """
--------------------------------------------
Welcome to the chat room.

To exit from the chat type: quit

To send private message to 'Joe' use syntax:
  private Joe:how are you?

To send message to everyone, use syntax:
  hi everyone!
--------------------------------------------
"""

server = socket()                       # shared by both threads
server.connect( ('localhost', 9000) )   # could be a remote host
username = input('What is your name: ').strip()
toSend = 'ADD %s\n' % username
server.send(toSend.encode() )

# the next two lines will start a secondary thread, that will be monitoring
# the incoming network activity,
# the responsibility of the main thread from now on is to monitor the keyboard
# input
incoming = IncomingThread()
incoming.start()
print("registered the user, started the thread to listen to the server")

print(instructions)
active = True     # main thread for user input
while active:
  
  message = input()     # wait for more user input
  if message.strip():
    if message.rstrip().lower() == 'quit':
      server.send('QUIT\n'.encode())
      active = False
    elif message.split()[0].lower() == 'private':
      colon = message.index(':')
      friend = message[7:colon].strip()
      toSend = 'PRIVATE %s\n%s\n' % (friend,message[1+colon: ]) 
      server.send(toSend.encode())
    else:
      toSend = 'MESSAGE ' + message
      server.send(toSend.encode())

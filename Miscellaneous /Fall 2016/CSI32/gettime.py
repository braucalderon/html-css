# Program: gettime.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 16 of the book
# Object-Oriented Programming in Python
#
# modified by NN
#

from socket import socket

connection = socket()
server = 'time.nist.gov'

# server time.nist.gov supports a very simple protocol (full specification is
# documented by NIST) on port 13
# known as 'daytime'
# whenever a client opens a connection to one of these time servers,
# the server immediately returns a string that contains date and time,
# i.e. no need for client to send a specific request
connection.connect( (server, 13) )
#print("connected")

response = connection.recv(1024) # 1024 is max # of bytes we are ready to receive
print("we got:",response, "\n type of it is",type(response))
# the type of the received message is "byte"

response = response.decode('UTF-8') # casting/converting/decoding to string
print(response, type(response))

#  Comment from stackoverflow 
#  in Python3x string is not the same type as in Python 2.x, 
#  you must cast it to bytes (encode it). 


fields = response.split()
print("we got:",fields)
date = fields[1]
time = fields[2]

print('Date (YY-MM-DD) is %s, time is %s (UTC)' % (date,time))

# Program: webclient.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 16 of the book
# Object-Oriented Programming in Python
#
from socket import socket

print("This program allows you to download a specified by you web-page.")
print('Please enter the web page you want to download,\n \
      using the format http://domain.name/page/to/download:')

url = input() # getting the URL

# processing the URL address aquired from the user
print("\nThe processed information:")
URLlist = url.split('/')
print("URL into list:",URLlist)
server = URLlist[2]                   # splitting into host name and path
print("server name:",server)
page = '/' + '/'.join(url.split('/')[3:])    # building the path to the file
print("page path:", page)

# connecting and retrieving the file
connection = socket()
connection.connect( (server, 80) )
print("connected successfully...")

connection.send(bytes('GET ' + page + ' HTTP/1.0\r\n\r\n', 'UTF-8'))
print("request sent successfully...")

raw = connection.recv(1024).decode('UTF-8')   # read first block (header + some content)
sep = raw.index('\r\n\r\n')
# Each line of the header is terminated with \r\n
# and the entire header will not have any blank lines but will be followed by one,
# therefore \r\n\r\n is a separator between the header and the beginning of the true
# content
print("End of the header: ",sep)
header = raw[ :sep]    # separating the header
content = raw[sep+4: ] # separating the content

length = 0                                   # just in case header doesn't say
for line in header.split('\n'):
  if line[:15] == 'Content-Length:':
    length = int(line[15:])
print("Length of the content is ",length)

outputFile = open('download.html', 'w')
outputFile.write(content)                    # write out content we have seen thus far

contentRead = len(content)
while contentRead < length:                  # still more...
  content = connection.recv(1024).decode('UTF-8')
  contentRead += len(content)
  outputFile.write(content)

outputFile.close()
connection.close()

print("done")

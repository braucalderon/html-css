# Program: easywebclient.py
# Authors: Michael H. Goldwasser
#          David Letscher
#
# This example is discussed in Chapter 16 of the book
# Object-Oriented Programming in Python
#
from urllib.request import urlopen

print("This program allows you to download a specified by you web-page.")
print('Please enter the web page you want to download,\n \
      using the format http://domain.name/page/to/download:')

url = input() # getting the URL

content = urlopen(url).read().decode('utf-8')

outputFile = open('download2.html','w')
outputFile.write(content)
outputFile.close()

print("done")

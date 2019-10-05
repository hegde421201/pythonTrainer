'''
In this program we will retrieve an image over HTTP.

Instead of copying data to the screen as the program runs, we accumulate the
data in a string, trim off the headers and then save the image data to a file.
'''

import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
CHARS_AT_A_TIME = 5120
sock_image = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_image.connect((HOST,PORT))
sock_image.sendall('GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n'.encode())
count = 0
picture = b""

while True:
    data = sock_image.recv(CHARS_AT_A_TIME)
    if len(data) < 1: break
    count = count + len(data)
    print(len(data),count)
    picture = picture + data

sock_image.close()

    
# Look for the end of the header (2 CRLF)
pos = picture.find("\r\n\r\n".encode())
print('Header length',pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open('output.jpg','wb')
fhand.write(picture)
fhand.close()

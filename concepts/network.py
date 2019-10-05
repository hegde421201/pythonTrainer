'''
Network programming
--------------------

Our primary goal in this chapter is to retieve web pages using the HTTP protocol.
HTTP stands for Hypertext Transfer Protocol.

Python has built-in support for HTTP protocol called socket.

The socket provides two-way communication between two programs.One can read and write to the same socket.
If you write to a socket, it is sent to the application at the other end of the socket.
If you read from the socket, you are given the data which the other application has sent.

If you try to read a socket when the program on the other end is idle or not sent any data, you just sit and wait.
If the programs on both ends of the socket wait for each other's data without doing anything, then nothing will happen.
Hence we need a protocol or a precise set of rules to solve this possible confusion.
The protocols decide who goes first and the responses to the messages.

HTTP is one such protocol.

'''
import socket

# sock is a socket instance with two parameters.
# AF_INET refers to the family address ipv4.
# SOCKET_STREAM refers to the TCP protocol which is connection oriented.

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# connect to the data.pr4e.org server on port 80
sock.connect(('data.pr4e.org',80))

# This is a GET request with the second parameter is the web page to whom we are requesting the webpage followed by blank lines
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # encode converts strings into byte objects
sock.send(cmd)

# The server will respond with the header information about the document and a blank line followed by the
# document content.

while True:
    data = sock.recv(512) # 512 bytes of data as chunks
    if len(data) < 1: # till no more data is left to be read
        break
    print(data.decode(),end='') # decode() converts bytes to strings

sock.close()



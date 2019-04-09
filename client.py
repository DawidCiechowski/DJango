import socket

s = socket.socket()

host = socket.gethostname()

port = 12345

s.connect((host, port))
string = s.recv(1024)
print (string.decode('utf-8', 'strict'))
s.close()
import socket

c = socket.socket()
c.connect(('127.0.0.1', 5622))
tip = c.recv(1000)
print(tip)

while True:
    a = input()
    r = c.send(a.encode())

import socket

s = socket.socket()
s.bind(('127.0.0.1', 5622))
s.listen(10)

while True:
    con, msg = s.accept()
    print(con)
    print(msg)
    con.send('hello'.encode())
    con.close()
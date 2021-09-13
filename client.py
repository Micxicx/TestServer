import socket

conn = socket.socket()
conn.connect(('127.0.0.1', 9090))
while True:
    s =input("# ")
    if s == "-q":
        break
    conn.send(s.encode('utf-8'))

    data = conn.recv(1024)
    print(data)
conn.close()


import socket

conn = socket.socket()
conn.bind(('', 9090))
conn.listen(1)
connected, adr = conn.accept()

print("OK")
while True:
    data = connected.recv(1024)
    connected.send(data.upper())
    print("OK")

connected.close()
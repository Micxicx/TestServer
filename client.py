import socket
import threading

conn = socket.socket()
conn.connect(('127.0.0.1', 9090))

def send():
    while True:
        s =input("# ")
        if s == "-q":
            break
        conn.send(s.encode('utf-8'))


def reception():
    print("start1")
    while True:
        data = conn.recv(1024)
        print(data)

th1 = threading.Thread(target=send)
th2 = threading.Thread(target=reception)

th1.start()
th2.start()


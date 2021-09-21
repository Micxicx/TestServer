import socket
import threading

conn = socket.socket()
conn.bind(('', 9090))
adrr = []
c_conn = []
def join(connected,adr):
    while True:
        try:
            data = connected.recv(1024)
            for i in range(len(c_conn)):
                if c_conn[i] != connected:
                    c_conn[i].send(data.upper())
            if not data:
                print("No data")
                break
            else:
                print(data)
        except ConnectionResetError:
            print("Connect false")
            adrr.remove(adr)
            c_conn.remove(connected)
            break
    connected.close()
def rep():
    while True:
        print("new")
        conn.listen(2)
        connected, adr = conn.accept()
        print("conected",adr)
        adrr.append(adr)
        c_conn.append(connected)
        print(1)
        th2 = threading.Thread(target=join, args = (connected,adr))
        print(2)
        th2.start()
        print(3)

th1 = threading.Thread(target = rep)
th1.start()
th1.join()

conn.close()
print("Stop")
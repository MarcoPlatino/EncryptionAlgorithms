import socket
from _thread import start_new_thread
import threading

lock = threading.Lock()

i = 0
def handle_client(c):
    while True:
        data = c.recv(1024)
        if not data:
            print(f'connection: {i}')
            lock.release()
            break
        c.send(data[::-1])
        i += 1
    c.close()

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("Socket successfully created")

port = 12346

s.bind(('', port))
print("socket binded to %s" % (port))

s.listen(5)
print("socket is listening")

message = ""
while message != "stop":
    # while True:
    #     message = input("what to sendus: ")
    #     c, addr = s.accept()
    #     # print('Got connection from', addr)
    #     c.send(message.encode())
    #     print(f'Recieved From Client: {c.recv(1024).decode()}')
    #     c.close()
    #     break
    while True:
        c, addr = s.accept()
        lock.acquire()
        print('Connected to:', addr[0], ':', addr[1])
        start_new_thread(handle_client, (c,))

s.close()

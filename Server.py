import socket
from _thread import start_new_thread
import threading


def handle_client(c, i):
    client_id = c.recv(1024).decode().strip()
    print(f'Client ID: {client_id}')
    while True:
        data = c.recv(1024)
        if not data:
            print(f'disconnected from client {client_id}')
            break
        c.send(data[::-1])
        i += 1
        print(f'request: {i} on client: {client_id}')
    c.close()

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

port = 12346

s.bind(('', port))
print("socket binded to %s" % (port))

s.listen(5)
print("socket is listening")
print("----------------------------------------------")
i = 0
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
        print('Connected to:', addr[0], ':', addr[1])
        start_new_thread(handle_client, (c,i))

s.close()

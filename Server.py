import socket
from _thread import start_new_thread
import threading

lock = threading.Lock()

clients = {}


def handle_client(c, i, addr):
    client_id = c.recv(1024).decode().strip()
    print(f'Client ID: {client_id}')
    lock.acquire()
    clients[client_id] = c
    # print(clients)
    lock.release()
    try:
        while True:
            try:
                message = c.recv(1024)
                message = message.decode()
                if not message or message == 'yes':
                    continue
                recipient = message[0]
                clients[recipient].send(message[1:].encode())
                # print(f'sent {message} from {clients[c]} to {clients[recipient]}')
                confirm = clients[recipient].recv(1024)
                if confirm == b'yes' or confirm == 'yes':
                    c.send('message sent'.encode())
                else:
                    c.send('unable to confirm message'.encode())
            except:
                print('Client Error....')
                c.send("No forwarding adress....".encode())
    finally:
        lock.acquire()
        if client_id in clients:
            del clients[client_id]
        lock.release()
        c.close()

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
b = 0
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
        b += 1
        start_new_thread(handle_client, (c,i,addr))

s.close()

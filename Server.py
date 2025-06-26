import socket

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
    while True:
        message = input("what to sendus: ")
        c, addr = s.accept()
        # print('Got connection from', addr)
        c.send(message.encode())
        print(f'Recieved From Client: {c.recv(1024).decode()}')
        c.close()
        break
s.close()

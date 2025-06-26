import socket             

port = 12346       

p = " "
while p != "stop":
        s = socket.socket()
        try:      
            s.connect(('192.168.86.205', port)) 
        except:
              print("connection to server failed!?!")
        message = (s.recv(1024).decode())
        print(f'Recieved From Server: {message}')
        s.send(input("Reply: ").encode())
        s.close()

import socket             

port = 12346       
i = 0
p = " "
while p != "stop":
        s = socket.socket()
        try:
            s.connect(('192.168.86.205', port))
            print("--------------------------------------------------")
            print("Connected to server successfully!")
            print("--------------------------------------------------")
            i = 0
        except Exception as e:
            i += 1        
            print(f"Connection to server failed!?!  Attempt {i}. Retrying...")
            if i >= 10:
                 print("Failed to connect after 10 attempts. Exiting.")
                 break
            continue
        message = (s.recv(1024).decode())
        s.send('[GOT THE MESSAGE SUCESSFULLY]'.encode())
        print(f'Recieved From Server: {message}')
        s.send(input("Reply: ").encode())
        s.close()
print("The thing is done.")
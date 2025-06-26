import socket             

port = 12346 
host ='192.168.86.205'   
i = 0
p = " "
s = 0
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    while True:
        try:
            s.connect(('192.168.86.205', port))
            print("--------------------------------------------------")
            print("Connected to server successfully!")
            print("--------------------------------------------------")
            i = 0
            break
        except Exception as e:
            i += 1        
            print(f"Connection to server failed!?!  Attempt {i}. Retrying...")
            if i >= 10:
                 print("Failed to connect after 10 attempts. Exiting.")
                 break
            continue

while True:
    main()
    msg = input("What to send to the server: ")
    if msg == 'ni':
        break
    s.send(msg.encode())
    data = s.recv(1024)
    print(f'Recieved: {data.decode()}')
s.close()

# while p != "stop":
#         s = socket.socket()
        
#         message = (s.recv(1024).decode())
#         s.send('[GOT THE MESSAGE SUCESSFULLY]'.encode())
#         print(f'Recieved From Server: {message}')
#         s.send(input("Reply: ").encode())
#         s.close()
# print("The thing is done.")
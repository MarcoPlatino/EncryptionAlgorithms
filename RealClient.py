import socket     
import threading
import queue

output = queue.Queue()

def sendMessage():
    while True:
        msg = input("What to send to the server: ")
        if msg == 'ni':
            break
        s.send(msg.encode())
    s.close()
port = 12346 
host ='192.168.86.205'   
i = 0
p = " "

send = threading.Thread(target=sendMessage, daemon=True)
send.start()
def main():
    i = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            s.connect(('192.168.86.205', port))
            print("--------------------------------------------------")
            print("Connected to server successfully!")
            print("--------------------------------------------------")
            i = 0
            client_id = "1"
            s.send(client_id.encode())
            return s
        except Exception as e:
            i += 1        
            print(f"Connection to server failed!?!  Attempt {i}. Retrying...")
            if i >= 10:
                 print("Failed to connect after 10 attempts. Exiting.")
                 break
            continue
    while True:
        data = s.recv(1024)
        print(f'Recieved: {data.decode()}')

s = main()


# while p != "stop":
#         s = socket.socket()
        
#         message = (s.recv(1024).decode())
#         s.send('[GOT THE MESSAGE SUCESSFULLY]'.encode())
#         print(f'Recieved From Server: {message}')
#         s.send(input("Reply: ").encode())
#         s.close()
# print("The thing is done.")
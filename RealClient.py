import socket     
import threading
import queue

output = queue.Queue()

def sendMessage(s):
    while True:
        msg = input("What to send to the server: ")
        if msg == 'ni':
            break
        s.send(msg.encode())
    s.close()

def recieveMessage(s):
    while True:
        try:
            data = s.recv(1024)
            if not data:
                break
            print(f"Recieved: {data.decode()}")
            s.send(b'yes')
        except:
            break

def main():
    port = 12346 
    host ='192.168.86.205'  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    for i in range(10):
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
            if i == 10:
                print("Failed to connect after 10 attempts. Exiting.")
                return
        threading.Thread(target=sendMessage, args=(s,), daemon=True).start()
        recieveMessage()


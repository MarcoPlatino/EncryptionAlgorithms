# Import socket module 
import socket             

# Create a socket object 

# Define the port on which you want to connect 
port = 12346       

# connect to the server on local computer 
p = " "
while p != "stop":
    s = socket.socket()         
    s.connect(('192.168.86.205', port)) 

    # receive data from the server and decoding to get the string.
    p = (s.recv(1024).decode())
    print(p)
    s.send('recieved'.encode())
    # close the connection 
    s.close()
# Server Socket
import socket

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print ("Socket successfully created")

# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12346             

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
s.bind(('', port))
print ("socket binded to %s" %(port)) 

# put the socket into listening mode 
s.listen(5)     
print ("socket is listening")            

# a forever loop until we interrupt it or 
# an error occurs 
message = ""
while message != "di":
  while True: 
    message = input("what to sendus: ")
  # Establish connection with client. 
    c, addr = s.accept()     
    print ('Got connection from', addr )

    # send a thank you message to the client. encoding to send byte type. 
    c.send(message.encode()) 
    print(c.recv(1024).decode())
    # Close the connection with the client 
    c.close()

    # Breaking once connection closed
    break
s.close()

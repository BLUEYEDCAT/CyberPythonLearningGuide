import socket
import threading

# define the port and ip that the socket will bind with
bind_ip = "0.0.0.0"
bind_port = 9999

# define the socket (IPv4, TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the server to the local host on port 9999
server.bind ((bind_ip, bind_port))

# start the server and listen on the pre-defined port
# the server will allow 5 connections
server.listen(5)

print("The server is listening on" + bind_ip)

# define the function that handles socket coming from the client
def handle_client(client_socket):
    # receive message from the client
    request = client_socket.recv(1024)
    print(request)
    str = "ACK"
    # send back an acknowledge message back to the client
    client_socket.send(str.endcode("UTF-8"))
    # close the socket
    client_socket.close()

# enter a infinite loop
while True:
    # accpet connection
    # assign client socket object to client
    # assign client address to addr
    client, addr = server.accept()
    # address array contains host address and port
    print("Accepting Connections from" + str(addr[0])
        + " " + str(addr[1]))
    # define a thread on handle_client function
    # send the client socket object as argument
    soc_handler = threading.Thread(target = handle_client, args = (client,) )
    # start the thread
    soc_handler.start()

import socket

target_host = "127.0.0.1"
target_port = 80

# create the socket and assign it to object client
# define the address family ::: AF_INET ---> IPv4
# define the socket type ::: SOCK_DGRAM ---> UDP packets
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# The difference is that TCP requires a three way handshake
# however, udp sockets can send data to the destination without
# establishing a connection
client.sendto(str.encode("UTF-8"),(target_host,target_port))

data, address = client.recvfrom(4096)

print (data.decode("UTF-8"))

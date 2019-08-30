 ### socket library ----> provides access to low-level netowkring interface
 ### BSD socket interface (Berkeleys Sockets)
 ### socket library ----> It allows you to send sockets on most of the platforms
import socket

# define the target host and port for later uses
# Or from user prompts
target_host = "www.infopro.com.my"
target_port = 80
# define the string
# the string is a http header with get method
str = "GET / HTTP/1.1\r\nHost: infopro.com.my\r\n\r\n"

# create a function to encode string
def strEncode(str):
    return str.encode("UTF-8")

# create a function to decode string
def strDecode(str):
    return str.decode("UTF-8")

# create a function to send the message
def sendMessage():
    # create the socket and assign it to object client
    # define the address family ::: AF_INET ---> IPv4
    # define the socket type ::: SOCK_STREAM ---> TCP packets
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect the socket to a remote address
    # socket.connect(address) takes in one argument
    # it must follow the address family standard
    # in this case, IPV4 requires a string value of domain name and a port number
    client.connect((target_host, target_port))
    # receive the message in bytes object 4096
    response = client.recv(4096)
    # print out the decoded response
    print(response.decode("UTF-8"))

# define the main function
def Main():
    # try and catch error handling block
    try:
        sendMessage()
    except:
        print('cannot connect to the host/ sedn the socket to the host')
# run main function
Main()

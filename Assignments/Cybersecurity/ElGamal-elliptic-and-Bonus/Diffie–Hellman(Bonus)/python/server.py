import socket

prime = 23
generator = 9
serverPrivateKey = 5
# server generated key
serverGenKey_X = int(pow(prime, generator, serverPrivateKey))

# ----------------------- Server chat with Client -----------------------

# create a socket object
server = socket.socket()
print("Socket created successfully")

# port number for establishing the connection
port = 4545

# the first parameter is the IP address (keep it empty to accept the  requests from any coming device)
# the second parameter is the port number
server.bind(('', port))

'''
change the socket to listening mode
the passed parameter '5' is the backlog (should set the max backlog to be 5 to avoid any issue)
backlog specifies the number of unaccepted connections that the system will allow before refusing new connections
'''
server.listen(5)
print("server is listening")

# Establishing the connection between server and client
Client, clientAddress = server.accept()
print('Connected with', clientAddress)

# Send welcome to Client
welcome = """************************************
* Welcome in Diffie-Hellman Server *
************************************\n"""
Client.send(welcome.encode('ascii'))
try:

    # receive client Generated Key (Y)
    clientMessage = Client.recv(2048).decode('ascii')
    print('client Generated Key (Y): = ' + clientMessage)
    Y = int(clientMessage)
    # send server Generated Key (X)
    Client.send(str(serverGenKey_X).encode('ascii'))
    # Server Secret Key
    serverSecretKey = int(pow(prime, Y, serverPrivateKey))
    print('Server shared secret key : ' + str(serverSecretKey))

    print("closing the connection")
    Client.close()
    print('closing the server')
    server.close()

except socket.error as err:
    print(err)
    print("closing the connection")
    Client.close()
    print('closing the server')
    server.close()

# ----------------------- Server chat with Client -----------------------


# while True:
#
#     clientMessage = Client.recv(2048)
#     clientMessage = clientMessage.decode('ascii')
#
#     if clientMessage == "close":
#         print("closing the connection")
#         Client.close()
#         print('closing the server')
#         server.close()
#         break
#
#     elif clientMessage == "sendPrime":
#         # send Prime Number To Client
#         Client.send('Prime Number :  '.encode('ascii'))
#         Client.send(str(prime).encode('ascii'))
#
#     elif clientMessage == "sendGenerator":
#         # send Generator Number To Client
#         Client.send('\nGenerator Number :  '.encode('ascii'))
#         Client.send(str(generator).encode('ascii'))
#
#     elif clientMessage == "sendX":
#         Client.send('\nServer Generated Key (X) :  '.encode('ascii'))
#         Client.send(str(serverGenKey).encode('ascii'))
#
#     elif clientMessage == "secretKey":
#         Client.send('\nServer Secret Key :  '.encode('ascii'))
#         Client.send(str(serverSecretKey).encode('ascii'))

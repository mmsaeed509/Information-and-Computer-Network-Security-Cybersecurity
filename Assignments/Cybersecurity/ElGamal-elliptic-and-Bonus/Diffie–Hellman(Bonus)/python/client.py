import socket

prime = 23
generator = 9
clientPrivateKey = 3
# client generated key
clientGenKey_Y = int(pow(prime, generator, clientPrivateKey))

# ----------------------- Server chat with Client -----------------------

# create a socket object
client = socket.socket()

# port number for establishing the connection
port = 4545

# connecting to the server on localhost machine
client.connect(('127.0.0.1', port))
print(client.recv(2048).decode())

try:
    # send client Generated Key (Y)
    client.send(str(clientGenKey_Y).encode('ascii'))
    # receive server Generated Key (X)
    serverMessage = client.recv(2048).decode('ascii')
    X = int(serverMessage)
    print('server Generated Key (X): = ' + serverMessage)
    # client shared secret key
    clientSecretKey = int(pow(prime, X, clientPrivateKey))
    print('Client shared secret key : '+str(clientSecretKey))

    print("closing the connection")
    client.close()

except socket.error as err:
    print(err)
    print("closing the connection")
    client.close()

# ----------------------- Server chat with Client -----------------------

# while True:
#     # receive data from the server and decoding to start
#     print(client.recv(2048).decode())
#
#     clientMessage = input("Write a message : ")
#     client.send(clientMessage.encode('ascii'))
#
#     if clientMessage == "close":
#         print("Closing Connection")
#         client.close()
#         break

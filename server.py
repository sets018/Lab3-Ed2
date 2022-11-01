import socket

# Crea el objeto socket del servidor tcp y ipv4 por default
server = socket.socket()
print('Server socket created')

# Enlaza (bind) el socket con un port y la direccion del host
adr_host = 'localhost'
port = 1234
server.bind((adr_host, port))

# Determina el numero de conexiones
n_connections = 4
server.listen(n_connections)
print('Waiting for connections')

while True:
    client, addr = server.accept()
    name = client.recv(1024).decode()
    print("Established connection with ", addr, name)
    client.send(bytes('Welcome ','utf-8'))
    client.close()
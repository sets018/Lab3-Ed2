import socket

client = socket.socket()

client.connect(('localhost', 1234))

name = input("Enter your name")

client.sendall(bytes(name, 'utf-8'))

print(client.recv(1024).decode())

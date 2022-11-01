import socket

client = socket.socket()

client.connect(('localhost', 1234))

text = input("aaaaaaaaaaa")

client.send(bytes(text, 'utf-8'))

print(client.recv(1024).decode())

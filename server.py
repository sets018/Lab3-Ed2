import socket
import random

class usr_input:
    def __init__(self, string, options_code):
        self.inpt_string = string
        self.options_code = options_code

    def get_input_op(self):
        sw = 0
        while (sw == 0):
            op = input(self.inpt_string)
            if ((op != None)):
                if ((op in self.options_code)):
                    sw = 1
                else:
                    print("Enter a valid option")
        return op


class data:
    def __init__(self, source_type, data_source):
        self.source_type = source_type
        self.data_source = data_source
    def get_data(self):
        if (self.source_type == "1"):
            pass
        if (self.source_type == "2"):
            pass
        if (self.source_type == "3"):
            pass
            # Create random array
            #self.create_array()
            #user_array = [random.randint(lower_limit,upper_limit) for _ in range(usr_range)]

# Crea el objeto socket del servidor tcp y ipv4 por default
server = socket.socket()
print('Server socket created')
print('Welcome to the server socket')

# Enlaza (bind) el socket con un port y la direccion del host
adr_host = 'localhost'
port = 1234
server.bind((adr_host, port))

alg_op = usr_input('Select an algorithm\n1- Mergesort\n2- Heapsort\n3- Quicksort ', ["1", "2", "3"], ).get_input_op()

data_op = usr_input('How do you want to input the data?\n1- Enter file location\n2- Enter string\n3- Create random array  ',
                    ["1", "2", "3"]).get_input_op()


# Determina el numero de conexiones
server.listen()
print('Waiting for connections')

while True:
    client, addr = server.accept()
    name = client.recv(1024).decode()
    print("Established connection with ", addr, name)
    #client.send(bytes(f'Welcome the server has selected\nAlgorithm {alg_select}\nData source {data_select}', 'utf-8'))
    client.sendall(bytes(f'Welcome the server has selected\nAlgorithm {alg_op}\nData source {data_op}', 'utf-8'))
    client.close()

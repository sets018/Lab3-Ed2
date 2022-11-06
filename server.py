import socket
import numpy as np
import random
import pickle

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
                    print("Enter a valid option\n")
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
            arr = self.get_rand_arr_params()
        return arr
    def get_rand_arr_params(self):
        n = self.get_input_params("Enter the number of elements in the array\n",1)
        lower_limit = self.get_input_params("Enter the lower limit of the interval\n", 0)
        upper_limit = self.get_input_params("Enter the upper limit of the interval\n", 0)
        return self.get_rand_arr(lower_limit, upper_limit, n)
    def get_input_params(self, inpt_string, cond_int):
        sw = 0
        while (sw == 0):
            input_param = input(inpt_string)
            if ((input_param != None)):
                if (cond_int == 1):
                    if (input_param.isdigit()):
                        sw = 1
                    else:
                        print("Enter a valid option\n")
                else:
                    if ((self.is_number(input_param))):
                        sw = 1
                    else:
                        print("Enter a valid option\n")
        if (cond_int == 1):
            return int(input_param)
        else:
            return float(input_param)
    def get_rand_arr(self, lower_limit, upper_limit, n):
        #return np.random.uniform(lower_limit, upper_limit, n)
        return [random.uniform(lower_limit,upper_limit) for _ in range(n)]
    def is_number(self,number):
        return (number.replace('.', '', 1).isdigit() and number.replace('-', '', 1).isdigit())


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
if (data_op == "1"):
    pass
if (data_op == "2"):
    pass
if (data_op == "3"):
    usr_data = data("3","None").get_data()
    arr = pickle.dumps(usr_data)
    #print(type(usr_data))

# Determina el numero de conexiones
server.listen()
print('Waiting for connections')

while True:
    client, addr = server.accept()
    name = client.recv(1024).decode()
    print("Established connection with ", addr, name)
    client.sendall(bytes(f'Welcome the server has selected\nAlgorithm {alg_op}\nData source {data_op}', 'utf-8'))
    client.sendall(arr)
    client.close()

import socket
import random
import pickle
import threading
from functools import wraps
import time
import struct


def send_data(conn, data):
    size = struct.pack('I', len(data))
    conn.sendall(size)
    conn.sendall(data)


def recv_data(conn):
    size_bytes = conn.recv(4)
    size = struct.unpack('I', size_bytes)
    size = size[0]
    data = conn.recv(size)
    return data


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
    def __init__(self, source_type):
        self.source_type = source_type

    def get_data(self):
        if (self.source_type == "1"):
            arr = self.get_arr_file()
        if (self.source_type == "2"):
            arr = self.get_arr()
        if (self.source_type == "3"):
            arr = self.get_rand_arr_params()
        return arr

    def get_arr_file(self):
        sw = 0
        sw2 = 0
        file_arr = []
        while (sw2 == 0):
            while (sw == 0):
                while True:
                    file_path = input("Enter the file location\n")
                    try:
                        usr_file = open(file_path, 'r').readlines()
                    except (FileNotFoundError, IOError):
                        print("Wrong file or file path")
                    else:
                        break

                file_sep = input("Enter the separator inside the file\n")
                usr_file = self.read_file(file_path, file_sep)
                if (usr_file != None):
                    if (len(usr_file) >= 2):
                        sw = 1
                    else:
                        print("Enter a valid file or separator\n")
            for number in usr_file:
                if (self.is_float(number)):
                    number = float(number)
                    file_arr.append(number)
            if (file_arr != None):
                if (len(file_arr) >= 2):
                    sw2 = 1
                else:
                    sw = 0
                    print("Enter a valid array or separator\n")
        return file_arr

    def read_file(self, file_path, file_sep):
        with open(file_path, 'r') as file:
            usr_file = file.read().replace('\n', '')
            usr_file = usr_file.split(file_sep)
        return usr_file

    def get_arr(self):
        sw = 0
        sw2 = 0
        arr = []
        while (sw2 == 0):
            while (sw == 0):
                usr_arr = input("Enter the array\n")
                sep = input("Enter the separator\n")
                usr_arr = usr_arr.split(sep)
                if (usr_arr != None):
                    if (len(usr_arr) >= 2):
                        sw = 1
                    else:
                        print("Enter a valid array or separator\n")
            for number in usr_arr:
                if (self.is_float(number)):
                    number = float(number)
                    arr.append(number)
            if (arr != None):
                if (len(arr) >= 2):
                    sw2 = 1
                else:
                    sw = 0
                    print("Enter a valid array or separator\n")
        return arr

    def get_rand_arr_params(self):
        n = self.get_input_params("Enter the number of elements in the array\n", 1)
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
        # return np.random.uniform(lower_limit, upper_limit, n)
        return [random.uniform(lower_limit, upper_limit) for _ in range(n)]

    def is_number(self, number):
        return (number.replace('.', '', 1).isdigit() and number.replace('-', '', 1).isdigit())

    def is_float(self, number):
        try:
            float(number)
            return True
        except:
            return False


sw = "1"
while (sw == "1"):
    # Crea el objeto socket del servidor tcp y ipv4 por default
    server = socket.socket()
    print('Server socket created')
    print('Welcome to the server socket')

    # Enlaza (bind) el socket con un port y la direccion del host
    adr_host = 'localhost'
    port = 1234
    server.bind((adr_host, port))

    alg_op = usr_input('Select an algorithm\n1- Mergesort\n2- Heapsort\n3- Quicksort ',
                       ["1", "2", "3"], ).get_input_op()
    if (alg_op == "3"):
        pivot_op = usr_input('Select a pivot for quicksort\n1- Far left\n2- Far right\n3- Middle\n4- Double',
                       ["1", "2", "3", "4"], ).get_input_op()
    data_op = usr_input(
        'How do you want to input the data?\n1- Enter file location\n2- Enter string\n3- Create random array  ',
        ["1", "2", "3"]).get_input_op()

    usr_data = data(data_op).get_data()
    arr = pickle.dumps(usr_data)

    # Determina el numero de conexiones
    server.listen()
    print('Waiting for connections')
    while True:
        client, addr = server.accept()
        name = recv_data(client).decode()
        print("Established connection with ", addr, name)
        send_data(client, bytes(f'Welcome the server has selected\nAlgorithm {alg_op}\nData source {data_op}', 'utf-8'))
        send_data(client, arr)
        send_data(client, bytes(alg_op, 'latin-1'))
        if (alg_op == "3"):
            send_data(client,bytes("1", 'utf-8'))
            send_data(client, bytes(pivot_op, 'latin-1'))
        else:
            send_data(client, bytes("0", 'utf-8'))
        sw2 = "1"
        while (sw2 == "1"):
            sw2 = recv_data(client).decode()
            if (sw2 == "0"):
                break
            msg = recv_data(client).decode()
            print(msg)
        res_arr_bytes = recv_data(client)
        if (res_arr_bytes == None):
            print("sending sorted arr client to server failed")
        if (res_arr_bytes != None):
            print("sorted array received from server")
            sorted_arr = pickle.loads(res_arr_bytes)
            if (sorted_arr == None):
                print("Unpickilng in server failed")
            # arr = np.frombuffer(arr_bytes, dtype = float)
            show_arr = usr_input('Print the sorted array received from the client\n1- Yes\n2- No ',
                                 ["1", "2"], ).get_input_op()
            if (show_arr == "1"):
                print(*sorted_arr, sep=", ")
                sw = usr_input('Do you want to try another algorithm/data? (keeps running the server)\n1- Yes\n2- No ',
                               ["1", "2"], ).get_input_op()
            server.close()
            if (sw == "1"):
                break
            if (sw == "2"):
                print("Closing server")

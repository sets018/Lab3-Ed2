import socket
import pickle
#import numpy as np

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

class sorter:
    def __init__(self, arr, alg_option, client):
        self.arr = arr
        self.alg_option = alg_option
        self.client = client 
    def sort(self):
        if (alg_op == "1"):
            pass
            #sorted_arr = mergesort(arr)
        if (alg_op == "2"):
            pass
            #sorted_arr =heapsort(arr)
        if (alg_op == "3"):
            pass
            #sorted_arr = quicksort(arr)   
        return sorted_arr
    def get_n(self):
        
client = socket.socket()

client.connect(('localhost', 1234))

name = input("Enter your name\n")

client.sendall(bytes(name, 'utf-8'))

print(client.recv(1024).decode())

arr_bytes = client.recv(4096)

if (arr_bytes != None):
    print("array received from server")
    arr = pickle.loads(arr_bytes)
    alg_op = client.recv(4096).decode()
    #arr = np.frombuffer(arr_bytes, dtype = float)
    show_arr = usr_input('Print the array received from the server\n1- Yes\n2- No ',
                       ["1", "2"], ).get_input_op()
    if (show_arr == "1"):
        print(*arr, sep=", ")
    sort_arr = sorter(arr, alg_op).sort()
    res_arr = pickle.dumps(sort_arr)
    client.sendall(res_arr)

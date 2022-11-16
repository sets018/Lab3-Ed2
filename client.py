import socket
import pickle
import threading
from functools import wraps
import time
import math
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


def timeit(func):
    cont = 0

    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        nonlocal cont
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        cont = cont + 1
        end_time = time.perf_counter()
        total_time = end_time - start_time
        if cont % (round(math.log(n_arr))) == 0:
            sw = bytes("1", 'utf-8')
            send_data(client, sw)
            #print(f'Function {func.__name__} Iteration {cont} Took {total_time:.4f} seconds')
            msg = bytes(f'Function {func.__name__} Iteration {cont} Took {total_time:.4f} seconds', 'utf-8')
            send_data(client, msg)
        return result

    return timeit_wrapper


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
    def __init__(self, arr, alg_op, pivot_op):
        self.arr = arr
        self.op = pivot_op
        self.alg_op = alg_op

    def sort(self):
        if (self.alg_op == "1"):
            sorted_arr = self.mergesort(self.arr)
        if (self.alg_op == "2"):
            sorted_arr = self.heapsort(self.arr)
        if (self.alg_op == "3"):
            sorted_arr = self.quickSort(self.arr, 0, len(self.arr) - 1)
        return sorted_arr

    def rightPartition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1

    def leftPartition(self, array, low, high):
        pivot = low
        for i in range(low + 1, high + 1):
            if array[i] <= array[low]:
                pivot += 1
                (array[i], array[pivot]) = (array[pivot], array[i])
        (array[pivot], array[low]) = (array[low], array[pivot])
        return pivot

    @timeit
    def quickSort(self, array, low, high):
        if low < high:
            # Para seleccionar pivote inicial escoger entre left y right metodos
            pi = self.leftPartition(array, low, high)
            self.quickSort(array, low, pi - 1)
            self.quickSort(array, pi + 1, high)
        return arr

    @timeit
    def heapsort(self, arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.buildheap(arr, n, i)
        for i in range(n - 1, 0, -1):
            (arr[i], arr[0]) = (arr[0], arr[i])
            self.buildheap(arr, i, 0)
        return arr

    def buildheap(self, arr, n, i):
        large = i
        left = 2 * i + 1
        right = 2 * i + 2
        if (left < n) and (arr[i] < arr[left]):
            large = left

        if right < n and arr[large] < arr[right]:
            large = right

        if large != i:
            (arr[i], arr[large]) = (arr[large], arr[i])
            self.buildheap(arr, n, large)

    @timeit
    def mergesort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            self.mergesort(left)
            self.mergesort(right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        return arr


sw = "1"
while (sw == "1"):
    client = socket.socket()

    client.connect(('localhost', 1234))

    print("Connected to server")

    print("Welcome")

    sw_pivot = "0"

    name = input("Enter your name\n")

    name_coded = bytes(name, 'utf-8')

    send_data(client, name_coded)

    text = recv_data(client).decode()

    print(text)

    arr_bytes = recv_data(client)

    alg_op = recv_data(client).decode('latin-1')

    pivot_op = "1"

    sw_pivot = recv_data(client).decode('utf-8')

    if (sw_pivot == "1"):
        pivot_op = recv_data(client).decode('latin-1')

    if ((arr_bytes != None) and (alg_op != None)):
        print("array received from server")
        arr = pickle.loads(arr_bytes)
        n_arr = len(arr)
        # arr = np.frombuffer(arr_bytes, dtype = float)
        show_arr = usr_input('Print the array received from the server\n1- Yes\n2- No ',
                             ["1", "2"], ).get_input_op()
        if (show_arr == "1"):
            print(*arr, sep=", ")
        main_time = time.perf_counter()
        sort_arr = sorter(arr, alg_op, pivot_op).sort()
        ending_time = time.perf_counter()
        print(f'Total sorting time: {ending_time - main_time}')
        msg = bytes("0", 'utf-8')
        send_data(client, msg)
        if (sort_arr == None):
            print("sorting in client failed")
        res_arr = pickle.dumps(sort_arr)
        if (res_arr == None):
            print("pickle in client failed")
        send_data(client, res_arr)
        sw = usr_input('Do you want to receive more data from server? (keeps running the client)\n1- Yes\n2- No ',
                       ["1", "2"], ).get_input_op()
        client.close()
    if (sw == "2"):
        print("Closing client")

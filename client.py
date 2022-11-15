import socket
import pickle
import time
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
    def __init__(self, arr, alg_op, client):
        self.arr = arr
        self.alg_op = alg_op
        self.client = client
    def sort(self):
        if (self.alg_op == "1"):
            sorted_arr = self.mergesort(self.arr)
        if (self.alg_op == "2"):
            sorted_arr = self.heapsort(self.arr)
        if (self.alg_op == "3"):
            sorted_arr = self.quicksort(self.arr,  0, len(self.arr) - 1)
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
    def quickSort(self, array, low, high):
        if low < high:
            # Para seleccionar pivote inicial escoger entre left y right metodos
            pi = self.leftPartition(array, low, high)
            self.quickSort(array, low, pi - 1)
            self.quickSort(array, pi + 1, high)
    def heapsort(self,arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.buildheap(arr, n, i)
        for i in range(n - 1, 0, -1):
            (arr[i], arr[0]) = (arr[0], arr[i])
            self.buildheap(arr, i, 0)
    def buildheap(self,arr, n, i):
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
    def get_time(self):
        start = time.time()
        a = 0
        for i in range(j):
            a += (i ** 100)
        # store iteration end timestamp
        end = time.time()
        # show time of execution per iteration
        print(f"Iteration: {j}\tTime taken: {(end - start) * 10 ** 3:.03f}ms")

client = socket.socket()

client.connect(('localhost', 1234))

name = input("Enter your name\n")

client.sendall(bytes(name, 'utf-8'))

print(client.recv(1024).decode())

arr_bytes = client.recv(4096)
alg_op = client.recv(4096).decode()

if (arr_bytes != None):
    print("array received from server")
    arr = pickle.loads(arr_bytes)
    #arr = np.frombuffer(arr_bytes, dtype = float)
    show_arr = usr_input('Print the array received from the server\n1- Yes\n2- No ',
                       ["1", "2"], ).get_input_op()
    if (show_arr == "1"):
        print(*arr, sep=", ")
    sort_arr = sorter(arr, alg_op, client).sort()
    res_arr = pickle.dumps(sort_arr)
    client.sendall(res_arr)

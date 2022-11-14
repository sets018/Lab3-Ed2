import random
def BuildHeap(arr, n, i):
	large = i 
	left = 2 * i + 1 
	right = 2 * i + 2 

	if (left < n) and (arr[i] < arr[left]):
		large = left

	if right < n and arr[large] < arr[right]:
		large = right

	if large != i:
		(arr[i], arr[large]) = (arr[large], arr[i]) 
		BuildHeap(arr, n, large)

def HeapSort(arr):
	n = len(arr)

	for i in range(n // 2 - 1, -1, -1):
		BuildHeap(arr, n, i)

	for i in range(n - 1, 0, -1):
		(arr[i], arr[0]) = (arr[0], arr[i])
		BuildHeap(arr, i, 0)

if __name__ == '__main__':
    arr = []
    for i in range(100):
        arr.append(random.randint(-100000,100000))
    print("Lista dada:", end="\n")
    print(arr)
    HeapSort(arr)
    print("Lista ordenada ascendentemente: ", end="\n")
    print(arr)
    


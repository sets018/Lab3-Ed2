import random 
def rightPartition(array, low, high):
	pivot = array[high]
	i = low - 1
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1

def leftPartition(array, low, high):
    pivot = low
    for i in range(low+1, high+1):
        if array[i] <= array[low]:
            pivot += 1
            (array[i], array[pivot]) = (array[pivot], array[i])
    (array[pivot], array[low]) = (array[low], array[pivot])
    return pivot

def quickSort(array, low, high):
	if low < high:
        #Para seleccionar pivote inicial escoger entre left y right metodos
		pi = leftPartition(array, low, high)
		quickSort(array, low, pi - 1)
		quickSort(array, pi + 1, high)


if __name__ == '__main__':
    arr = []
    for i in range(20):
        arr.append(random.randint(-100000,100000))
    print("Lista dada:", end="\n")
    print(arr)
    quickSort(arr, 0, len(arr) - 1)
    print("Lista ordenada ascendentemente: ", end="\n")
    print(arr)
    
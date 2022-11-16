import random 
import copy
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

def midPartition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def dualPartition(arr, low, high):
	
	if arr[low] > arr[high]:
		arr[low], arr[high] = arr[high], arr[low]
		
	j = k = low + 1
	g, p, q = high - 1, arr[low], arr[high]
	
	while k <= g:
		if arr[k] < p:
			arr[k], arr[j] = arr[j], arr[k]
			j += 1

		elif arr[k] >= q:
			while arr[g] > q and k < g:
				g -= 1	
			arr[k], arr[g] = arr[g], arr[k]
			g -= 1

			if arr[k] < p:
				arr[k], arr[j] = arr[j], arr[k]
				j += 1				
		k += 1	
	j -= 1
	g += 1
	arr[low], arr[j] = arr[j], arr[low]
	arr[high], arr[g] = arr[g], arr[high]
	return j, g

def quickSort(array, low, high,op):
    if low < high:
        if(op=="1"):
            pi = leftPartition(array, low, high)
            quickSort(array, low, pi - 1, op)
            quickSort(array, pi + 1, high, op)           
        if(op=="2"):
            pi = rightPartition(array, low, high)
            quickSort(array, low, pi - 1, op)
            quickSort(array, pi + 1, high, op)
        if(op=="3"):
            pi = midPartition(array, low, high) 
            quickSort(array, low, pi, op)
            quickSort(array, pi + 1, high, op)
        if(op=="4"):
            lp, rp = dualPartition(arr, low, high)
            quickSort(arr, low, lp - 1,op)
            quickSort(arr, lp + 1, rp - 1,op)
            quickSort(arr, rp + 1, high,op)






if __name__ == '__main__':
    arr = []
    for i in range(50):
        arr.append(random.randint(-100000,100000))
    print(f'{arr} original')
    test = copy.deepcopy(arr)
    test.sort()
    op = input("Select a the pivot")
    quickSort(arr, 0, len(arr) - 1, op)
    if test == arr:
        print("bueno")
    else:
        print("malo")
    print(f'{arr} ordenado')


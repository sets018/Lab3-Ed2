import random
def MergeSort(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		left = arr[:mid]
		right = arr[mid:]
		MergeSort(left)
		MergeSort(right)
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

if __name__ == '__main__':
    arr = []
    for i in range(100):
        arr.append(random.randint(-100000,100000))
    print("Lista dada:", end="\n")
    print(arr)
    MergeSort(arr)
    print("Lista ordenada ascendentemente: ", end="\n")
    print(arr)

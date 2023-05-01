"""
Sorting Algo

1. Heap sort
2. Merge sort
3. Quick sort


Algorithm   	            Time Complexity	                           Space Complexity
 	            Best    	    Average     	Worst	                    Worst

Selection Sort	Ω(n^2)	        θ(n^2)	        O(n^2)	                    O(1)
Bubble Sort	    Ω(n)	        θ(n^2)	        O(n^2)	                    O(1)
Insertion Sort	Ω(n)	        θ(n^2)	        O(n^2)	                    O(1)
Heap Sort	    Ω(n log(n))	    θ(n log(n))	    O(n log(n))	                O(1)
Quick Sort	    Ω(n log(n))	    θ(n log(n))	    O(n^2)	                    O(log(n))
Merge Sort	    Ω(n log(n))	    θ(n log(n))	    O(n log(n))	                O(n)
Bucket Sort	    Ω(n +k)	        θ(n +k)	        O(n^2)	                    O(n)
Radix Sort	    Ω(nk)	        θ(nk)	        O(nk)	                    O(n + k)
Count Sort	    Ω(n +k)	        θ(n +k)	        O(n +k)	                    O(k)
Shell Sort	    Ω(n)	        θ(n log(n))	    O(n log(n))	                O(1)
Tim Sort	    Ω(n)	        θ(n log(n))	    O(n log (n))	            O(n)
Tree Sort	    Ω(n log(n))	    θ(n log(n))	    O(n^2)	                    O(n)
Cube Sort	    Ω(n)	        θ(n log(n))	    O(n log(n))	                O(n)
"""

####################
	# Heap Sort
####################




####################
	# Merge Sort
####################
def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1


array = [ 10, 7, 8, 9, 1, 5]
print(f'Original array: {array}')
mergeSort(array)
print(f'Sorted array: {array}')



####################
	# Quick Sort
####################
def partition(array, low, high):
	# pivot = last element of the array
	pivot = array[high]
	i = low - 1

	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			array[i], array[j] = array[j], array[i]

	array[i + 1], array[high] = array[high], array[i + 1]
	return i + 1


def quick_sort(array, low, high):
	if low < high:
		partition_index = partition(array, low, high)
		quick_sort(array, low, partition_index - 1)
		quick_sort(array, partition_index + 1, high)


array = [ 10, 7, 8, 9, 1, 5]
print(f'Original array: {array}')
quick_sort(array, 0, len(array) - 1)
print(f'Sorted array: {array}')


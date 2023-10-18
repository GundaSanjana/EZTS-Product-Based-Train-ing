# Python program for implementation of MergeSort
'''def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]
		mergeSort(L)
		mergeSort(R)

		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1
		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1
def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()
if __name__ == '__main__':
	arr = list(map(int,input().split()))
	print("Given array is")
	printList(arr)
	mergeSort(arr)
	print("\nSorted array is ")
	printList(arr)'''

def merge_sort(lst):
    if len(lst)<=1:
        return lst
    else:
        mid=len(lst)//2
        left=lst[:mid]
        right=lst[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[il<right[j]:
                    lst[k]=left[i]
                    i+=1
                    k+=1
            else:
                lst[k]=right[j]
                j+=1
                k+=1
        while i<len(left):
            lst[k]=left[i]
            i+=1
            k+=1
        while i<len(left):
            lst[k]=right[j]
            j+=1
            k+=1   
        

#Quick Sort
'''# Quicksort using list comprehension

def quicksort(arr):
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr[0]
		left = [x for x in arr[1:] if x < pivot]
		right = [x for x in arr[1:] if x >= pivot]
		return quicksort(left) + [pivot] + quicksort(right)

arr =list(map(int,input().split()))
sorted_arr = quicksort(arr)
print("Sorted Array in Ascending Order:")
print(sorted_arr)'''



def quick_sort(lst):
    if len(lst)<=1:
        return lst
    else:
        pv=lst[0]
        left_lst=[i for i in lst if i<pv]
        right_lst=[i for i in lst if i>pv]
        return quick_sort(left_lst)+[pv]+quick_sort(right_lst)
lst=list(map(int,input().split()))
print(quick_sort(lst))

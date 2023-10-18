#Selection sort
'''arr=[56,32,78,43,56,67,89]
for i in range(len(arr)):
    min_ind=i
    for j in range(i+1,len(arr)):
        if arr[min_ind]>arr[j]:
            min_ind=j  #finding the min element index

    #swapping the element with min element
    arr[i],arr[min_ind]=arr[min_ind],arr[i]
        
print(arr)'''


def selection_sort(lst):
    for i in range(len(lst)):
        min_ind=i
        for j in range(i+1,len(lst)):
            if lst[j]<lst[min_ind]:
                   min_ind=j
        lst[i],lst[min_ind]=lst[min_ind],lst[i]

    for i in range(len(lst)):
        print(lst[i],end=' ')
lst=list(map(int,input().split()))
selection_sort(lst)

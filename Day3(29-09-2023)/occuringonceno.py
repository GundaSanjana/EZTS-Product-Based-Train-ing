'''In the given array every number occurs twice only one number
occurs once.Find out the no occuring once
i/p=arr=[1,5,1,2,3,2,3]
o/p=5'''
def findsingle(arr,n):
    res=arr[0]
    for i in range(1,n):
        res=res^arr[i]
    return res
arr=[2,3,5,4,5,3,4,2,88]
print(findsingle(arr,len(arr)))

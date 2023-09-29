'''After creating an array find out the smallest missing positive integer
i/p=[3,7,-5,-6,0,4]
o/p=1
i/p=[3,1,-5,-6,0,4]
o/p=2
i/p=[1,2,3,4,-5]
o/p=0
i/p=[3,1,-5,2,0]
o/p=4'''
'''def missing_no(n,arr):
    chk=0
    for i in range(len(arr)):
        if arr[i]==1:
            chk+=1
        if arr[i]<0:
            arr[i]=1
        
    if chk==0:
        return 1
    for i in range(len(arr)):
        val=abs(arr[i])-1
        if val>=0 and val<len(arr):
            arr[val]=-1*abs(arr[val])
    for i in range(len(arr)):
        if arr[i]=0:
            return i+1
    return len(arr)+1
n=int(input())
arr=list(map(int,input().split(",")))
print(missing_no(n,arr))'''


def miss(arr):
    nums=set(arr)
    l=0
    while l in nums:
        l += 1
    return l
arr=list(map(int,input().split(',')))
res=miss(arr)
print(res)


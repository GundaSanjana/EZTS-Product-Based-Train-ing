'''for the given no n check whether the kth bit is set or not.
n=10,k=3
form=>n&(1<<k-1)
set or not'''
n=int(input())
k=int(input())
if n&(1<<k-1)==0:
    print("Not set")
else:
    print("Set")
    


def sum(arr):
    s=0
    for i in arr:
        s+=i
    return s
arr=list(map(int,input().split(",")))
print(sum(arr))



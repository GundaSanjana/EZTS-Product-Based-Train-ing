#Print nth term of fibonacci series
n=int(input())
n1=0
n2=1
if(n<0):
    print("Not Possible")
else:
    for i in range(0,n-1):
        n3=n1+n2
        n1=n2
        n2=n3
    print(n2)

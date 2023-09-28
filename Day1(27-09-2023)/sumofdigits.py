'''Get one number as input find out sum of digits of given number
using while loop and for loop'''

'''n=int(input())
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
print(s)'''

n=int(input())
s=0
for i in range(n):
    r=n%10
    s=s+r
    n=n//10
print(s)

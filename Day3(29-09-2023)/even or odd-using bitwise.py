'''check number odd or even
normal way n%2==0 even or odd
fastest way using bitwise'''

n=int(input())
if(n&1==0):
    print("Even")
else:
    print("Odd")

'''explanation:
every number is formed in ways of powers of 2
thats y 2 to the power 0,1,2
so pow(2,1)=2
2,8,16...
now only number which has power of 2 is odd is pow(2,0)=1'''

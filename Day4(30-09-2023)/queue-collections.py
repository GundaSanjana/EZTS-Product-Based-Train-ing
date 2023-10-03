#Function Implementation Stack
from collections import deque
l=deque()
n=int(input("Enter number of elements:"))
for i in range(n):
    l.append(int(input("Enter a element:")))
print(l)
for i in range(n):
    #print(l.pop(0)) #we get error here as all indexes are completed
    print(l.popleft())
print(l)

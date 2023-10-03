#Simple Stack
l=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    l.append(int(input("Enter a element:")))
print(l)
for i in range(n):
    print(l.pop())
print(l)



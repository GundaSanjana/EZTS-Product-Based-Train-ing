def subset(li,target_Sum,ele=0):
    li1=[]
    if sum(li1) == target_Sum:
        print(li1)
    if ele == len(li):
        return
    target_Sum=target_Sum-li[ele]
    if target_Sum<0:
        li1.append(li[ele])
        subset(li,target_Sum,ele+1)
    elif target_Sum==0:
        print(li1)
        

li=list(map(int,input().split(",")))
target_Sum=int(input())
s=sum(li)
for i in li:
        if i>target_Sum:
            li.pop()
if target_Sum>=min(li) and target_Sum<s:
    subset(li,target_Sum)
else:
    print("invalid")
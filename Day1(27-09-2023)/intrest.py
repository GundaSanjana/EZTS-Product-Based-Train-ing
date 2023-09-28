//1st method
'''a=int(input())
i=int(input())
m5=int(input())
m9=int(input())
i1=(a*4/12*i)/100;
i2=((a-m5)*4/12*i)/100;
m=((a-m5+m9)*4/12*i)/100;
print((a-m5+m9)+i1+i2+m)'''

//2nd method
p=int(input())
SI1=(p*(4/12)*12)/100;
p=p-25000
SI2=(p*(4/12)*12)/100;
p=p+10000
SI3=(p*(4/12)*12)/100;
p=p+SI1+SI2+SI3
print(p)

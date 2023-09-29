#swapping 2 no's using XOR
a=100
b=200
print("a:",a,"b:",b)
a=a^b #a=100^200
b=a^b #b=100^200^200 ans 200 200 cancelled b=100
a=a^b #a=100^200^100 ans 100 gets cancelled a=200
print("a:",a,"b:",b)

#Bit Manipulation Tricks
#XOR
print(5^5)  #x^x=0 any no XOR with itself is 0
print(5^5^5) #XOR of no with 0 is no itself
print(1^2^3) #even1's=>0
print(4^5^6)  #odd 1's=>1
#Right shift
#divide the no by shift value times,
print(5>>1)#we divide only 1time 5/2=2 so o/p=2
print(5>>2)#here we divide 2 times 5/2=2=>2/2=1 so o/p=1
print(14>>2)#divide 2 times 14/2=7=>7/2=3 so o/p=3
print(6>>3)#divide 3 times 6/3=2=>2/2=1=>1/2=0 so o/p=0
print(9>>1)#divide 1 time 9/2=4 so o/p=4
print(9>>2)#divide 2 times 9/2=4=>4/2=2 so o/p=2
print(9>>3)#divide 3 times 9/2=4=>4/2=2=>2/2=1 so o/p=1
print(9>>4)#divide 4 times 9/2=4=>4/2=2=>2/2=1=>1/1=0 so o/p=0
#left shift
#no*power(2,shifting value)=ans
print(10<<3) #10*power(2,3)=>10*8=80 so o/p=80
print(9<<4)  #9*power(2,4)=>9*16=144 so o/p=144

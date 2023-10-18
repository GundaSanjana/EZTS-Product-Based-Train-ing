#generating paranthesis of similar type
'''def generateparanthesis(n):
    def generate(partial,left,right,valid_combinations=[]):
        if left>0:
            generate(partial + '(',left-1,right)
        if right>left:
            generate(partial + ')',left,right-1)
        if left==0 and right==0:
            valid_combinations.append(partial)
        return valid_combinations
    return generate('',n,n)
n=2
print(generateparanthesis(n))'''



def paren(res,n,op,cl,str):
    if op==cl and cl==n:
        res.append(str)
        return
    if op<n:
        paren(res,n,op+1,cl,str+"(")
    if cl<op:
         paren(res,n,op,cl+1,str+")")
def gen_par(n):
    res=[]
    paren(res,n,0,0,"")
    return res
n=int(input())
x=gen_par(n)
for i in x:
    print(i)

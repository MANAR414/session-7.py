a=0
b=1
numb=int(input('enter the nth term of fibonacci:'))

def nth_fibonacci_num(numb):
     for i in range (numb):
         global a,b
         f=a 
         a,b=b,a+b
     print(f)

nth_fibonacci_num(numb)

#fibonnaci program
def fib_normal(n):
    fib=[]
    if n>=1:
        a=0
        fib.append(a)
    if n>=2:
        b=1
        fib.append(b)
    if(n>2):
        while(n-2):
            c=a+b
            fib.append(c)
            a,b=b,c
            n-=1
    return fib
print(fib_normal(3))



#fibonnaci with recursion
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

print(fibonacci(10))

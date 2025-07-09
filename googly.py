#if some of the digit is prime its googly

def googly(num):
    t=num
    sum=0
    while num>0:
        r=num%10
        sum+=r
        num=num//10
    print(sum)
    for i in range(2,t):
        if t%i==0:
            return False
        else:
            return True
if googly(3):
    print("prime")
else:
    print("not prime")

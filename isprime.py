

def isprime_no(n):
    if n==1:
        return False
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True


n=int(input())  
if isprime_no(n):
    print(n,"is a prime no")
else:
    print(n,"is not a prime no")


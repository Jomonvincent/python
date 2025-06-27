'''n=int(input("Enter an integer: "))
sum=0
for i in range(1,n+1):
    sum+=n**i
print(f"sum of n+nn+....n*n: {sum}")'''

n=input("Enter a integer: ")
print(str(n))
print(f"{n}+{n+n}+{n+n+n} = {int(n)+int(n+n)+int(n+n+n)}")
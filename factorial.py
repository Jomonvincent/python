#program to find factorial of a number
num=int(input("Enter a positive integer : "))
num=abs(num)
fact=1
for i in range(1,num+1):
    fact*=i
    print(fact)
print(f"factorial of {num} = {fact}")
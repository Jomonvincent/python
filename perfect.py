import math
r1=int(input("Enter a 4 digit number: "))
while(r1<1000 or r1>9999):
    r1=int(input("Enter a 4 digit number (1000-9999): "))
r2=int(input(f"Enter a 4 digit number greater than {r1}: "))
while(r2<r1 or r2>9999):
    r2=int(input(f"Enter a 4 digit number greater than {r1}: "))
found=False
for i in range(r1,r2+1):
    if(math.sqrt(i)%1==0):
        if(all(int(digit)%2==0 for digit in str(i))):
            print(f"perfect square: {i}")
            found=True
print(found)
            

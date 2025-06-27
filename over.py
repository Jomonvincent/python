nums=input("Enter some numbers seperated by space:")
print(nums)
n=nums.split()
for i in range(len(n)):
    if int(n[i])>=100:
        n[i]="over"
print(n)




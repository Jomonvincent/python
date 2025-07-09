arm=[]
for i in range(1,1001):
    sum=0
    num=str(i)
    for d in num:
        sum+=int(d)**len(num)
    if sum==int(num):
        arm.append(num)
print(arm)

#or

def armstrong(num):
    temp=num
    count=0
    while temp>0:
        count+1
        temp=temp//10
    temp=num
    sum=0
    while temp>0:
        r=temp%10
        sum+=r**count
        temp=temp//10
    return sum==num

for i in range(1,1000):
    if armstrong(i):
        print(i)
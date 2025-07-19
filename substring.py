#how to find the target sum from a list
a=[2,4,3,4,5,6,3,9,7,6]
dic={}
for i,num in enumerate(a):
    if num not in dic:
        dic[num]=i
print(dic)
t=15
i=0
while True:
    d=t-a[i]
    if d in dic:
        print(a[i],dic[d])
        break
    else:
        i+=1
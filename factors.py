'''n=100
k=3
for i in range(n,1,-1):
    if n%i==0:
        print(i)
'''


n=100
k=3
res=[]
for i in range(1,int(n**0.5),1):
    if n%i==0:
        res.append(i)
        if i!=n//i:
            res.append(n//i)
res.sort(reverse=True)
print(res)
if k<=n:
    print(res[k-1])
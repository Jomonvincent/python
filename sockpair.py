socks=[10,20,10,10,30,50,50,10,20]
dic={}
n=0
for i in socks:
    dic[i]=dic.get(i,0)+1
for i in dic:
        n+=dic[i]//2
print(dic)
print(n)
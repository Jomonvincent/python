string="ABC"
n=len(string)-1
ans=0
while n>0:
    for i in string:
        ans+=ord(i)*10**n
        print(ans)
        n-=1
print(ans)

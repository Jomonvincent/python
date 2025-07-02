a1=[1,3,5,]
a2=[2,4,6]
result=[]
i=j=0
while(i<len(a1) and j<len(a2)):
    if a1[i]<a2[j]:
        result.append(a1[i])
        i+=1
    else:
        result.append(a2[j])
        j+=1
if i==len(a1):
    result.extend(a2[j:])
elif j==len(a2):
    result.extend(a1[i:])
print(result)
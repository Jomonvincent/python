#input=3,5,2,0,0,3,0,7,0
#output=3,5,2,3,7,0,0,0,0
arr=[3,5,2,0,0,3,0,7,0]
new_arr=[]
c=0
for num in arr:
    if num!=0:
        new_arr.append(num)
    else:
        c+=1
n=len(new_arr)
for i in range(n,n+c,1):
    new_arr.append(0)
print(arr)
print(new_arr)

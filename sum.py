total=0
arr=[1,5,4,2,6]
n=len(arr)+1
'''for i in range(n+2):
   total+=i
#for j in arr:
#    total-=j
total-=sum(arr)
print(total)
arr.sort()
print(arr)'''
total=n*(n+1)//2
s=sum(arr)
print(total-s)

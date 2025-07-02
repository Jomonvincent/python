arr=[-2,1,-3,4,-1,2,1,-5,4]
cs=ms=0
for i in range(len(arr)):
    cs+=arr[i]
    if cs<0:
        cs=0
    elif cs>ms:
        ms=cs
print(ms)
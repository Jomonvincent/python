def dailytemp(t):
    n=len(t)
    res=[0]*n
    for i in range(n):
        for j in range(i+1,n):
            if t[j]>t[i]:
                res[i]=j-i
                break
    return res
l=[172,74,76,71,69,89,678]
print(dailytemp(l))
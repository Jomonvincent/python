def pro_array(nums):
    n=len(nums)
    l=[1]*n         #create left subarray and set l[0]=1
    r=[1]*n         #create right subarray and set l[n-1]=1
    ans=[1]*n
    for i in range(1,n,1):
        l[i]=l[i-1]*nums[i-1]
    for i in range(n-2,-1,-1):
        r[i]=r[i+1]*nums[i+1]
    for i in range(n):
        ans[i]=l[i]*r[i]
    return ans      
nums=[1,2,3,4]
print(pro_array(nums))
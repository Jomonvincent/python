def twosum(nums,target):
    result=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
            else:
                j+=1

nums=[3,2,4]
target=6
print(twosum(nums,target))

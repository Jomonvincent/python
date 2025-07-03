#trapping rain water problem using sub array concept
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l[]
        r[0]*n
        sum=0
        for i in range(n):
            if height[i]>l[i]:
                l[i]=height[i]
        for i in range(n,-1,-1):
            if height[i]>r[i]:
                r[i]=height[i]
        for i in range(n+1):
            hmin=min(l[i],r[i])
            sum=sum+hmin-height[i]
        return sum
        
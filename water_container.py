class Solution:
    def maxArea(self, height: List[int]) -> int:
        s=0
        e=len(height)-1
        max_area=0
        while s<e:
            #area=min(height[s],height[e])*(e-s) or
            h1=height[s]
            h2=height[e]
            min_h=min(h1,h2)
            w=e-s
            area=min_h*w
            max_area=max(area,max_area)
            if height[s]<height[e]:
                s+=1
            elif height[s]>height[e]:
                e-=1
            else:
                s+=1
                e-=1
        return max_area

height=[1,8,6,2,5,4,8,3,7]
Solution.maxArea(height)
        
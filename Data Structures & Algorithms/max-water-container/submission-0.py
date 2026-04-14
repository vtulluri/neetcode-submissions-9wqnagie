class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        l,r=0,len(height)-1
        while l<r:
            h=min(height[l], height[r])
            max_area=max(max_area, h*(r-l))
            if height[l]< height[r]:
                l+=1
            else:
                r-=1
        return max_area
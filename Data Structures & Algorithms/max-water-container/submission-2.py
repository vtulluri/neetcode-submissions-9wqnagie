class Solution:
    def maxArea(self, heights: List[int]) -> int:
        longest=0
        l=0
        r=len(heights)-1

        while l<r:
            minim=min(heights[l], heights[r])
            # print(minim)
            temp=(r-l)*minim
            longest=max(temp, longest)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return longest

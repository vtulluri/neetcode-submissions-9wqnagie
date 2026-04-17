class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        res=1000000000
        total=0
        for r in range(len(nums)):
            total+=nums[r]

            while total>=target:
                res= min(res, r-l+1)
                total-=nums[l]
                l+=1
        return 0 if res==1000000000 else res
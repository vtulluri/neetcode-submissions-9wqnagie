class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum=0
        count=0
        prefix = defaultdict(int)
        prefix[0]=1

        for num in nums:
            curr_sum+=num
            count+=prefix[curr_sum-k]
            prefix[curr_sum]+=1
        return count
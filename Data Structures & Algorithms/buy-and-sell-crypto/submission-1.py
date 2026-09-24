class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        long=0

        while r<len(prices):
            if prices[r]-prices[l]<0:
                l=r
                r+=1
            else:
                tmp=prices[r]-prices[l]
                long=max(tmp, long)
                r+=1
        return long


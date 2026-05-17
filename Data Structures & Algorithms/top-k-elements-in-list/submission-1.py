class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)]

        for n in nums:
            count[n]=1 + count.get(n,0)
        for n, c in count.items():
            # print(count.items())
            freq[c].append(n)
        print(freq)

        res=[]

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res



# import heapq
# from collections import Counter

# class Solution:
#     def topKFrequent(self, nums, k):
#         count = Counter(nums)
#         heap = []
        
#         for num, freq in count.items():
#             heapq.heappush(heap, (freq, num))
#             if len(heap) > k:
#                 heapq.heappop(heap)
        
#         result = []
#         for freq, num in heap:
#             result.append(num)
        
#         return result


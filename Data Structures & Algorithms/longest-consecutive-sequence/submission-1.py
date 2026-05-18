class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest=0
        for n in numSet:
            if n-1 not in numSet:
                length=0
                while n+length in numSet:
                    length+=1
                    longest=max(length, longest)
        return longest


# Since we need O(n), sorting is not allowed.
# I'll store all numbers in a HashSet for O(1) lookup.
# Then I’ll only start building a sequence from numbers that don’t have a previous number (n-1).
# From each start, I expand forward and track the length of the sequence.
            

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right=0, len(s)-1
        print(left, right)

        while left<right:
            s[left], s[right]= s[right], s[left]
            left+=1
            right-=1
        # break
        # s[0], s[3]=s[3], s[0]
        # t,e,e, n
        # s
        return s

        return s.reverse()
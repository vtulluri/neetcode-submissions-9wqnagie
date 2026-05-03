class Solution:
    def mySqrt(self, x: int) -> int:
        # l=0
        # r=x
        # res=0

        # while l<=r:
        #     m=(l+r)//2
        #     if x<m**2:
        #         r=m-1
        #     elif x>m**2:
        #         l=m+1
        #         res=m
        #     else:
        #         return m
        # return res
        l,r=0,x
        res=0
    
        while l<=r:
            # m=l+((r-l)//2)
            m=(l+r)//2
            if m**2>x:
                r=m-1
            elif m**2<x:
                l=m+1
                res=m
            else:
                return m
        return res
        # r
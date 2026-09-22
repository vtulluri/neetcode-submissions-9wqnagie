class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res=set()
        # nums.sort()
        # # print(nums)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if (nums[i]+nums[j]+nums[k])==0:
        #                 tmp=[nums[i], nums[j], nums[k]]
        #                 # print(tmp)
        #                 res.add(tuple(tmp))
        # return [list(i) for i in res]

        # res=set()
        # nums.sort()
        # # print(nums)
        # a=0
        # l=1
        # r=len(nums)-1

        # while l<r:
        #     if (nums[a]+nums[l]+nums[r])==0:
        #         res.add(tuple(nums[a]+nums[l]+nums[r]))
        #     elif (nums[a]+nums[l]+nums[r])>0:
        #         l+=1
        #     else:
        #         r-=1
        # a+=1
        # l+=1

        res=set()
        nums.sort()
        for a in range(len(nums)-2):
            i,j=a+1,len(nums)-1
            while i<j:
                total=nums[a]+nums[i]+nums[j]
                if total>0:
                    j-=1
                elif total<0:
                    i+=1
                else:
                    res.add((nums[a],nums[i],nums[j]))
                    i+=1
                    j-=1
        return [list(i) for i in res]
        





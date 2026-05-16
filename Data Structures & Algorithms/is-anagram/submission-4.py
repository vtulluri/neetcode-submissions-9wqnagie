class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        count={}

        for ch in s:
            count[ch]=count.get(ch, 0)+1
        # print(count)

        for ch in t:
            if ch not in count:
                return False
            count[ch]-=1
            if count[ch]==0:
                del count[ch]  

        return len(count)==0
        print(count)

        # #count s 
        # count t - from count s 
        # if hashmap== empty then true else return false 


        



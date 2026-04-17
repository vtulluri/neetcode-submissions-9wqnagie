from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        
        if len1 > len2:
            return False
        
        need = Counter(s1)
        window = Counter()
        
        left = 0
        
        for right in range(len2):
            window[s2[right]] += 1
            
            # keep window size fixed
            if right - left + 1 > len1:
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            
            # compare frequencies
            if window == need:
                return True
        
        return False
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams_map={}

        for word in strs:

            count=[0] * 26 

            for ch in word:
                index=ord(ch)- ord('a')
                count[index]+=1

            key=tuple(count)

            if key not in anagrams_map:
                anagrams_map[key]=[]

            anagrams_map[key].append(word)

        return list(anagrams_map.values())



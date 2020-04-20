class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for i in strs:
            s=[0]*26
            for j in i:
                s[ord(j)-ord('a')]+=1
            res[tuple(s)].append(i)
        return res.values()
         
                
     

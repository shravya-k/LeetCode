class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumdic=defaultdict(int)
        sumarr=[]
        t=0
        cnt=0
        for i in nums:
            t+=i
            sumarr.append(t)
        
        for key in sumarr:
            print(key,key-k)
            if key==k:
                cnt+=1
            if key-k in sumdic:
                cnt+=sumdic[key-k]
            sumdic[key]+=1
        return cnt
            

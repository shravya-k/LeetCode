class Solution:
    import collections
    def findMaxLength(self, nums: List[int]) -> int:
        dic=collections.defaultdict(list)
        fin=0
        res=0
        for i in range(len(nums)):
            if nums[i]==1:
                fin+=1
            if nums[i]==0:
                fin+=(-1)        
            dic[fin].append(i)
            if fin==0:
                temp=i-0+1
                res=max(temp,res)
            else:
                if len(dic)>1:
                    temp=i-(dic[fin][0])
                    res=max(temp,res)
        return res
        
            
            
            
          
        


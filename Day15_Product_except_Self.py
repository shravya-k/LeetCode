class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        left=[]
        ryt=[]
        res=[]
        prod=1
    
        for i in range(len(nums)):
            prod*=nums[i]
            left.append(prod)
            
        prod=1
        for j in range(len(nums)):
            prod*=nums[len(nums)-j-1]
            ryt.append(prod)
        ryt=ryt[::-1]
        #print(left,ryt)
        for j in range(len(nums)):
            if ((j-1)>=0) and ((j+1)<=len(nums)-1):
                res.append(left[j-1]*ryt[j+1])
            else:
                if not (j-1)>=0:
                    res.append(ryt[j+1])
                if not ((j+1)<=len(nums)-1):
                    res.append(left[(j-1)])
                
            
            
        return res
        
        

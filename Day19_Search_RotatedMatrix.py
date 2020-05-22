class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarysearch(key,arr,l,r):
            #print(arr,l,r)
            if l<=r:
                m=int((r+l)//2)
                if arr[m]==key:
                    #print('yes')
                    return m
                if key>arr[m]:
                    return binarysearch(key,arr,m+1,r)
                elif key<arr[m]:   
                    return binarysearch(key,arr,l,m-1)
            return -1
            
        pivot=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                #print(nums[i],nums[i+1],pivot)
                pivot=i
       # nums=sorted(nums)
        #print(pivot)
        #print(nums[0]<=target<=nums[pivot])
       # return(binarysearch(target,nums,pivot+1,len(nums)-1))
        if len(nums)>0:
            if nums[0]<=target<=nums[pivot]:
               # print(nums[0]<=target,nums[pivot])
                return(binarysearch(target,nums,0,pivot))
            return(binarysearch(target,nums,pivot+1,len(nums)-1))
        return -1
        
            
            
        
        
        
            
        
            
        

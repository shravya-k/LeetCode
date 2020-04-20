class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        key=0
        for i in range(l):
            
            if nums[key]==0:
                
                nums.pop(key)
                nums.append(0)
                #print(i,key,nums)
            else:
                key+=1

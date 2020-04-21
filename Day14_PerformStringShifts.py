class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        shift=shift[::-1]
        for i in range(len(shift)):
            arr=shift.pop()
            if arr[0]==0:
                s=s[arr[1]:]+s[:arr[1]]
            if arr[0]==1:     
                s=s[(len(s)-arr[1]):]+s[:(len(s)-arr[1])]
        return(s)
            

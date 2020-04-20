class Solution:
    def isHappy(self, n: int) -> bool:
        l=set()
        def findsq(n):
            summ=0
            while n!=0:
                summ=summ+((n%10)*(n%10))
                n=int(n/10)
                #print(summ)
            return(summ)
        s=set()
        while n!=1 and (n not in s):
            s.add(n)
            n=findsq(n)
        return n==1
            
            
        
        
        

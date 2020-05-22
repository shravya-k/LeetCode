class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        table= [[0 for i in range(len(text1)+1)] for j in range(len(text2)+1)]
        n1=len(text1)
        n2=len(text2)
        
        for i in range(1,n2+1):
            for j in range(1,n1+1):
                if text2[i-1]==text1[j-1]:
                    table[i][j]=table[i-1][j-1]+1
                else:
                    table[i][j]=max(table[i][j-1],table[i-1][j])
               
                
        return table[n2][n1]
        
        

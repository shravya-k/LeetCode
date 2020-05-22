# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        def construct(root,value):
            if root:
                if root.val>value:
                    if root.left:
                        construct(root.left,value)
                    else:
                        root.left=TreeNode(value)
                elif root.val<value:
                    if root.right:
                        construct(root.right,value)
                    else:
                        root.right=TreeNode(value)
                    
            
       
        root=TreeNode(preorder[0])
        for i in range(1,len(preorder)):
            construct(root,preorder[i])
        return(root)
            
            
            
            
                    
            
            
            
            
        
        
        
                
        

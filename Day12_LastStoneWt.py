class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res=0
        
        def height(root):
            if root:
                return max(height(root.left),height(root.right))+1
            return 0
        
        def inorder(root):
            if root:
                inorder(root.left)
                inorder(root.right)
                #print(((height(root.left)) + (height(root.right)) + 1))
                self.res=max(self.res,((height(root.left)) + (height(root.right)) + 1))   
            return self.res
        
        if root:
            return inorder(root)-1
        return 0


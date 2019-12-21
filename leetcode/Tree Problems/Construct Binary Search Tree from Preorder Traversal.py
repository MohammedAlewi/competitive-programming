# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.preorder=None
        self.bsd=None
        self.tree=None
        self.index=0
        
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        size= 10000*len(preorder)
        self.bsd=['null']*(size)
        self.preorder=preorder
        length=len(self.preorder)
        for i in range(length):
            self.construct(i)
            
        self.tree=TreeNode(None)
        self.tree=self.const_tree(tree=self.tree,i=0)
    
        return self.tree
        
    def construct(self,i,j=0):
        if len(self.bsd)>j and self.bsd[j]=='null':
            self.bsd[j]=self.preorder[i]
        elif self.preorder[i]<self.bsd[j]:
            self.construct(i,2*(j+1)-1)
        elif self.preorder[i]>=self.bsd[j] :
            self.construct(i,2*(j+1))
            
    
 
    def const_tree(self,tree,i):
        if self.bsd[i]=='null':return;
        tree.val=self.bsd[i]
        if len(self.bsd)>2*(i+1) and tree.val!='null':
            tree.left=TreeNode('null')
            tree.right=TreeNode('null')
            tree.left=self.const_tree(tree.left,2*(i+1)-1) 
            tree.right=self.const_tree(tree.right,2*(i+1))
            return tree
        else: return tree
      
        
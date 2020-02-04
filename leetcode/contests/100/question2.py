# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        values=[]
        self.getNumbers(root,values)
        # ans=TreeNode(values[0])
        ans=self.constructTree(values)
        # print(values)
        return ans
    
    
    def getNumbers(self,tree,values):
        if tree!=None:
            self.getNumbers(tree.left,values)
            values.append(tree.val)
            self.getNumbers(tree.right,values)
            
    def constructTree(self,values):
        if len(values)==0:
            return None
        if len(values)==1:
            return TreeNode(values[0])
        root=TreeNode(values[0])
        root.right=self.constructTree(values[1:])
        return root
            
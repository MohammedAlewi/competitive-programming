# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        first=[]
        second=[]
        new=[]
        
        self.traverse_inorder(root1,first)
        self.traverse_inorder(root2,second)
        
        i,j=0,0
        
        while i<len(first) and j <len(second):
            if first[i]<second[j]:
                new.append(first[i])
                i+=1
            else:
                new.append(second[j])
                j+=1
                
        while i<len(first):
            new.append(first[i])
            i+=1
            
        while j <len(second):
            new.append(second[j])
            j+=1
            
        return new
    
    
    def traverse_inorder(self,root,arr):
        if root!=None:
            self.traverse_inorder(root.left,arr)        
            arr.append(root.val)
            self.traverse_inorder(root.right,arr)
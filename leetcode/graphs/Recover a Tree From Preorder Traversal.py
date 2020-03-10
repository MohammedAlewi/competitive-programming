# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.root=None
        
    def recoverFromPreorder(self, S: str) -> TreeNode:
        root=TreeNode(0)
        val=self.construct_tree(S,0,0,root,'l')
        return root.left
    
    def construct_tree(self,str_val,index,parent,root,flag):
        if index>=len(str_val):
            return parent,index
        if flag=='l':
            root.left=TreeNode(self.get_num(str_val,index))
            next_node=root.left
        else:
            root.right=TreeNode(self.get_num(str_val,index))
            next_node=root.right
        index+=len(self.get_num(str_val,index))-1
        dashes= self.dashes(str_val,index+1)
        index+=dashes+1
        
        if parent< dashes:
            values= self.construct_tree(str_val,index,dashes,next_node,'l')
            if values[0]>parent:
                values= self.construct_tree(str_val,values[1],values[0],next_node,'r') 
            dashes=values[0]
            index=values[1]
        return dashes,index
        
        
        
        
    def dashes(self,str_val,index):
        count=0
        while index < len(str_val):
            if str_val[index] == '-':
                count+=1
            else:
                break
            index+=1
        return count
    
    def get_num(self,str_val,index):
        count=''
        while index < len(str_val):
            if str_val[index] != '-':
                count+=str_val[index]
            else:
                break
            index+=1
        return count
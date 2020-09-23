# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        
        while root != None:
          self.stack.append(root)
          root=root.left
        
    def next(self) -> int:
        node =  self.stack.pop()
        self.next_node(node.right)
        
        return node.val
        
    def next_node(self,node):
        if node:
          self.stack.append(node)
          return self.next_node(node.left)

    def hasNext(self) -> bool:
        return len(self.stack)
        
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

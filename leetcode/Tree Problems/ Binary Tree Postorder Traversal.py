# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        tree=root
        stack=[tree]
        stack_covered=[]

        while len(stack):
            node=stack.pop(0)
            if node!=None:
                stack.insert(0,node.left)
                stack.insert(0,node.right)
                stack_covered.insert(0,node.val)

        return stack_covered
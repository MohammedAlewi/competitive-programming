# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deepestLeaves(self,root):
        return self.dfs(root,0)[0]

    def dfs(self,root,level): 
        current=None,level
        if root!=None:
            left=self.dfs(root.left,level+1)
            right=self.dfs(root.right,level+1)
            current=root.val,level
            if left[1] >right[1]  or (right[0]==None  and left[0]!=None) :
                return left
            elif right[1]>left[1] or (right[0]!=None  and left[0]==None):
                return right
            elif right[1]==left[1] and left[0]!=None and right[0]!=None:
                return right[0]+left[0],right[1]
        return current



# tree=TreeNode(5)
# tree.left=TreeNode(1)
# tree.right=TreeNode(2)
# tree.left.left=TreeNode(1)
# tree.left.right=TreeNode(4)
# tree.left.right.left=TreeNode(45)

# tree.right.left=TreeNode(1)
# # tree.right.left=TreeNode(1)
# tree.right.right=TreeNode(3)

# tree.left.right=TreeNode(5)


s=Solution()
ans=s.deepestLeaves(tree)

print(ans)
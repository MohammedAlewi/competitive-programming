class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preorder_rec(tree):
    if tree!=None:
        print(tree.val,end=",")
        preorder_rec(tree.left)
        preorder_rec(tree.right)


def preorder_iter(tree):
    stack=[tree]
    queue_covered=[]

    while len(stack):
        node=stack.pop(0)
        if node!=None:
            stack.insert(0,node.right)
            stack.insert(0,node.left)
            queue_covered.append(node.val)
    return queue_covered

t=TreeNode(7)
temp=t
t.left=TreeNode(2)
t.left.left=TreeNode(1)
t.left.right=TreeNode(10)
t.right=TreeNode(5)
t.right.left=TreeNode(9)
t.right.right=TreeNode(8)


print(preorder_iter(t))
print(preorder_rec(t))
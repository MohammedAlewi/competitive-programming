class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def postorder_iterative(tree):
    stack=[tree]
    stack_covered=[]

    while len(stack):
        node=stack.pop(0)
        if node!=None:
            stack.insert(0,node.left)
            stack.insert(0,node.right)
            stack_covered.insert(0,node.val)
            
    return stack_covered

def postorder_rec(tree):
    if tree!=None:
        postorder_rec(tree.left)
        postorder_rec(tree.right)
        print(tree.val,end=", ")

t=TreeNode(7)
temp=t
t.left=TreeNode(2)
t.left.left=TreeNode(1)
t.left.right=TreeNode(10)
t.right=TreeNode(5)
t.right.left=TreeNode(9)
t.right.right=TreeNode(8)


print(postorder_iterative(t))
print(postorder_rec(t))
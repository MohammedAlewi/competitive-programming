class TreeNode:
    def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None
       self.null='null'

    def __str__(self):
        return str(self.val)

    def construct_tree(self,values,index,root):
        if (0 <= index*2+1 < len(values)) and values[index*2+1]!=self.null:
            root.left=TreeNode(values[index*2+1])
            self.construct_tree(values,index*2+1,root.left)
            
        if (0 <= index*2+2 < len(values)) and values[index*2+2]!=self.null:
            root.right=TreeNode(values[index*2+2])
            self.construct_tree(values,index*2+2,root.right)

    def construct(self,values):
        if not values:
            return None
        parent=TreeNode(values[0])
        self.construct_tree(values,0,parent)
        return parent

    def pre_order(self,root,index=0):
        if root==None:
            return
        print(index,'. ',root.val)
        self.pre_order(root.left,index*2+1)
        self.pre_order(root.right,index*2+2)


def get_element(min_bound,root,max_bound):
    if root==None:
        return None
    if min_bound<=root.val<=max_bound:
        val1=get_element(min_bound,root.left,root.val)
        val2=get_element(root.val,root.right,max_bound)
        return val1 if val1!=None else val2
    else:
        return root

def change_element(min_bound,root,max_bound,element,original):
    if root==None:
        return None
    if min_bound<=element.val<=max_bound:
        temp=root.val
        root.val=element.val
        element.val=temp

        if get_element(float('-inf'),original,float('inf'))==None:
            return original
        element.val=root.val
        root.val=temp

    change_element(min_bound,root.left,root.val,element,original)
    change_element(root.val,root.right,max_bound,element,original)
    





null='null'
parent=TreeNode(None).construct([3,14])

result=get_element(float('-inf'),parent,float('inf'))
change_element(float('-inf'),parent,float('inf'),result,parent)

print(result)
TreeNode(None).pre_order(parent)





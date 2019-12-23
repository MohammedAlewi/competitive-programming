# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        x=head
        y=ListNode(0)
        self.swap(x,y)

        return y.next

    def swap(self,root,prev):
        if root==None or root.next==None:return
        x=root.next
        if prev!=None:prev.next=x
        root.next=x.next
        x.next=root
        self.swap(root.next,root)

    def print_q(self,node):
        while(node!=None):
            print(node.val,end=", ")
            node=node.next
        print()

x=ListNode(1)
x.next=ListNode(2)
x.next.next=ListNode(3)
x.next.next.next=ListNode(4)

s=Solution()
s.print_q(x)
d=s.swapPairs(x)
s.print_q(d)
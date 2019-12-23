# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.vals=[]
    def nextLargerNodes(self, head: ListNode):
        if head==None: return self.vals
        self.vals.append(self.find_next(head,head.val))
        return self.nextLargerNodes(head.next)

    def find_next(self,head,num):
        if head==None: return 0
        elif num<head.val: return head.val
        return self.find_next(head.next,num)

    def print_q(self,node):
        while(node!=None):
            print(node.val,end=", ")
            node=node.next
        print()

a=ListNode(2)
x=a
x.next=ListNode(7)
x=x.next
x.next=ListNode(4)
x=x.next
x.next=ListNode(3)
x=x.next
x.next=ListNode(5)

s=Solution()
d=s.nextLargerNodes(a)
print(d)
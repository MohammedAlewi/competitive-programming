# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        temp =None
        
        while(head!=None):
            n1=ListNode(head.val)
            n1.next=temp
            temp=n1
            head=head.next
        return temp
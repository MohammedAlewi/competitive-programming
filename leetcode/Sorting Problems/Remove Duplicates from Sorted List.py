# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        l=head
        while(head!=None and head.next!=None):
            if(head.val==head.next.val):
                head.next=head.next.next 
            else:
                head=head.next
        return l
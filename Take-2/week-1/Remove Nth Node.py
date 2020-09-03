# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return None
        
        result = self.removeNode(head,n)
        return result[0]
        
        
    def removeNode(self,head,n):
        if head.next == None:
            if n == 1:
                return None,1
            else:
                return head,1
            
        next_node = self.removeNode(head.next,n)
        if n == next_node[1]+1:
            return next_node[0], next_node[1]+1
        
        head.next = next_node[0]
        return head, next_node[1]+1
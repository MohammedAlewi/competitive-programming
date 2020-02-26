# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        values=[]
        heapq.heapify(values)
        for head in lists:
            
            while head!=None:
                heapq.heappush(values,head.val)
                head=head.next
                
        final=ListNode(None)
        link=final
        while  len(values):
            final.next=ListNode(heapq.heappop(values))
            final=final.next
            
        return link.next
                
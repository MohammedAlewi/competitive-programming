# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count=0
        connected=False
        nums=set(G)
        
        while head!=None:
            if head.val in nums:
                connected=True
            else:
                if connected:
                    count+=1
                connected=False
            head=head.next
        
        if connected:
            count+=1
        return count
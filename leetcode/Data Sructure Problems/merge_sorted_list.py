# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if(l1==None):return l2
        elif(l2==None):return l1
        
        if(l1.val>l2.val):
            node=ListNode(l2.val)
            l3=node
            l2=l2.next
        else:
            node=ListNode(l1.val)
            l3=node
            l1=l1.next
        
        l=l3
        while(l1!=None and l2!=None):
            if(l1.val<=l2.val):
                l3.next=ListNode(l1.val)
                l1=l1.next
            else:
                l3.next=ListNode(l2.val)
                l2=l2.next
            l3=l3.next
        l3.next=l2 if(l1==None)else l1
        return l
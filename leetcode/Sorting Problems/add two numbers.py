# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sol=ListNode(0)  
        sum=sol
        carry=0
        sum.val=(l1.val+l2.val)%10
        carry=(carry+l1.val+l2.val)//10
        l1=l1.next
        l2=l2.next
        while(l1!=None or l2!=None):
            val1= l1.val if(l1!=None) else 0
            val2= l2.val if(l2!=None) else 0
            s1=ListNode(0)
            s1.val=(carry+val1+val2)%10
            carry=(carry+val1+val2)//10
            sum.next=s1
            sum=s1
            if(l1!=None): l1=l1.next
            if(l2!=None): l2=l2.next
        if(carry!=0):sum.next=ListNode(carry)
        return sol
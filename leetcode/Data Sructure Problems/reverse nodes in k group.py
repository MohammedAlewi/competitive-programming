# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        new_node=ListNode('START')
        new_node.next=head
        length=self.get_length(head)
        self.reverse(new_node,head,k,length)
        head=new_node.next
        return head
    
    def reverse(self,head,node,k,length):
        if length<k or k==0:return
        start=node
        for i in range(k-1):
            finish=start.next
            start.next=finish.next
            finish.next=head.next
            head.next=finish
        self.reverse(start,start.next,k,length-k)
        
    def get_length(self,head):
        count=head
        i=0
        while(count!=None):
            count=count.next
            i+=1
        return i
        
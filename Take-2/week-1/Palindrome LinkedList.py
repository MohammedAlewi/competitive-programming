# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True
        result = self.checkPalindrome(head,head)
        return result[0]
        
    def checkPalindrome(self,current,head):
        if current.next==None:
            return head.val ==current.val , head.next
        
        
        condition,second = self.checkPalindrome(current.next,head)
        
        if condition == False or second.val != current.val:
            return False,second
        
        return condition,second.next
        
        
        
        
            
            
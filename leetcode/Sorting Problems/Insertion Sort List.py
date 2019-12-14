class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        temp=head
        result=temp
        lenght=self.length(head)
        index=0
        while(index<lenght):
            temp2=head
            for i in range(index):
                if(temp.val<temp2.val):
                    x=temp.val
                    temp.val,temp2.val=temp2.val,x
                temp2=temp2.next
            temp=temp.next
            index+=1
        return result

    def length(self,head):
        length=0
        temp=head
        while(temp!=None):
            length+=1
            temp=temp.next
        return length

    def print(self,head):
        temp=head
        while(temp!=None):
            print(temp.val,end=" ")
            temp=temp.next
        print()
        
        
n=ListNode(5)
g=n
n.next=ListNode(2)
l=[12, 6, 8, 13, 5, 9, 1, 2, 7, 14, 4, 10, 11, 15, 3]
for i in l:
    n=n.next
    n.next=ListNode(i)
 
x=Solution()
x.print(g)
sorted_n=x.insertionSortList(g)
x.print(sorted_n)

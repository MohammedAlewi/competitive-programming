class MyLinkedList:

    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail


    def get(self, index: int) -> int:
        x=0;
        temp=self.head
        while(x<index):
            temp=temp.next
            if(temp==None or temp.val==None):return -1
            x+=1
        return temp.val
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
         

    def addAtHead(self, val: int) -> None:
        n=Node(val)
        if(self.head.val!=None):n.next=self.head
        else: n.next=self.tail
        self.head=n
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        

    def addAtTail(self, val: int) -> None:
        n=Node(val)
        if(self.tail.val==None) :self.tail.val=val;return None
        else: self.tail.next=n
        self.tail=n
        """
        Append a node of value val to the last element of the linked list.
        """
        

    def addAtIndex(self, index: int, val: int) -> None:
        x=0;
        n=Node(val)
        if(index==0):
            n.next=self.head
            self.head=n
            return
        temp=self.head
        while(x+1<index):
            temp=temp.next
            if(temp==None):return ;
            x+=1
        n.next=temp.next
        temp.next=n
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        

    def deleteAtIndex(self, index: int) -> None:
        x=0;
        if(index==0):self.head=self.head.next;return 
        temp=self.head
        while(x+1<index):
            temp=temp.next
            if(temp==None):return ;
            x+=1
        if(temp.next==None):return None;
        temp.next=temp.next.next
        if(temp.next==None):self.tail=temp
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        
        
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
print()

# obj.printer()
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# ["MyLinkedList","addAtHead","deleteAtIndex","deleteAtIndex","addAtTail","deleteAtIndex","addAtTail","addAtTail","addAtHead","addAtIndex","addAtTail","get"]
# [[]           ,[1]            ,[1],           [1],           [7],          [2],          [1],            [8],          [2],    [5,2],       [7],      [2]]

2,1,7,1,8,5,7
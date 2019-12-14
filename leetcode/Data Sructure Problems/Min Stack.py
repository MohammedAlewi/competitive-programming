class MinStack:
    def __init__(self):
        self.head=Node(None)
        self.min=None;

    def push(self, x: int) -> None:
        if(self.min==None):self.min=x
        else: self.min= x if(x<self.min) else self.min
        n=Node(x)
        n.next=self.head
        self.head=n

    def pop(self) -> None:
        if(self.head==None):return
        self.head=self.head.next

    def top(self) -> int:
        if(self.head==None):return
        return self.head.val

    def getMin(self) -> int:
        if(self.head==None):return
        return self.min

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None


x=MinStack()
x.push(4)
x.push(-1)


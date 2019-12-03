class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Stack:
    def __init__(self):
        self.node=None

    def push(self,value):
        n=Node(value)
        self.node.next=n
        self.node=self.node.next

    def pop(self):
        val= self.node.val
        self.node
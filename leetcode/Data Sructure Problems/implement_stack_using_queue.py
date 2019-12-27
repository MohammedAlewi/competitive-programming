class MyStack:

    def __init__(self):
        self.qeue=[]
        """
        Initialize your data structure here.
        """
        

    def push(self, x: int) -> None:
        self.qeue.append(x)
        """
        Push element x onto stack.
        """
        

    def pop(self) -> int:
        return self.qeue.pop()
        """
        Removes the element on top of the stack and returns that element.
        """
        

    def top(self) -> int:
        return self.qeue[-1]
        """
        Get the top element.
        """
        

    def empty(self) -> bool:
        return len(self.qeue)==0
        """
        Returns whether the stack is empty.
        """
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
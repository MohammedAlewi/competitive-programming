class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=[]
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        """
        Push element x to the back of queue.
        """
        

    def pop(self) -> int:
        return self.stack.pop(0)
        """
        Removes the element from in front of queue and returns that element.
        """
        

    def peek(self) -> int:
        return self.stack[0]
        """
        Get the front element.
        """
        

    def empty(self) -> bool:
        return len(self.stack)==0
        """
        Returns whether the queue is empty.
        """
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
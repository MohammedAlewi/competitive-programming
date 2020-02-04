class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[] 
        while len(pushed)>0 and len(popped)>0 :
            p1=pushed.pop(0)
            stack.append(p1)
            while(len(stack)>0 and popped[0]==stack[len(stack)-1]):
                popped.pop(0)
                stack.pop()
    
        while len(popped)>0 and len(stack)>0:
            if popped[0]==stack[len(stack)-1]:
                stack.pop()
                popped.pop(0)
            else:
                return False
        return len(popped)==0 and len(pushed)==0 
            
            
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for i in list(num):
            while stack and stack[-1] > int(i) and k>0:
                stack.pop()
                k -= 1
                
            stack.append(int(i))
            
        
        
        while stack and k>0:
            stack.pop()
            k -= 1
            
        
        i = 0
        while i < len(stack) and stack[i] == 0:
            i+=1
            
        result = "".join([str( stack[index] ) for index in range(i,len(stack)) ])
        
        if result == "":
            return "0"
        return result

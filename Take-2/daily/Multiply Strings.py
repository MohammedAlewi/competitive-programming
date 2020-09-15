class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1= "0"* (len(num2)-len(num1)) + num1
        num2= "0"* (len(num1)-len(num2)) + num2
        
        result = []
        buff= 0
        
        i,j= len(num1)-1,len(num1)-1
        
        while j>=0:
            
            k = j
            l = i
            
            total= buff
            while l <= j and k >= i : 
                total += ( int(num1[l]) * int(num2[k]) )
                l,k=l+1,k-1
            
            result.append( str(total %10) )
            buff = total//10
            
            if i > 0:i-=1
            else: j-=1
            
        result.append(str(buff))
        
        while len(result) and result[-1]=="0":
            result.pop()
        
        if len(result)==0:
            result=["0"]
        
        return "".join(result[::-1])
            
        
            

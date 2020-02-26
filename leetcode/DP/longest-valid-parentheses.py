class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_val=0
        i,j=0,1
        while i<len(s):
            ans=self.find_max(s,i,j)
            max_val=max(ans[0],max_val)
            i=max(ans[1],i+1)
            j=i+1
        return max_val
    
    
    def find_max(self,s,i,j):
        count=0
        while i <len(s) and j <len(s):
            if s[i]=="(" and s[j]==")":
                count+=2
                i=j+1
                j=i+1
            elif s[i]==")":
                return count,i
            elif s[i]=="(" and s[j]=="(":
                val=self.find_max(s,j,j+1)
                if val[1]<len(s) and s[val[1]]==")" and s[i]=="(":
                    count+=val[0]+2
                    i=val[1]+1
                    j=i+1
                else:
                    return max(count,val[0]),val[1]
        return count,i
        
            
            
        
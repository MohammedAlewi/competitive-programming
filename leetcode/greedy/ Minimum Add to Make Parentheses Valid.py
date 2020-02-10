class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack={}
        stack['(']=0
        count=0
        for i in S:
            if stack['(']==0 and i not in stack:
                count+=1
            elif i not in stack:
                stack['(']-=1
            else:
                stack[i]+=1
        result=stack['(']+count
        return result
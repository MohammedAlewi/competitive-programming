class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n<1:
            return [""]
        elif n==1:
            return ['()']
        else:
            values= self.generateParenthesis(n-1)
            result=set()
            for val in values:
                result.add('('+val+')')                
                result.add(val+'()')
                result.add('()'+val)
            
            return list(result)
    def insert_parenthesis(n,result):
        new=[]
        pos=0
        for val in result:
            if val=='(':
                new.append(val)
            else:
                new.pop()
            
            
            
            
            
        

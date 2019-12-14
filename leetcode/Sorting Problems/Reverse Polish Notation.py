import math
class Solution:
    def evalRPN(self, tokens):
        pass

    def excute(self,token):
        index=0
        op=['+','-', '*', '/']
        x=0
        while(len(token)>1):
            if token[index] in op:
                result=str(self.calculate(token[index-2],token[index],token[index-1]))
                token[index-2]=result
                token=token[:index-1]+token[index+1:]
                index-=2
            x+=1
            index+=1
        return token[0]


    def calculate(self,val1,op,val2):
        if(op=='+'): return int(val1)+int(val2)
        elif(op=='-'): return int(val1)-int(val2)
        elif(op=='*'): return int(val1)*int(val2)
        elif(op=='/'): return self.divied(val1,val2)

    def divied(self,val1,val2):
        r=abs(int(val1))//abs(int(val2))
        if ((int(val1)//int(val2))<0): r=r *-1
        return r

x=Solution()
a=["4", "13", "5", "/", "+"]
a=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(x.excute(a))
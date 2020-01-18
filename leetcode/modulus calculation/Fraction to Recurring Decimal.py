class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        result=abs(numerator)//abs(denominator)
        result=str(result)
        sign=''
        if numerator<0 and denominator>0 or numerator>0 and denominator<0:
            sign='-'
        rem=(abs(numerator)%abs(denominator))*10
        decimal_p=self.divied(abs(denominator),rem)
        return sign+result+decimal_p

    def divied(self,a,b):
        decimal_point=[]
        rem={}
        while b!=0:
            tmp=b
            if rem.get(tmp)!=None:
                index=rem.get(tmp)
                return self.put_bracket(decimal_point,index)
            decimal_point.append(b//a)
            rem[tmp]=len(rem.values())
            b=(b%a)*10
            tmp=b%a
        return self.normal_num(decimal_point)

    def normal_num(self,decimal_point):
        str_="." if len(decimal_point)>0 else ""
        for i in decimal_point:
            str_+=str(i)
        return str_

    def put_bracket(self,decimal_point,index):
        str_="." if len(decimal_point)>0 else ""
        for i in range(len(decimal_point)):
            if index==i:
                str_+="("
            str_+=str(decimal_point[i])
        str_+=")"
        return str_

x=Solution()
r=x.fractionToDecimal(-50,8)
print(r)
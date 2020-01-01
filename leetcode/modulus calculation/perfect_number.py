
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <=1 :return False
        sums=self.gcd_cal(num)
        print(sums)
        if num==sums: return True
        return False
        
    def gcd_cal(self,num):
        g_diviser,x=math.floor(math.sqrt(num)),2
        sums=1
        while x<=g_diviser: 
            if num%x==0:
                sums+=x+num/x
            x+=1
        return sums
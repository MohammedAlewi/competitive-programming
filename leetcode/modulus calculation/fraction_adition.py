class Solution:
    def fractionAddition(self, expression: str) -> str:
        n,d=self.parse_input(expression)
        return self.calculate(n,d)
        
    def parse_input(self,expression):
        nums=expression.split("/")
        n=[int(nums[0])]
        d=[]
        for i in range(1,len(nums)-1):  
            val=nums[i].split("+")
            if nums[i].rfind("+")==-1:
                index=nums[i].rfind("-")
                val=[nums[i][:index],nums[i][index:]]
            d.append(int(val[0]))
            n.append(int(val[1])) 
        d.append(int(nums[len(nums)-1]))
        return n,d
    
    def gcd(self,a,b):
        if a%b==0:return b
        return self.gcd(b,a%b)
    
    def calculate(self,n,d):
        gcd_val=d[0]
        for i in d:
            gcd_val=i*gcd_val//self.gcd(gcd_val,i)
            
        mul=[gcd_val//i for i in d]
        sums=0
        for i in range(len(n)):
            sums+=n[i]*mul[i]
        diviser=self.gcd(sums,gcd_val)
        
        return str(sums//diviser)+"/"+str(gcd_val//diviser)
        
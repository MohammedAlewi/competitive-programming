class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        ans=self.calculate(self.pars_input(a),self.pars_input(b))
        return ans
        
    def calculate(self,a,b):
        real_num=a[0]*b[0]+ a[1]*b[1]*-1
        complex_num=a[0]*b[1]+a[1]*b[0]    
        return str(real_num)+"+"+str(complex_num)+"i"
    
    def pars_input(self,num):
        n,i=num.split("+")
        return int(n),int(i[:-1])
class Solution:
    def findNthDigit(self, n):
        if n//10==0:
            return n
        n-=10
        length=len(str(n))
        x=self.prepare_num(n,length-2,length-1)
        
        num=x//length,x%length
        number=pow(10,length-1)+num[0]
        return str(num[0])#[num[1]]#,number


    def prepare_num(self,n,length,original_len):
        if length<=0:
            return n
        # print(n,(9*pow(10,length))*original_len,length)
        n-=(9*pow(10,length))*original_len
        length-=1
        return self.prepare_num(n,length,original_len)
            
str_=""
for i in range(200):
    str_+=str(i)
# print(str_[201])
x=Solution()
# print(x.findNthDigit(201))
        
# for i in range(len(str_)):
#     print(x.findNthDigit(i),str_[i],i)

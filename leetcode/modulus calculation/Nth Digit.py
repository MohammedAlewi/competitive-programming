import math
class Solution:
    def __init__(self):
        self.value=[0]

    def findNthDigit(self, n):
        x=self.find_num(n)
        # print(x,self.value[0])
        value=str(x)[self.value[0]]
        return value

    def find_num(self,number,current=1,c=1):
        if number<=9*current*c:
            self.value[0]=(number+c-1)%c
            return  math.ceil(number/c)
        number-=9*current*c
        return 9*current + self.find_num(number,current*10,c+1)
# s=[0]
# def find_num(number,current=1,c=1):
#     if number<9*current*c:
#         s[0]=(number+c-1)%c
#         return  math.ceil(number/c)
#     number-=9*current*c
#     return 9*current + find_num(number,current*10,c+1)

str_=""
for i in range(100000):
    str_+=str(i)


x=Solution()
for i in range(len(str_)):
    if str(str_[i])!=str(x.findNthDigit(i)):
        print(str(str_[i]),str(x.findNthDigit(i)),i,len(str_))
        break
# print(str(str_[9]),str(x.findNthDigit(9)))
# print(find_num(8975))
    
        
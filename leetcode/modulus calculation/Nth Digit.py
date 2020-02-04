import math
class Solution:
    def __init__(self):
        self.value=[0]

    def findNthDigit(self, n):
        x=self.find_num(n)
        value=str(x)[self.value[0]]
        return value

    def find_num(self,number,current=1,digit_size=1):
        if number<=9*current*digit_size:
            self.value[0]=(number+digit_size-1)%digit_size
            return  math.ceil(number/digit_size)
        number-=9*current*digit_size
        return 9*current + self.find_num(number,current*10,digit_size+1)


str_=""
for i in range(100000):
    str_+=str(i)

# print(str_[193])


x=Solution()
print(x.findNthDigit(2147483647))
# print(x.findNthDigit(193))










# for i in range(len(str_)):
#     if str(str_[i])!=str(x.findNthDigit(i)):
#         print(str(str_[i]),str(x.findNthDigit(i)),i,len(str_))
#         break
# print("PASSED")
    
        
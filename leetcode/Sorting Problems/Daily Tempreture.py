
class Solution:
    def dailyTemperatures(self, T):
        result=[]
        lenght=len(T)
        for i in range(lenght):
            result.append(self.checkWarmTemp(T[i:]))
        return result
        
    def checkWarmTemp(self,temp):
        lenght=len(temp)
        for i in range(1,lenght):
            if(temp[0]<temp[i]): return i
        return 0

s=Solution()
print(s.dailyTemperatures([34,23,43,45,34,12,49,22,34,21,43,121]))
#[2, 1, 1, 3, 2, 1, 5, 1, 2, 1, 1, 0]
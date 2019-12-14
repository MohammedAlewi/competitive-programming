
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

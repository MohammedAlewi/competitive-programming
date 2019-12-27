class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result=[0]*len(T)
        lenght=len(T)
        m=[(T[0],0)]
        for i in range(1,lenght):
            if len(m)>0 and T[i]>m[len(m)-1][0]:
                while(len(m)>0 and T[i]>m[len(m)-1][0]):
                    result[m[len(m)-1][1]]=i-m[len(m)-1][1]
                    m.pop()
            m.append((T[i],i))
        return result
        

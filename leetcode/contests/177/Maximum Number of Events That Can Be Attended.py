class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda value:value[1])
        dates=[False]*100005

        for i in events:
            for j in range(i[0],i[1]+1):
                if dates[j]==False:
                    dates[j]=True
                    break
                    
        counts=0
        for i in dates:
            if i:
                counts+=1
        return counts
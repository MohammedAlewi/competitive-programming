class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda value:value[1])
        dates=set()
        count=0
        for event in events:
            for j in range(event[0],event[1]+1):
                if  j not in dates:
                    dates.add(j)
                    count+=1
                    break
                    
        return count

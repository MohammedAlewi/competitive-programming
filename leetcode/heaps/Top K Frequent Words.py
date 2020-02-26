class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
                    
        values={}
        for i in words:
            if values.get(i)==None:
                values[i]=0
            values[i]-=1
            
        value=[(values[key], key) for key in values.keys()]
        heapq.heapify(value)
        ans= heapq.nsmallest(k,value)
        return [word for _,word in ans]
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values={}
        for i in nums:
            if values.get(i)==None:
                values[i]=0
            values[i]+=1
        value=[(values[key], key) for key in values.keys()]
        heapq.heapify(value)
        ans= heapq.nlargest(k,value)
        return [i[1] for i in ans]
    
        
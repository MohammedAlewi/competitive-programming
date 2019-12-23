class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        citations.reverse()
        lenght=len(citations)
        for i in range(lenght):
            if(citations[i]<=i):
                return i
        return lenght
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr =sorted( [ (arr[i], i) for i in range(len(arr)) ])
        rank = [0]*len(arr)
        counter = 0
        prev = float('-inf')
        
        for i in arr:
            if i[0] > prev:
                counter+=1
                prev = i[0]
            rank[i[1]]= counter
            
        return rank
        

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        new_arr=[]
        for num  in A:
            new_arr.append(num*num)
            
        new_arr.sort()
        return new_arr
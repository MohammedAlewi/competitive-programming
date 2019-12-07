class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        lenght=len(A)
        permeter=0
        for i in range(lenght):
            if((lenght-i-3)>=0 and A[lenght-i-1]<(A[lenght-i-2]+A[lenght-i-3])):
                return A[lenght-i-1]+A[lenght-i-2]+A[lenght-i-3]
        return permeter
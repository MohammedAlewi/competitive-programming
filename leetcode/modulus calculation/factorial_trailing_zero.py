class Solution:
    def trailingZeroes(self, n: int) -> int:
        total,next_diviser=0,5
        while next_diviser<=n:
            total+=(n//next_diviser)
            next_diviser*=5
        return total
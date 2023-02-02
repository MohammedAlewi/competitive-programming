class Solution:
    def numberOfWays(self, s: str) -> int:
        def calculate(formatted):
            moves = cum_sum = 0
            y_count = formatted[-1] if formatted else -1
            for j in range(len(formatted) - 3, -1, -2):
                cum_sum += formatted[j + 1] * y_count
                moves += formatted[j] * cum_sum
                y_count += formatted[j]
            return moves
                

        formatted = []
        # x1, y1, x2, y2...
        i,j = 0, 0
        while j < len(s):
            while j < len(s) and s[i] == s[j]:
                j += 1
            formatted.append(j - i)
            i = j
        
        return calculate(formatted) + calculate(formatted[:-1])  
        # "001101000111101010111"

class Solution:
    def integerBreak(self, n: int) -> int:
        values={1:0}
        for j in range(2,n+1):
            buffer=0
            for i in range(1,j):
                first_num=max(i,values[i])
                snd_num=j-i
                val=first_num*snd_num
                if buffer<val:
                    buffer=val
            values[j]=buffer
        return values[n]
            
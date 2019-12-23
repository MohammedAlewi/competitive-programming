class Solution:
    def reverse(self, x: int) -> int:
        val=str(x)
        val2=""
        for i in range(len(val)):
            val2+=val[len(val)-1-i]
        val2='-'+val2[:len(val2)-1] if(val2[len(val2)-1]=='-') else val2   
        val2= int(val2) if (int(val2)<2147483647 and  int(val2)>-2147483648) else 0
        return val2
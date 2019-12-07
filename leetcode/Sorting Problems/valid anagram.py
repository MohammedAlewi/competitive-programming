class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        val1=list(s)
        val2=list(t)
        if(len(val1)!=len(val2)):return False
        for i in val1:
            if( i in val2):val2.remove(i)
        return len(val2)==0
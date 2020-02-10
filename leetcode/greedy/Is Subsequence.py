class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        for i in range(len(t)):
            if j<len(s) and t[i]==s[j]:
                j+=1
            if j==len(s):
                break
        if j==len(s):
            return True
        return False
        
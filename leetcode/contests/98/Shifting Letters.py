class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        for i in range(len(shifts)-2,-1,-1):
            shifts[i]+=shifts[i+1]
        print(shifts)
        
        new_s=[]
        for i in range(len(S)):
            char=((ord(S[i])+shifts[i]-97) % 26) +97
            new_s.append(chr(char))
        new="".join(new_s)
        
        return new
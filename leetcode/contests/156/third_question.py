class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        new=""
        i=0
        while i <= (len(s)-k):
            if s[i:i+k]== s[i]*k:
                i+=k
            else: 
                new+=s[i]
                i+=1
        while i<len(s):
            new+=s[i]
            i+=1
        print(new,s)
        if len(new)==len(s):
            return new
        return self.removeDuplicates(new,k)
                
        
        
s=Solution()
print(s.removeDuplicates("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy",4))




#    length=min(len(s),len(t))
#         max_lens=[]
#         for i in range(length):
#             currentLen=0
#             costs=0
#             for j in range(i,length):
#                 costs+=abs(ord(s[j])-ord(t[j]))
#                 if costs<=maxCost:
#                     currentLen+=1
#                 else:
#                     break
#             max_lens.append(currentLen)
#         return max(max_lens)
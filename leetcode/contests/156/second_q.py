class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        length=min(len(s),len(t))
        lenses=[]
        for j in range(length):
            lenses.append(abs(ord(s[j])-ord(t[j])))
       
        count=0
        curent_count=0
        max_sum=0
        start_index=0
        k=0
        while k < len(lenses) and start_index<len(lenses):
            max_sum+=lenses[k]
            if max_sum<=maxCost:
                curent_count+=1
                k+=1
            else:
                max_sum-=lenses[start_index]
                start_index+=1
            if count<curent_count:
                count=curent_count
        


            # for j in range(len(lenses)):
            # for k in range(j, len(lenses)):
            #     max_sum+=lenses[k]
            #     if max_sum<=maxCost:
            #         curent_count+=1
            #     else:break
            # if count<curent_count:
            #     count=curent_count
            # curent_count=0
            # max_sum=0

        return count
            
        
        
s=Solution()
print(s.equalSubstring("abcd","bcdf",3))




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
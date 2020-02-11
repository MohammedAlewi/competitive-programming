class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
            
        
        l=1
        current=100
        for i in S:
            # print(current)
            if current>=widths[ord(i)-97]:
                current-=widths[ord(i)-97]
            else:
                l+=1
                current=100
                current-=widths[ord(i)-97]
        return [l,100-current]
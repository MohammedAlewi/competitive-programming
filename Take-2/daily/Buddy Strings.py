from collections import Counter
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        a_2 = []
        b_2 = []
        
        if len(A) != len(B) or len(A)<2:
            return False
        
        identical= "".join([A[0]]*len(A))
        if identical == A == B:
            return True
        
        for i in range(len(A)):
            if B[i] != A[i]:
                a_2.append(A[i])
                b_2.append(B[i])
        
        if len(a_2) == len(b_2) == 0 and len(A)>2:
            return max(Counter(A).values()) >=2
        
        if len(a_2) != len(b_2) or len(a_2)!=2:
            return False
        
        return a_2[0] == b_2[1] and a_2[1] == b_2[0]

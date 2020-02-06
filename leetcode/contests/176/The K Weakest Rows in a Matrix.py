class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        l=[]
        for i in range(len(mat)):
            solders=0
            for j in mat[i]:
                solders+=j
            l.append((i,solders))
        
        # x=[l[0]]
        for i in range(1,len(l)):
            x=i
            val=l[x]
            while x>0 and val[1]<l[x-1][1]:
                l[x]=l[x-1]
                x-=1
            l[x]=val
            
        ans=[]
        for j in range(k):
              ans.append(l[j][0])
        return ans
        
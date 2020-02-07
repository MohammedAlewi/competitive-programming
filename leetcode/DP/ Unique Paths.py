class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        l=[1]*(n)
        arr=[]
        arr.append(l)
        
        i,j=0,1
        while i<m:
            new=[1]
            while j<n:
                val=new[j-1]+arr[i][j]
                new.append(val)
                j+=1
            arr.append(new)
            j=1
            i+=1
            
        return arr[m-1][n-1]
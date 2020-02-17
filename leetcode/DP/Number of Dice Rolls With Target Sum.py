class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d==1:
            return 1 if target<=f  else 0
        l=[1]*(f)
        
        for i in range(1,d):
            new=[]
            start=0
            end=0
            sums=l[start]
            for end in range(1,max(len(l)+f,target)):
                if end-start>f and start<len(l) :
                    sums-=l[start]
                    start+=1
                    new.append(sums % 1000000007)
                else:
                    new.append(sums % 1000000007)
                    
                if end <len(l):
                    sums+=l[end]
                    sums=sums
            l=new
        return l[target-d]
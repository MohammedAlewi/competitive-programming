class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        all_list=[0]*(80000)
        
        for i in A:
            all_list[i]+=1
            
        index=[]
        vals=[]
        move=0
        for i in range(0,len(all_list)):
            if all_list[i]>1:
                index.append(i)
                vals.append(all_list[i]-1)
            if all_list[i]==0 and len(index)>0:
                currn=index.pop(0)
                val=vals.pop(0) -1
                move+=i-currn
                if val>0:
                    index=[currn]+index
                    vals=[val]+vals
        return move
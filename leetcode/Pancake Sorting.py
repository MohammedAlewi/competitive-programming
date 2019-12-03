class Solution:
    def pancakeSort(self, A):
        flips=[]
        while(len(A)>0):
            largest=self.max_num_index(A)
            arr=A[:largest+1]
            arr2=A[largest+1:] if(largest+1<len(A)) else []
            A=self.reverse(arr)
            A=self.reverse((A+arr2))
            flips=[A.pop()]+flips
        return flips
        

    def max_num_index(self,list_vals):
        val=list_vals[0]
        result=0
        index=len(list_vals)
        for i in range(index):
            if list_vals[i]>val: result=i;val=list_vals[i]
        return result

    def reverse(self,list_vals):
        val=[]
        for i in list_vals:
            val=[i]+val
        return val

print(Solution().pancakeSort([4,37,12,9,5,2,1]))
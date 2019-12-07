class Solution:
    def pancakeSort(self, A):
        flips=[]
        index=len(A)
        i=0
        while(len(A)*10>i):
            largest=self.max_num_index(A,index)
            print(largest,A[largest])
            arr=A[:largest+1]
            arr2=A[largest+1:] if(largest+1<len(A)) else []
            A=self.reverse(arr)
            print('arr1 :',arr,'  arr2: ',arr2)
            A=(arr2+A)
            print('A ',A)
            # A=self.reverse(A)
            # print('A rev :',A)

            # flips=[A.pop()]+flips
            index-=1
            flips.append(A[largest])
            i+=1
        print('A final :',A)
        return flips
        

    def max_num_index(self,list_vals,index):
        val=list_vals[0]
        result=0
        for i in range(index):
            if list_vals[i]>val: result=i;val=list_vals[i]
        return result

    def reverse(self,list_vals):
        val=[]
        for i in list_vals:
            val=[i]+val
        return val

    def isSorted(self,A):
        for i in range(len(A)):
            if A[i]>A[i+1]:return False
        return True

print(Solution().pancakeSort([3, 2, 4, 1]))
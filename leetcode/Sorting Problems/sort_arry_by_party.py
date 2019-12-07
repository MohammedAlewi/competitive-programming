class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd_list=[i  for i in A if i%2!=0]
        even_list=[i  for i in A if i%2==0]
        index=0
        while(len(A)>index):
            A[index]=even_list.pop()
            index+=1
            A[index]=odd_list.pop()
            index+=1
        return A;

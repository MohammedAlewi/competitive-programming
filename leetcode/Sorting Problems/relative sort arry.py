class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        final=[]
        for i in arr2:
            while(arr1.count(i)>0):
                arr1.remove(i)
                final.append(i)
        arr1.sort()
        return final+arr1
class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        dictValue={}
        for i in arr:
            if dictValue.get(i)==None:
                dictValue[i]=1
            else:
                dictValue[i]+=1
        arr=list(dictValue.values())
        arr.sort()
        for i in range(1,len(arr)):
            if arr[i-1]== arr[i]:
                return False
        return True
        
        
s=Solution()
print(s.uniqueOccurrences([26,2,16,16,5,5,26,2,5,20,20,5,2,20,2,2,20,2,16,20,16,17,16,2,16,20,26,16]))
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic={}
        for i in range(len(arr)):
            if dic.get(arr[i])==None:
                dic[arr[i]]=1
            else:
                dic[arr[i]]+=1
        vals=list(dic.values())
        vals.sort()
        
        size=0
        sums=0
        for i in range(len(vals)-1,-1,-1):
            if sums<len(arr)/2:
                sums+=vals[i]
                size+=1
        return size
                

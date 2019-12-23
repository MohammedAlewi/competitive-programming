class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        d=dict()
        for i in barcodes:
            if(d.get(i)==None):d[i]=1
            else:d[i]+=1
        result=[]
        if(len(barcodes)<3):return barcodes
        while(len(result)<len(barcodes)):
            v=self.max_val(d)
            result+=v+self.max_val(d,v[0])
        return result[:len(barcodes)]
    
    def max_val(self,d,ex=None):
        result=list(d.keys())[0] if list(d.keys())[0]!=ex else list(d.keys())[1]
        for i in d.keys():
            if d.get(i)>d.get(result) and i!=ex:result=i
        d[result]-=1
        return [result] if d[result]>-1 else [-1]   
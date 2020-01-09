class TopVotedCandidate:
    def __init__(self, persons, times):
        self.values={}
        self.ans={}
        self.persons=persons
        self.times=times

    def q(self, t: int) -> int:
        index=self.bin_search_min(self.times,0,t,len(self.times)-1)
        return self.calculate(index)

    def calculate(self,index):
        if self.ans.get(index)!=None:
            return self.ans[index]
        self.values={}
        for i in range(index+1):
            if self.values.get(self.persons[i])==None:
                self.values[self.persons[i]]=0
            self.values[self.persons[i]]+=1
        result=self.max_value(index)
        self.ans[index]=result
        return result
        
    def max_value(self,index):
        max_val=(0,0)
        for key in self.values:
            value=self.values[key]
            if max_val[1]<value:
                max_val=(key,value)
            elif max_val[1]==value and self.persons[index]==key:
                max_val=(key,value)
        return max_val[0]

    def bin_search_min(self,a,l,val,r,min_val=0):
        if r>=l:
            mid=(l+r)//2
            if a[mid]==val:
                return mid
            elif a[mid]<val:
                return self.bin_search_min(a,mid+1,val,r,mid)
            return self.bin_search_min(a,l,val,mid-1,min_val)
        return min_val

obj = TopVotedCandidate([0,1,1,0,0,1,0], [0,5,10,15,20,25,30])
print(obj.q(3))
print(obj.q(12))
print(obj.q(25))
print(obj.q(15))
print(obj.q(24))
print(obj.q(8))

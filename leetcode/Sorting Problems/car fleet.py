class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position)==0:return 0
        fleets=1
        vals=self.prepare_ds(position,speed,target)
        x=list(vals.keys())
        x.sort()
        t=[]
        for i in x:
            for j in vals[i]:
                t.append(j)
                
        min_val=t[-1]
        for i in range(len(t)-1,-1,-1):
            if t[i]> min_val:
                min_val=t[i]
                fleets+=1
            
        return fleets

    def prepare_ds(self,position,speed,target):
        d={}
        lenght=len(position)
        for i in range(lenght):
            if d.get(position[i])==None:d[position[i]]=[]
            d[position[i]].append((target-position[i])/speed[i])
        return d
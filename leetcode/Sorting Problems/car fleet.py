class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        fleets=[]
        lenght=len(position)
        vals=self.prepare_ds(position,speed)
        x=list(vals.keys())
        x.sort()
        x.reverse()
        for i in x:
            val=(x[0]-i+target)/vals[i]
            print(val)
            if(len(fleets)==0 or val>fleets[0]): fleets.insert(0,val)
        return len(fleets)

    def prepare_ds(self,position,speed):
        d={}
        lenght=len(position)
        for i in range(lenght):
            d[position[i]]=speed[i]
        return d
    

x=Solution()
d=x.carFleet(12,[10,8,0,5,3],[2,4,1,1,3])
print(d)
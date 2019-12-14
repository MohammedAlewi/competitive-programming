class RecentCounter:
    def __init__(self):
        self.vals=[]
        self.calls=[]

    def ping(self, t: int) -> int:
        if t ==None :return None
        self.vals.insert(0,t)
        calls=0
        for i in self.vals:
            if(t-3000)>i:break
            calls+=1
        return calls


d=RecentCounter()
print(d.ping(None))
print(d.ping(1))
print(d.ping(100))
print(d.ping(3001))
print(d.ping(3002))
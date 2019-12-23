class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        d=dict()
        for i in points:
            distance=(i[0])**2+(i[1])**2
            if(d.get(distance)==None):d[distance]=[i]
            else:d[distance].append(i)
        val=[]
        keys=list(d.keys())
        keys.sort()
        for i in keys:val+=d[i]
        return val[:K]
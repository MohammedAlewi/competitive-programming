class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        points=self.generatePoints(R,C)
        d=dict()
        for i in points:
            distance=abs(i[0]-r0)+abs(i[1]-c0)
            if(d.get(distance)==None):d[distance]=[i]
            else:d[distance].append(i)
        val=[]
        keys=list(d.keys())
        keys=self.counting_sort(keys)
        for i in keys:val+=d[i]
        return val
    
    def generatePoints(self,row,col):
        points=[]
        for i in range(row):
            for j in range(col):
                points.append((i,j))
        return points
    
    def counting_sort(self,the_list):
        min_val = the_list[0]
        max_val = the_list[0]
        for i in the_list:
            if i > max_val:
                max_val = i
            if i < min_val:
                min_val = i

        final_list = []
        count_holder = {}
        for i in range(min_val, max_val + 1):
            count_holder[i] = 0

        for j in the_list:
            count_holder[j] += 1

        for k in count_holder.keys():
            if count_holder[k] > 0:
                final_list += [k] * count_holder[k]

        return final_list

    
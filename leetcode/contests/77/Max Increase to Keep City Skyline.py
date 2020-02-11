class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        total=0
        for row in grid:
            max_top=max(row)
            for j in range(len(row)):
                max_left=self.getMaxleft(grid,j)
                total+=min(max_left,max_top)-row[j]
                row[j]=min(max_left,max_top)
        return total
    
    
    def getMaxleft(self,grid,index):
        max_val=0
        for i in grid:
            max_val=max(i[index],max_val)
        return max_val
        
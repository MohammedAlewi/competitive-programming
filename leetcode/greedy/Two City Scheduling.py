class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[0]-x[1])
        sums=0
        for i in range(len(costs)//2):
            sums+=costs[i][0]
            
        for i in range(len(costs)//2,len(costs)):
            sums+=costs[i][1]
            
        return sums
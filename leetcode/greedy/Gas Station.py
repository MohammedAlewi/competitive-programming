class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        c=0
        ans=[0]*len(gas)
        start_index=-1
        for i in range(len(gas)*2):
            ans[i%len(gas)]=c+gas[i%len(gas)]-cost[i%len(gas)]
            c=max(0,ans[i%len(gas)])
            if ans[i%len(gas)]<0:
                start_index=-1
            if start_index==-1 and ans[i%len(gas)]>=0:
                start_index=i%len(gas)
        return start_index if min(ans)>=0 else -1
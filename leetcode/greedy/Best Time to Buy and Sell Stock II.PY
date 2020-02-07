class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        buy_flag=False
        buy=0
        current=0
        while current<len(prices)-1:
            if prices[current] > prices[current+1] and buy_flag:
                buy_flag=False
                profit+=prices[current] - buy
                buy=0
                # print(current,"sell")
            elif prices[current]< prices[current+1] and not buy_flag:
                buy=prices[current]
                # print(current,"buy")
                buy_flag=True
            current+=1
        if buy_flag:
            profit+=prices[current] - buy
        return profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        diff = 0
        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                sell = prices[i]
            elif prices[i] > sell:
                sell = prices[i]
                temp = sell - buy
                if temp > diff:
                    diff = temp
                

        
        return diff



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mini = prices[0]
        maxi = prices[0]

        for i in range(len(prices)):
            if prices[i] < maxi:
                ans += maxi-mini
                maxi = prices[i]
                mini = prices[i]
            elif prices[i] > maxi:
                maxi = prices[i]
        if maxi > mini:
            ans += maxi - mini
        return ans